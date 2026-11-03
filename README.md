# Toko Ada Aja (toko dummy untuk demo Ganes)

Website toko serba ada untuk HP (portrait, selebar iPhone 12 = 390 px; di laptop tetap 390 px di tengah).
Kontennya dibaca dari file data, jadi nanti bisa diserap ke 14 menu dashboard Ganes.

## URL

- Toko: https://zhr18.github.io/toko-ada-aja/
- Info untuk diserap: https://zhr18.github.io/toko-ada-aja/info.html
- Repo: https://github.com/zhr18/toko-ada-aja

## Sync dengan Ganes

Ditunda. Akun dev-ganes tidak dipakai untuk v3.5 sementara waktu. Saat dimulai, ikuti `ganes/00_PANDUAN_SYNC.md`.

Widget chat belum terpasang. Tempel kode pasang di `index.html`, blok `GANES WIDGET`.

## Struktur

| Path | Isi |
|---|---|
| `index.html` | Website (Beranda, Kategori, Produk, Promo, Lacak, Bantuan, Keranjang) |
| `info.html` | Halaman statis semua info toko, untuk diserap Knowledge Base |
| `data/products.csv` | **Sumber data produk** (kolom sama dengan dashboard + Atribut) |
| `data/pos_stock.csv` | Stok POS simulasi untuk skenario S03 |
| `data/store.json` | Profil toko, jam buka, promo, pesanan dummy, FAQ |
| `docs/` | PDF kebijakan (1 sengaja hasil scan) |
| `ganes/` | Paket impor dan panduan per menu dashboard |
| `tools/` | `build.py`, `sync_from_ganes.py` |

Semua alamat, nomor, dan pesanan adalah **dummy**. Beberapa data sengaja dibuat untuk skenario demo ax_ganes; lihat `ganes/14_scenario_hooks.md`.
