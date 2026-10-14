# Keputusan Desain Kelompok

## Rancangan yang Menjadi Dasar

Rancangan final kelompok merupakan hasil penggabungan bagian terbaik dari rancangan Arif, Rara, Niken, dan Faris.

Rancangan Niken digunakan sebagai dasar untuk bagian transaksi karena pemisahan `TransaksiPeminjaman` dan `ItemPeminjaman` memudahkan satu transaksi menyimpan beberapa alat serta mendukung pengembalian sebagian.

## Bagian yang Diambil atau Dimodifikasi

- Dari rancangan Arif digunakan konsep class `Mahasiswa` yang menyimpan NIM, nama, nomor HP, dan daftar ID transaksi aktif. Daftar transaksi aktif digunakan untuk menerapkan batas maksimal dua transaksi aktif.
- Dari rancangan Rara digunakan class `Peralatan` dengan kode, nama, kategori, kondisi, dan status ketersediaan. Pencarian alat dikembangkan agar dapat menggunakan kode, sebagian nama, atau kategori.
- Dari rancangan Niken digunakan class `ItemPeminjaman` dan `TransaksiPeminjaman`. Informasi tanggal serta kondisi pengembalian disimpan pada setiap item agar pengembalian sebagian dapat dicatat dengan benar.
- Dari rancangan Faris digunakan class `SistemLaboratorium` sebagai pengelola Dictionary mahasiswa, peralatan, dan transaksi serta class `StatistikPeminjaman` untuk fitur statistik.

## Alasan Memilih Struktur Class

- `Mahasiswa` bertanggung jawab pada data dan status transaksi aktif mahasiswa.
- `Peralatan` bertanggung jawab pada data, kondisi, dan ketersediaan alat.
- `ItemPeminjaman` mewakili satu alat di dalam transaksi dan menyimpan status/tanggal/kondisi pengembalian.
- `TransaksiPeminjaman` mengelola satu transaksi yang berisi beberapa item.
- `SistemLaboratorium` mengelola CRUD, koleksi utama, peminjaman, pengembalian, pencarian, dan riwayat.
- `StatistikPeminjaman` dipisahkan agar perhitungan statistik tidak menambah tanggung jawab class transaksi atau peralatan.

Dictionary digunakan untuk data utama karena NIM, kode alat, dan ID transaksi bersifat unik. List digunakan untuk transaksi aktif mahasiswa dan daftar item transaksi.

## Alternatif Desain yang Tidak Dipilih

Class `Pengembalian` terpisah sempat dipertimbangkan. Alternatif tersebut tidak dipilih karena setiap alat dalam satu transaksi dapat dikembalikan pada waktu dan kondisi yang berbeda. Informasi pengembalian lebih sederhana disimpan langsung pada `ItemPeminjaman`.

Penyimpanan database juga tidak digunakan karena ketentuan proyek mewajibkan built-in collection dan melarang penggunaan database.
