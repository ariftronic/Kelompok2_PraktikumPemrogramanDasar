# Catatan Desain dan Panduan PresentasiV2

## Perubahan desain

- `modules/tampilan.py` berisi function tampilan, bukan class baru. Validasi bisnis tetap di SistemLaboratorium.
- ItemPeminjaman menambah atribut `nama_alat_saat_pinjam` dan `kategori_saat_pinjam` bertipe string.
- TransaksiPeminjaman menambah atribut `nama_mahasiswa_saat_pinjam` bertipe string.
- Referensi objek mahasiswa/alat tetap dipertahankan untuk ketersediaan dan transaksi aktif. String historis digunakan untuk tampilan riwayat agar edit master tidak mengubah nama lama.
- UML final gambar yang sudah ada belum diubah. Saat menyunting di Draw.io, tambahkan ketiga atribut di atas pada class masing-masing. Jumlah class dan hubungan antarclass tetap sama.
- Statistik memakai nama master terbaru; jika nilai teratas seri, implementasi memilih identitas pertama yang ditemukan. Ini bukan peringkat lengkap.

## Urutan demonstrasi

1. Tambah mahasiswa dan dua alat dengan kode berbeda.
2. Tunjukkan tabel data serta pencarian sebagian nama/kategori.
3. Buat transaksi berisi dua alat dan tunjukkan validasi durasi salah.
4. Tampilkan dashboard stok dan transaksi.
5. Kembalikan satu alat baik; tunjukkan status sebagian dikembalikan.
6. Coba hapus mahasiswa aktif; operasi ditolak.
7. Kembalikan alat kedua rusak ringan/berat; transaksi selesai dan alat tidak tersedia.
8. Tampilkan riwayat serta statistik.
9. Edit nama master; tunjukkan riwayat tetap memakai nama saat peminjaman.
10. Keluar dengan konfirmasi setelah demonstrasi selesai.

## Batas cakupan

Tidak menambah penyimpanan file/database, denda, login, atau framework UI. Tantangan A dan B tetap dipakai. Pengujian tidak membuktikan kesempurnaan untuk setiap input atau penggunaan method internal secara bebas; aplikasi dirancang untuk alur menu yang tersedia. Dokumen refleksi dan review resmi hanya diisi setelah kegiatan nyata.
