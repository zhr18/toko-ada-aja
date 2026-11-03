# Panduan sync: Toko Ada Aja ↔ Ganes dashboard

> **Status:** sync ditunda. Akun dev-ganes tidak dipakai untuk v3.5 sementara waktu. Semua file di sini sudah siap diserap saat akun dipakai nanti.

Akun dashboard: ditentukan saat sync dimulai.
Website toko: https://zhr18.github.io/toko-ada-aja/.

## Prinsip

- **Satu sumber data produk**: `data/products.csv`, dengan kolom yang sama seperti tabel Produk di dashboard.
- **Dashboard mengatur chatbot.** Persona, sapaan, warna, jawaban, dan flow chatbot di website diatur dari dashboard. Website hanya memuat widget-nya.
- Kolom yang tidak dikenal dashboard (`Atribut (JSON)`) hanya dipakai website.

## Arah sync

| Arah | Cara |
|---|---|
| Website → dashboard | Upload `01_products_import.csv` di **Products › Upload CSV**. Upload isi `knowledge-base/` di **Knowledge Base**, atau masukkan URL `info.html`. |
| Dashboard → website | **Products › Download CSV**, lalu `python tools/sync_from_ganes.py file.csv`, commit, push. Website langsung memakai harga, stok, dan status dari dashboard. |
| Chatbot di website | Salin kode pasang dari **Persona & Widget** (atau **Chatbot Settings**), tempel di `index.html` di antara `GANES WIDGET START` dan `GANES WIDGET END`. |

## 14 menu

| # | Menu dashboard | File / halaman | Yang dilakukan |
|---|---|---|---|
| 1 | Overview | `12_overview_checklist.md` | Cek angka muncul setelah chat uji |
| 2 | Conversations | `08_conversations_test_script.md` | Jalankan 10 chat uji di website |
| 3 | Answer Gaps | `07_answer_gaps_seed.csv` | Tanyakan pertanyaan yang belum ada jawabannya |
| 4 | Chat Simulator | `06_chat_simulator_tests.csv` | 30 pertanyaan uji + jawaban yang diharapkan |
| 5 | Knowledge Base | `knowledge-base/` + `info.html` | Upload 4 PDF / 3 MD atau masukkan URL |
| 6 | Products | `01_products_import.csv` | Upload CSV (26 SKU) |
| 7 | Chatbot Flow | `05_chatbot_flow.md` | 8 alur percakapan |
| 8 | Persona & Widget | `03_persona_and_widget.md` | Persona "Ayu", sapaan, warna, kode pasang |
| 9 | Organization | `04_organization.md` | Profil toko, jam buka, kontak |
| 10 | Add-ons | `09_add_ons.md` | Order Tracking, Promos, Tickets, Add to Cart, Live Agent |
| 11 | AI Services | `10_ai_services.md` | Atribut produk untuk pencarian |
| 12 | Billing | `13_billing_and_team.md` | Data paket dummy untuk uji |
| 13 | Team | `13_billing_and_team.md` | 3 anggota dummy: Owner, Manager, Staff |
| 14 | Chatbot Settings | `11_chatbot_settings.md` | Bahasa, fallback, handover |

Kait skenario demo ax_ganes: `14_scenario_hooks.md`.
