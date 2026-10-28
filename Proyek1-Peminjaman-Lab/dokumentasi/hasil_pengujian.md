# Hasil Pengujian

Pengujian dilakukan menggunakan file pada folder `tests/` tanpa framework tambahan.

## File Pengujian

- `test_mahasiswa.py` menguji tambah, duplikat NIM, edit, cari, dan hapus mahasiswa.
- `test_peralatan.py` menguji tambah, duplikat kode, ketersediaan, pencarian fleksibel, dan hapus alat.
- `test_transaksi.py` menguji transaksi beberapa alat, status transaksi, penolakan alat tidak tersedia, duplikasi alat, dan dokumentasi keterlambatan.
- `test_pengembalian.py` menguji pengembalian sebagian, kondisi alat, aturan penghapusan alat saat transaksi aktif, dan transaksi selesai.
- `test_skenario_wajib.py` menguji enam skenario yang diwajibkan pada dokumen Proyek 1.

## Skenario Wajib

| No | Skenario | Hasil Diharapkan |
|---|---|---|
| 1 | Tambah beberapa mahasiswa dan peralatan | Data tersimpan |
| 2 | Mahasiswa meminjam beberapa alat dalam satu transaksi | Transaksi berhasil dan alat menjadi tidak tersedia |
| 3 | Meminjam alat yang tidak tersedia | Transaksi ditolak |
| 4 | Mengembalikan sebagian alat | Status transaksi menjadi `sebagian dikembalikan`; alat yang kembali baik tersedia lagi; alat lain tetap dipinjam |
| 5 | Mengembalikan alat rusak ringan/berat | Alat tidak kembali tersedia |
| 6 | Menghapus mahasiswa yang masih memiliki transaksi aktif | Operasi ditolak |

## Cara Menjalankan

Dari folder `Proyek1-Peminjaman-Lab`:

```bash
python -m tests.test_mahasiswa
python -m tests.test_peralatan
python -m tests.test_transaksi
python -m tests.test_pengembalian
python -m tests.test_skenario_wajib
python -m tests.test_validasi
```

## Hasil Aktual Perbaikan Presentasi

Pengujian dijalankan pada 28 Oktober 2026 terhadap kode perbaikan yang berasal dari commit dasar `e5a9d54`, sebelum dikirim ke branch `Presentasi`.

| Modul pengujian | Hasil aktual | Status |
|---|---|---|
| test_mahasiswa | 5 dari 5 lulus | Lulus |
| test_peralatan | 6 dari 6 lulus | Lulus |
| test_transaksi | 6 dari 6 lulus | Lulus |
| test_pengembalian | 6 dari 6 lulus | Lulus |
| test_skenario_wajib | Keenam skenario menghasilkan perilaku yang diharapkan | Lulus |
| test_validasi | 15 dari 15 lulus | Lulus |

Total: 44 pemeriksaan lulus, 0 gagal.

Pengujian tambahan memeriksa batas durasi 0/1/7/8 hari, penolakan transaksi ketiga, status aktif saat pengembalian sebagian, kesempatan meminjam setelah transaksi selesai, kondisi pengembalian tidak valid, pengembalian ulang, dan penggunaan ulang identitas setelah dihapus. Riwayat serta statistik mahasiswa lama tetap dapat dibaca.

## Uji Alur Menu

Alur berikut juga dijalankan melalui input terminal pada `main.py`:

1. Tambah mahasiswa M1 dan alat A1.
2. Buat transaksi TRX001 untuk A1 dengan durasi 7 hari.
3. Pilih pengembalian, masukkan kondisi `bagus`.
4. Pilih `y` untuk mencoba lagi, lalu kembalikan A1 dengan kondisi `baik`.
5. Pilih keluar.

Hasil aktual: kondisi salah ditolak, program tetap berjalan, percobaan berikutnya berhasil dengan status transaksi selesai, dan program keluar normal tanpa traceback. Status: lulus.

Pengujian duplikasi alat kini menggunakan alat tersedia dan memeriksa pesan penolakan duplikasi. Pengujian keterlambatan kini menjalankan method pengembalian sistem, tanpa mengubah atribut item secara langsung.

Hasil ini merupakan pengujian teknis, bukan hasil cross-group code review. Jalankan ulang jika kode berubah.



## Verifikasi PresentasiV2 - 28 Oktober 2026

Basis: branch Presentasi, commit `a510646`. Pengujian dijalankan pada kode V2 sebelum publikasi branch.

| Kelompok | Hasil aktual |
|---|---|
| Enam modul tes sebelumnya | 44/44 lulus |
| test_presentasi_v2 | 12/12 lulus |
| Total pemeriksaan modul | 56/56 lulus |
| Pemeriksaan sintaks compileall | Lulus |
| Alur menu melalui input terminal | 14/14 lulus |

Dua belas pemeriksaan baru menguji HP kosong pada tambah/update, lima variasi kode perintah yang dilarang, nama historis mahasiswa, nama/kategori historis alat, pengembalian setelah edit, edit kosong, dan transaksi baru setelah edit.

Empat belas alur terminal mencakup:

1. Durasi `²`, ditolak lalu `7` diterima.
2. Durasi berisi 5.000 digit, ditolak tanpa ValueError.
3. Durasi `0`, ditolak lalu `7` diterima.
4. Durasi `8`, ditolak lalu `7` diterima.
5. Durasi kosong, ditolak lalu `7` diterima.
6. Durasi `abc`, ditolak lalu `7` diterima.
7. Durasi `01`, ditolak sesuai pilihan menu lalu `7` diterima.
8. Kondisi salah lalu percobaan ulang dengan angka `1`; transaksi selesai.
9. Pembatalan saat memilih alat; transaksi tidak dibuat.
10. Pembatalan saat memilih durasi; transaksi tidak dibuat.
11. Pembatalan hapus/keluar dan jawaban konfirmasi tidak valid; data tetap ada.
12. Penolakan kode alat `selesai` melalui menu.
13. Pengembalian transaksi selesai langsung kembali tanpa meminta alat lagi.
14. Daftar mahasiswa/alat, pencarian dan riwayat kosong, stok tersedia/dipinjam/rusak, serta statistik tanpa transaksi.

Uji alur terminal dijalankan dengan harness eksternal yang mengirim input ke `main.py`; harness bukan dependency aplikasi. Untuk mengulangi secara manual, tambahkan M1/Andi/0812 dan A1/Kamera/media, kemudian ikuti skenario di atas. Semua proses berakhir normal tanpa traceback. Pengujian ini tidak menggantikan cross-group code review atau pemeriksaan diagram UML.
