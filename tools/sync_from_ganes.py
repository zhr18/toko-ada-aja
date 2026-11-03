"""Pull products FROM the dashboard into the website.
   1. Ganes dashboard › Products › Download CSV
   2. python tools/sync_from_ganes.py path/to/downloaded.csv
   The site then shows exactly the dashboard's names, prices, stock and visibility.
   The extra column "Atribut (JSON)" is kept per SKU, because the dashboard CSV does not carry it."""
import csv, json, sys, pathlib, subprocess
ROOT = pathlib.Path(__file__).resolve().parent.parent
COLS = ["SKU","Parent SKU","Nama Produk","Deskripsi Singkat","Harga","Harga Sebelum Diskon","Stok","Visibility","Kategori"]
ALIAS = {"SKU":["sku"],"Parent SKU":["parent sku","parent_sku"],"Nama Produk":["nama produk","product name","name"],"Deskripsi Singkat":["deskripsi singkat","short description","description"],
         "Harga":["harga","price"],"Harga Sebelum Diskon":["harga sebelum diskon","compare at price"],"Stok":["stok","stock"],"Visibility":["visibility","status"],"Kategori":["kategori","category"]}
if len(sys.argv) < 2: sys.exit("usage: python tools/sync_from_ganes.py exported.csv")
src = list(csv.reader(open(sys.argv[1], encoding="utf-8-sig"))); head = [h.strip().lower() for h in src[0]]
ix = {c: next((head.index(a) for a in ALIAS[c] if a in head), -1) for c in COLS}
missing = [c for c, i in ix.items() if i < 0 and c in ("SKU", "Nama Produk", "Harga", "Stok")]
if missing: sys.exit(f"The CSV has no column for: {missing}. Headers found: {src[0]}")
old = {r[0]: r[9] for r in list(csv.reader(open(ROOT/"data/products.csv", encoding="utf-8-sig")))[1:] if len(r) > 9}
with open(ROOT/"data/products.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(COLS + ["Atribut (JSON)"]); n = 0
    for r in src[1:]:
        if not any(x.strip() for x in r): continue
        row = [r[ix[c]].strip() if ix[c] >= 0 and ix[c] < len(r) else "" for c in COLS]
        w.writerow(row + [old.get(row[0], "")]); n += 1
print(f"synced {n} products from {sys.argv[1]}")
subprocess.run([sys.executable, str(ROOT/"tools/build.py")], check=True)
