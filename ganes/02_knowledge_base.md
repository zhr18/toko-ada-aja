# Knowledge Base

Dua cara, pilih yang didukung dashboard:

1. **Upload file** dari folder `knowledge-base/`:
   - `kebijakan-retur.pdf` / `.md`: retur 30 hari
   - `pengiriman-dan-pembayaran.pdf` / `.md`
   - `garansi-elektronik.pdf` / `.md`
   - `promo-cicilan-scan.pdf`: **sengaja hasil scan tanpa teks**. Kemungkinan besar gagal dibaca. Itu kait skenario S09 ("chatbot tidak bisa membaca dokumen"). Jangan dianggap error.
2. **Masukkan URL website**: `https://zhr18.github.io/toko-ada-aja/info.html`. Halaman ini statis (tanpa JavaScript) dan memuat semua info toko, FAQ, kebijakan, dan daftar produk, supaya bisa diserap perayap.

Setelah upload, uji di Chat Simulator dengan baris kategori "Kebijakan" di `06_chat_simulator_tests.csv`.
