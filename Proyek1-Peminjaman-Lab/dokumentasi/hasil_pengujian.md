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
```

Hasil aktual perlu dicatat kembali setelah seluruh file final selesai di-merge ke branch `main`.
