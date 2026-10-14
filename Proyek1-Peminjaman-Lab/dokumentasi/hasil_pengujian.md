# Hasil Pengujian

Pengujian menggunakan file pada folder `tests/` tanpa framework tambahan.

## Ringkasan

- `test_mahasiswa.py`: 5 dari 5 pemeriksaan lulus.
- `test_peralatan.py`: 6 dari 6 pemeriksaan lulus.
- `test_transaksi.py`: 5 dari 5 pemeriksaan lulus.
- `test_pengembalian.py`: 6 dari 6 pemeriksaan lulus.
- `test_skenario_wajib.py`: 6 dari 6 skenario lulus.
- Total pemeriksaan: 28 dari 28 lulus pada verifikasi integrasi sebelum Pull Request ini dibuat.

## Skenario Wajib

| No | Skenario | Hasil Diharapkan |
|---|---|---|
| 1 | Menambah beberapa mahasiswa dan alat | Data berhasil disimpan |
| 2 | Mahasiswa meminjam beberapa alat | Transaksi berhasil dan alat menjadi tidak tersedia |
| 3 | Meminjam alat yang sedang tidak tersedia | Transaksi ditolak |
| 4 | Mengembalikan sebagian alat | Status menjadi `sebagian dikembalikan` |
| 5 | Mengembalikan alat dalam kondisi rusak | Alat tidak kembali tersedia |
| 6 | Menghapus mahasiswa dengan transaksi aktif | Operasi ditolak |

Jalankan dari folder `Proyek1-Peminjaman-Lab`:

```bash
python -m tests.test_skenario_wajib
```