"""Build crawlable pages from the data files.
   python tools/build.py              -> info.html, sitemap.xml, data/products.json
   python tools/build.py --preview X  -> also a single-file preview with the data inlined (for quick sharing)"""
import csv, json, html, sys, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://zhr18.github.io/toko-ada-aja/"
ALIAS = {"sku":["sku"],"parent":["parent sku"],"name":["nama produk","product name","name"],"short":["deskripsi singkat","short description","description"],
         "price":["harga","price"],"before":["harga sebelum diskon","compare at price"],"stock":["stok","stock"],"vis":["visibility","status"],"cat":["kategori","category"],"attrs":["atribut (json)","attributes"]}

def products():
    rows = list(csv.reader(open(ROOT/"data/products.csv", encoding="utf-8-sig")))
    head = [h.strip().lower() for h in rows[0]]; ix = {k: next((head.index(a) for a in v if a in head), -1) for k, v in ALIAS.items()}
    out = []
    for r in rows[1:]:
        g = lambda k: r[ix[k]].strip() if ix[k] >= 0 and ix[k] < len(r) else ""
        n = lambda v: int(re.sub(r"[^\d]", "", v) or 0)
        try: attrs = json.loads(g("attrs")) if g("attrs") else {}
        except Exception: attrs = {}
        out.append({"sku": g("sku"), "parent_sku": g("parent"), "name": g("name"), "short_description": g("short"), "price": n(g("price")),
                    "compare_at_price": n(g("before")), "stock": n(g("stock")), "visibility": g("vis") or "active", "category": g("cat"), "attributes": attrs})
    return [p for p in out if p["sku"]]

P = products(); S = json.load(open(ROOT/"data/store.json", encoding="utf-8"))
(ROOT/"data/products.json").write_text(json.dumps(P, ensure_ascii=False, indent=1), encoding="utf-8")
st = S["store"]; e = html.escape
kb = sorted((ROOT/"ganes/knowledge-base").glob("*.md"))
def md2html(t):
    t = e(t); t = re.sub(r"^## (.+)$", r"<h3>\1</h3>", t, flags=re.M); t = re.sub(r"^# (.+)$", r"<h2>\1</h2>", t, flags=re.M)
    return "".join(f"<p>{x}</p>" if not x.startswith("<h") else x for x in t.split("\n\n") if x.strip())
rp = lambda n: "Rp" + f"{n:,}".replace(",", ".")
page = f"""<!DOCTYPE html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Info lengkap · {e(st['name'])}</title><meta name="description" content="Semua informasi {e(st['name'])}: profil, jam buka, pengiriman, pembayaran, retur, promo, FAQ, dan daftar produk beserta stok.">
<style>body{{max-width:390px;margin:0 auto;padding:16px;font:14px/1.55 system-ui,sans-serif;color:#131A16}}table{{width:100%;border-collapse:collapse;font-size:12.5px}}td,th{{border-bottom:1px solid #eee;padding:6px 4px;text-align:left;vertical-align:top}}h2{{margin-top:28px}}</style></head><body>
<h1>{e(st['name'])}</h1><p>{e(st['tagline'])} {e(st['type'])}. Toko dummy untuk demo Ganes.</p>
<h2>Profil toko</h2><p>Alamat: {e(st['address'])}<br>Telepon/WhatsApp: {e(st['phone'])}<br>Email: {e(st['email'])}<br>Admin (live agent): {e(st['live_agent_hours'])}</p>
<h2>Jam buka</h2><ul>{''.join(f'<li>{e(d)}: {e(h)}</li>' for d,h in st['hours'])}</ul>
<h2>Pengiriman</h2><ul>{''.join(f'<li>{e(x)}</li>' for x in st['delivery'])}</ul>
<h2>Pembayaran</h2><ul>{''.join(f'<li>{e(x)}</li>' for x in st['payment'])}</ul>
<h2>Retur (ringkas di profil toko)</h2><p>Retur dan penukaran maksimal {st['return_days_profile']} hari setelah barang diterima.</p>
<h2>Promo</h2><ul>{''.join(f"<li><b>{e(x['title'])}</b>: {e(x['body'])} ({e(x['period'])})</li>" for x in S['promos'])}</ul>
<h2>Pertanyaan umum</h2>{''.join(f'<h3>{e(q)}</h3><p>{e(a)}</p>' for q,a in S['faq'])}
<h2>Dokumen kebijakan</h2>{''.join(md2html(f.read_text(encoding='utf-8')) for f in kb)}
<h2>Daftar produk</h2><table><tr><th>SKU</th><th>Produk</th><th>Harga</th><th>Stok</th><th>Kategori</th></tr>
{''.join(f"<tr><td>{e(p['sku'])}</td><td>{e(p['name'])}<br><small>{e(p['short_description'] or 'Deskripsi belum tersedia')}</small></td><td>{rp(p['price'])}</td><td>{p['stock'] if p['stock'] else 'Habis'}</td><td>{e(p['category'])}</td></tr>" for p in P if p['visibility']=='active')}
</table><p><a href="./">Kembali ke toko</a></p></body></html>"""
(ROOT/"info.html").write_text(page, encoding="utf-8")
(ROOT/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{BASE}{u}</loc></url>\n" for u in ["", "info.html"] + [f"docs/{f.name}" for f in sorted((ROOT/'docs').glob('*.pdf'))]) + "</urlset>\n", encoding="utf-8")
if "--preview" in sys.argv:
    out = pathlib.Path(sys.argv[sys.argv.index("--preview") + 1])
    idx = (ROOT/"index.html").read_text(encoding="utf-8")
    inline = "<script>window.__CSV__=" + json.dumps((ROOT/"data/products.csv").read_text(encoding="utf-8-sig")) + ";window.__STORE__=" + json.dumps(S, ensure_ascii=False) + ";</script>\n"
    out.write_text(idx.replace("<!-- GANES WIDGET START -->", inline + "<!-- GANES WIDGET START -->"), encoding="utf-8")
print(f"built: {len(P)} products · info.html · sitemap.xml · data/products.json")
