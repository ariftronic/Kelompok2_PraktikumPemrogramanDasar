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
│   ├── statistik.py
│   └── tampilan.py
├── tests/
│   ├── __init__.py
│   ├── test_mahasiswa.py
│   ├── test_peralatan.py
│   ├── test_transaksi.py
│   ├── test_pengembalian.py
│   ├── test_skenario_wajib.py
│   ├── test_validasi.py
│   └── test_presentasi_v2.py
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
python -m tests.test_validasi
python -m tests.test_presentasi_v2
```

Pengujian dibuat dengan function, `if`, dan `print` tanpa framework tambahan agar tetap sesuai materi praktikum.

## Perbaikan untuk Presentasi

- Salah ketik kondisi pengembalian ditolak tanpa menghentikan menu; pengguna dapat mencoba lagi.
- NIM dan kode alat yang tercatat dalam riwayat tidak dapat didaftarkan ulang setelah dihapus, agar riwayat dan statistik tidak bercampur dengan identitas baru. Ini keputusan desain tambahan, bukan aturan eksplisit pada soal.
- Pengujian duplikasi memakai alat yang masih tersedia. Pengujian keterlambatan melalui proses pengembalian sistem.
- Pengujian tambahan menggunakan function, List, perulangan, percabangan, dan print tanpa framework baru.

Data hanya disimpan selama program berjalan. Review antarkelompok dan refleksi tetap perlu dilengkapi setelah kegiatan tersebut dilakukan.


## PresentasiV2 - Tampilan dan Validasi

Jalankan `python main.py` dari folder `Proyek1-Peminjaman-Lab`. Gunakan terminal dengan lebar minimal 76 kolom agar tabel dan dua kolom menu terlihat rapi. Tidak perlu memasang library tambahan.

- Dashboard menunjukkan jumlah mahasiswa, alat, transaksi aktif, dan kondisi stok.
- Menu dikelompokkan menjadi data master, transaksi, pemantauan, dan laporan.
- Daftar mahasiswa dan alat menggunakan tabel. Teks panjang ditampilkan utuh sebagai detail.
- Pesan `[OK]`, `[!]`, dan `[INFO]` membedakan keberhasilan, penolakan, dan informasi.
- Hapus data dan keluar program meminta konfirmasi `y/n`; jawaban lain diminta ulang.
- Peminjaman menampilkan alat tersedia. Ketik `selesai` untuk lanjut atau `batal` untuk membatalkan.
- Durasi harus salah satu pilihan `1` sampai `7`. Input salah diminta ulang tanpa mengubah stok.
- Pengembalian menampilkan rincian transaksi dan menerima kondisi `1`/`2`/`3` atau teks kondisi. Ketik `batal` pada kode alat untuk kembali.
- Nomor HP tidak boleh kosong. Format nomor tidak dibatasi agar tidak menambahkan asumsi di luar soal.
- Kode `selesai` dan `batal` tidak dapat digunakan sebagai kode alat karena dipakai oleh menu.
- Riwayat menampilkan nama mahasiswa dan alat saat transaksi dibuat; data master dan statistik tetap menggunakan nama terbaru untuk identitas yang sama.

Perbaikan menggunakan function, string, List/Dictionary, loop, percabangan, atribut objek, serta format f-string. Tidak ada database, framework UI, inheritance tambahan, atau dependency baru.

## Batas Pemeriksaan

56 pemeriksaan modul dan 14 alur menu lulus pada kode PresentasiV2. Hasil ini tidak menjamin bebas dari semua bug. Data tetap hanya hidup selama sesi program. Dokumen review antarkelompok/refleksi harus dilengkapi berdasarkan kegiatan nyata. Diagram UML gambar belum diperbarui untuk atribut riwayat baru; lihat catatan perubahan desain pada `dokumentasi/presentasi_v2.md`.
