# Keputusan Desain Kelompok

## Dasar Rancangan

Rancangan final menggunakan class utama `Mahasiswa`, `Peralatan`, `ItemPeminjaman`, `TransaksiPeminjaman`, `SistemLaboratorium`, dan `StatistikPeminjaman`.

## Alasan Pemilihan Class

- `Mahasiswa` menyimpan identitas mahasiswa dan daftar ID transaksi aktif.
- `Peralatan` menyimpan data alat, kondisi, dan status ketersediaan.
- `ItemPeminjaman` mewakili satu alat di dalam satu transaksi sehingga pengembalian sebagian dapat dicatat per alat.
- `TransaksiPeminjaman` mengelola satu transaksi yang dapat berisi beberapa item.
- `SistemLaboratorium` mengelola koleksi mahasiswa, peralatan, transaksi, CRUD, peminjaman, dan pengembalian.
- `StatistikPeminjaman` dipisahkan agar tanggung jawab statistik tidak menumpuk pada class sistem.

## Struktur Data

Dictionary digunakan untuk data utama karena NIM, kode alat, dan ID transaksi bersifat unik. List digunakan untuk menyimpan transaksi aktif mahasiswa dan daftar item di dalam transaksi.

## Alternatif yang Dipertimbangkan

Class `Pengembalian` terpisah sempat dipertimbangkan. Rancangan final menyimpan informasi pengembalian pada `ItemPeminjaman` karena satu transaksi dapat dikembalikan sebagian dan setiap alat dapat mempunyai tanggal serta kondisi kembali yang berbeda.