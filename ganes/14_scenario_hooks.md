# Kait skenario uji ax_ganes dan ganes_saas

Data toko sengaja memuat kondisi untuk 15 skenario di Foundation Library v3.5.0. Semua dummy.

| Skenario | Data atau cara uji di Toko Ada Aja |
| --- | --- |
| S01 Pelanggan minta orang | Rina, chat uji no. 10 di `08_conversations_test_script.md`. Jawaban dari `kebijakan-retur.md` |
| S02 Mulai hari | Gabungan S01, S03, dan S09 sebagai tiga hal yang perlu user |
| S03 Produk habis | `TAA-DR-001` Rice Cooker Mini stok 0 di toko, 12 di `data/pos_stock.csv`. "Ditanya 17×" dibuat dengan chat uji atau disimulasikan |
| S04 Uji chatbot | 30 pertanyaan di `06_chat_simulator_tests.csv` |
| S05 Undo | Lanjutan S03: stok 12 dikembalikan ke 0 |
| S06 Pelanggan menunggu | Chat Rina dibiarkan menunggu saat user di menu lain |
| S07 Tangan sibuk | Chat Rina, dibuka dengan gestur 👍 |
| S08 Orang kedua | Tidak butuh data toko. Data pelanggan terlihat di Conversations |
| S09 Dokumen tidak terbaca | `promo-cicilan-scan.pdf`, 1 halaman hasil scan tanpa lapisan teks. Prototype lama menyebut 3 halaman |
| S10 Ubah harga | `TAA-MM-001` Kopi Robusta. Naik 5%: Rp42.000 → Rp44.100 |
| S11 Deskripsi kosong | `TAA-EL-003` Earphone Bluetooth |
| S12 Cek sisa stok | `TAA-MM-004` Madu Hutan, stok 3 |
| S13 Suara | Pertanyaan yang sama dengan S12 |
| S14 Jam buka | Senin–Sabtu 08.00–21.00 → 09.00–22.00 |
| S15 Kebijakan retur | Profil toko 7 hari vs `kebijakan-retur.pdf` 30 hari |

## Kasus tambahan

| Kasus | Data |
| --- | --- |
| Varian sebagian habis | `TAA-IB-001-L` habis, `TAA-IB-001-M` tersedia |
| Produk nonaktif | `TAA-AT-003` Map Plastik |
| Stok rendah | `TAA-EL-003`, `TAA-IB-003` |
| Role tanpa izin | Nia (Staff) di `13_billing_and_team.md` |
