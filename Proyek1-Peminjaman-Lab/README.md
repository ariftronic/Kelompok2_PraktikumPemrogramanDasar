# Proyek 1 - Sistem Pengelolaan Peminjaman Peralatan Laboratorium

Proyek ini dibuat untuk memenuhi tugas Proyek 1 Praktikum Pemrograman Dasar - Kelompok 2.

## Anggota dan Pembagian Tugas

- Muhammad Nur Arif - class `Mahasiswa`, CRUD mahasiswa, validasi transaksi aktif, pengujian mahasiswa, dan dokumentasi.
- Fatimah Az Zahra (Rara) - class `Peralatan`, CRUD alat, kondisi/ketersediaan alat, pencarian fleksibel, dan pengujian alat.
- Niken Syafira Zulfaida - class `ItemPeminjaman` dan `TransaksiPeminjaman`, status transaksi, pengembalian per item, dan pengujian transaksi.
- Faris Rafiuddin Hannan - class `SistemLaboratorium`, integrasi program, proses pengembalian, class `StatistikPeminjaman`, `main.py`, dan pengujian integrasi.

## Deskripsi Sistem

Aplikasi digunakan untuk mengelola mahasiswa, peralatan laboratorium, transaksi peminjaman, pengembalian sebagian, kondisi alat, tanggal pengembalian, riwayat peminjaman, keterlambatan, dan statistik peminjaman.

Program menggunakan Object-Oriented Programming, List, Dictionary, String, Function/Method, Module, CRUD, perulangan, kondisi, Tuple, dan module bawaan `datetime`. Program tidak menggunakan database.

## Fitur Minimal

1. Kelola data mahasiswa: tambah, edit, hapus, cari.
2. Kelola data alat: tambah, edit, hapus, cari.
3. Membuat transaksi peminjaman.
4. Menampilkan transaksi.
5. Memproses pengembalian alat.
6. Mencari transaksi berdasarkan mahasiswa.
7. Menampilkan alat tersedia.
8. Menampilkan alat yang sedang dipinjam.
9. Menampilkan alat rusak.
10. Menampilkan riwayat peminjaman mahasiswa.
11. Keluar dari program.

Menu statistik ditambahkan sebagai fitur pengembangan.

## Aturan Bisnis

- Alat yang tidak tersedia tidak dapat dipinjam.
- Setiap mahasiswa maksimal memiliki 2 transaksi aktif.
- Satu transaksi dapat berisi beberapa alat menggunakan List.
- Batas peminjaman maksimal 7 hari.
- Pengembalian sebagian diperbolehkan.
- Transaksi tetap aktif sampai seluruh alat dikembalikan.
- Alat kondisi baik kembali tersedia.
- Alat rusak ringan atau rusak berat tidak kembali tersedia.
- Mahasiswa dengan transaksi aktif tidak dapat dihapus.
- Alat yang masih tercatat dalam transaksi aktif tidak dapat dihapus.
- Tanggal pengembalian dan kondisi pengembalian dicatat pada setiap `ItemPeminjaman`.

## Tantangan yang Dipilih

### Tantangan A - Pencarian Fleksibel

Pencarian alat dapat dilakukan berdasarkan kode alat, sebagian nama alat, atau kategori.

### Tantangan B - Statistik Peminjaman

Program menampilkan:
- alat paling sering dipinjam;
- mahasiswa paling sering meminjam;
- jumlah transaksi selesai;
- jumlah transaksi aktif.

## Struktur Folder

```text
Proyek1-Peminjaman-Lab/
├── main.py
├── README.md
├── modules/
│   ├── __init__.py
│   ├── konstanta.py
│   ├── mahasiswa.py
│   ├── peralatan.py
│   ├── transaksi.py
│   ├── sistem_lab.py
│   └── statistik.py
├── tests/
│   ├── __init__.py
│   ├── test_mahasiswa.py
│   ├── test_peralatan.py
│   ├── test_transaksi.py
│   ├── test_pengembalian.py
│   └── test_skenario_wajib.py
└── dokumentasi/
    ├── uml/
    │   ├── individu/
    │   └── final/
    ├── keputusan_desain.md
    ├── hasil_pengujian.md
    ├── kontribusi_anggota.md
    ├── code_review.md
    └── refleksi.md
```

## Cara Menjalankan

Buka terminal pada folder `Proyek1-Peminjaman-Lab`, lalu jalankan:

```bash
python main.py
```

## Cara Menjalankan Pengujian

Pastikan terminal berada pada folder `Proyek1-Peminjaman-Lab`, lalu jalankan:

```bash
python -m tests.test_mahasiswa
python -m tests.test_peralatan
python -m tests.test_transaksi
python -m tests.test_pengembalian
python -m tests.test_skenario_wajib
```

Pengujian dibuat dengan function, `if`, dan `print` tanpa framework tambahan agar tetap sesuai materi praktikum.
