"""Tampilan terminal sederhana, tanpa library tambahan."""


def judul(teks):
    print("\n" + "=" * 76)
    print("  " + teks)
    print("  SISTEM PEMINJAMAN PERALATAN | PRESENTASI V2")
    print("=" * 76)


def pesan_hasil(berhasil, pesan):
    if berhasil:
        print("\n[OK] " + pesan)
    else:
        print("\n[!] " + pesan)


def konfirmasi(teks):
    while True:
        jawaban = input(teks + " (y/n): ").strip().lower()
        if jawaban == "y":
            return True
        if jawaban == "n":
            print("[INFO] Kembali tanpa melanjutkan tindakan.")
            return False
        print("[!] Pilih y atau n.")


def ringkasan(sistem, statistik):
    print("  Mahasiswa: " + str(len(sistem.mahasiswa))
          + "   |   Alat: " + str(len(sistem.peralatan))
          + "   |   Transaksi aktif: " + str(statistik.jumlah_transaksi_aktif()))
    print("  Tersedia: " + str(len(sistem.alat_tersedia()))
          + "    |   Dipinjam: " + str(len(sistem.alat_dipinjam()))
          + "    |   Rusak: " + str(len(sistem.alat_rusak())))
    print("-" * 76)


def tabel_mahasiswa(daftar):
    judul("DAFTAR MAHASISWA")
    print(f"{'NIM':<16} {'NAMA':<24} {'NOMOR HP':<20} {'AKTIF':>6}")
    print("-" * 76)
    for mhs in daftar:
        # Lebar minimum; nilai panjang ditampilkan utuh di baris berikutnya.
        if len(mhs.nim) > 16 or len(mhs.nama) > 24 or len(mhs.no_hp) > 20:
            mhs.tampilkan_info()
            print("-" * 76)
        else:
            print(f"{mhs.nim:<16} {mhs.nama:<24} {mhs.no_hp:<20} {mhs.jumlah_transaksi_aktif():>6}")
    print("-" * 76)
    print("Total: " + str(len(daftar)) + " mahasiswa")


def tabel_alat(daftar):
    judul("DAFTAR PERALATAN")
    print(f"{'KODE':<12} {'NAMA ALAT':<22} {'KATEGORI':<16} {'KONDISI / STATUS'}")
    print("-" * 76)
    for alat in daftar:
        status = alat.kondisi
        if alat.kondisi == "baik":
            if alat.tersedia:
                status = "Tersedia"
            else:
                status = "Dipinjam"
        if len(alat.kode_alat) > 12 or len(alat.nama_alat) > 22 or len(alat.kategori) > 16:
            alat.tampilkan_info()
            print("-" * 76)
        else:
            print(f"{alat.kode_alat:<12} {alat.nama_alat:<22} {alat.kategori:<16} {status}")
    print("-" * 76)
    print("Total: " + str(len(daftar)) + " alat")
