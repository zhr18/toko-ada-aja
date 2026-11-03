# Chatbot Flow

| # | Niat pelanggan | Contoh kalimat | Alur |
|---|---|---|---|
| 1 | Cek stok | "Popok ukuran L ada?" | Cari produk → sebut stok → bila habis, tawarkan varian lain (ukuran M) |
| 2 | Harga & promo | "Kopi berapa? Ada promo?" | Sebut harga → promo yang berlaku → kode bila ada |
| 3 | Lacak pesanan | "Pesanan TAA-240101 sampai mana?" | Minta nomor → status dari Order Tracking |
| 4 | Pengiriman | "Bisa same day ke Bekasi?" | Area + jam batas 14.00 → ongkir |
| 5 | Pembayaran & cicilan | "Bisa cicilan?" | Metode bayar → cicilan dari dokumen promo (gagal bila PDF scan belum terbaca) |
| 6 | Retur | "Barang salah ukuran, bisa tukar?" | Syarat retur → cara mengajukan → serahkan ke admin bila barang sudah dikirim |
| 7 | Jam buka | "Minggu buka jam berapa?" | Jam buka dari Organization |
| 8 | Bicara dengan orang | "Saya mau bicara dengan admin" | Tandai "wants a person" → Needs Attention → admin di jam layanan; di luar jam, buat tiket |
