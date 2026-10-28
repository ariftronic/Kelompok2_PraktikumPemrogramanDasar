from modules.konstanta import MAKS_HARI_PINJAM
from modules.sistem_lab import SistemLaboratorium
from modules.statistik import StatistikPeminjaman
from modules.tampilan import judul, pesan_hasil, konfirmasi, ringkasan, tabel_mahasiswa, tabel_alat


def garis():
    print("-" * 76)


def tampilkan_mahasiswa(daftar):
    if len(daftar) == 0:
        print("Tidak ada data mahasiswa.")
        return

    tabel_mahasiswa(daftar)


def tampilkan_alat(daftar):
    if len(daftar) == 0:
        print("Tidak ada data alat.")
        return

    tabel_alat(daftar)


def tampilkan_transaksi(daftar):
    if len(daftar) == 0:
        print("Tidak ada data transaksi.")
        return

    for trx in daftar:
        garis()
        trx.tampilkan_detail()

    garis()


def menu_mahasiswa(sistem):
    while True:
        judul("DATA MAHASISWA")
        print("1. Tambah mahasiswa")
        print("2. Edit mahasiswa")
        print("3. Hapus mahasiswa")
        print("4. Cari mahasiswa")
        print("5. Tampilkan semua mahasiswa")
        print("0. Kembali")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            nim = input("NIM     : ")
            nama = input("Nama    : ")
            no_hp = input("Nomor HP: ")
            berhasil, pesan = sistem.tambah_mahasiswa(nim, nama, no_hp)
            pesan_hasil(berhasil, pesan)

        elif pilihan == "2":
            nim = input("NIM mahasiswa yang diedit: ").strip()

            if nim not in sistem.mahasiswa:
                print("Mahasiswa tidak ditemukan.")
                continue

            print("Kosongkan data jika tidak ingin mengubah nilainya.")
            nama = input("Nama baru              : ")
            no_hp = input("Nomor HP baru          : ")
            berhasil, pesan = sistem.edit_mahasiswa(nim, nama, no_hp)
            pesan_hasil(berhasil, pesan)

        elif pilihan == "3":
            nim = input("NIM mahasiswa yang dihapus: ")
            if not konfirmasi("Hapus mahasiswa " + nim + "?"):
                continue
            berhasil, pesan = sistem.hapus_mahasiswa(nim)
            pesan_hasil(berhasil, pesan)

        elif pilihan == "4":
            keyword = input("Masukkan NIM atau nama: ")
            tampilkan_mahasiswa(sistem.cari_mahasiswa(keyword))

        elif pilihan == "5":
            tampilkan_mahasiswa(sistem.cari_mahasiswa(""))

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid.")


def menu_alat(sistem):
    while True:
        judul("INVENTARIS ALAT")
        print("1. Tambah alat")
        print("2. Edit alat")
        print("3. Hapus alat")
        print("4. Cari alat")
        print("5. Tampilkan semua alat")
        print("0. Kembali")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            kode = input("Kode alat : ")
            nama = input("Nama alat : ")
            kategori = input("Kategori  : ")
            berhasil, pesan = sistem.tambah_alat(kode, nama, kategori)
            pesan_hasil(berhasil, pesan)

        elif pilihan == "2":
            kode = input("Kode alat yang diedit: ").strip()

            if kode not in sistem.peralatan:
                print("Peralatan tidak ditemukan.")
                continue

            print("Kosongkan data jika tidak ingin mengubah nilainya.")
            nama = input("Nama alat baru        : ")
            kategori = input("Kategori baru         : ")
            berhasil, pesan = sistem.edit_alat(kode, nama, kategori)
            pesan_hasil(berhasil, pesan)

        elif pilihan == "3":
            kode = input("Kode alat yang dihapus: ")
            if not konfirmasi("Hapus alat " + kode + "?"):
                continue
            berhasil, pesan = sistem.hapus_alat(kode)
            pesan_hasil(berhasil, pesan)

        elif pilihan == "4":
            keyword = input("Kode / sebagian nama / kategori: ")
            tampilkan_alat(sistem.cari_alat(keyword))

        elif pilihan == "5":
            tampilkan_alat(sistem.cari_alat(""))

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid.")


def buat_transaksi(sistem):
    judul("PEMINJAMAN BARU")
    nim = input("NIM mahasiswa: ").strip()

    if nim not in sistem.mahasiswa:
        print("Mahasiswa tidak ditemukan.")
        return

    if not sistem.mahasiswa[nim].boleh_meminjam():
        print("Mahasiswa sudah mencapai batas transaksi aktif.")
        return

    tampilkan_alat(sistem.alat_tersedia())
    if len(sistem.alat_tersedia()) == 0:
        return

    daftar_kode = []
    print("Masukkan kode alat satu per satu.")
    print("Ketik 'selesai' untuk lanjut atau 'batal' untuk membatalkan.")

    while True:
        kode = input("Kode alat: ").strip()

        if kode.lower() == "batal":
            print("[INFO] Peminjaman dibatalkan.")
            return

        if kode.lower() == "selesai":
            break

        if kode == "":
            print("Kode alat tidak boleh kosong.")
            continue

        if kode in daftar_kode:
            print("Kode alat sudah dipilih.")
            continue

        if kode not in sistem.peralatan:
            print("Alat tidak ditemukan.")
            continue

        if not sistem.peralatan[kode].dapat_dipinjam():
            print("Alat tidak tersedia.")
            continue

        daftar_kode.append(kode)
        print("Alat ditambahkan ke daftar peminjaman.")

    if len(daftar_kode) == 0:
        print("Transaksi dibatalkan karena belum ada alat yang dipilih.")
        return

    pilihan_hari = []
    for hari in range(1, MAKS_HARI_PINJAM + 1):
        pilihan_hari.append(str(hari))

    while True:
        lama_text = input("Lama pinjam (1-7 hari, batal untuk kembali): ").strip()
        if lama_text.lower() == "batal":
            print("[INFO] Peminjaman dibatalkan.")
            return
        if lama_text in pilihan_hari:
            break
        print("[!] Masukkan pilihan 1 sampai 7 tanpa angka nol di depan.")

    lama_hari = int(lama_text)
    berhasil, pesan, trx = sistem.buat_transaksi(
        nim,
        daftar_kode,
        lama_hari,
    )
    pesan_hasil(berhasil, pesan)

    if berhasil:
        trx.tampilkan_detail()


def proses_pengembalian(sistem):
    judul("PENGEMBALIAN ALAT")
    id_transaksi = input("ID transaksi: ").strip()

    if id_transaksi not in sistem.transaksi:
        print("Transaksi tidak ditemukan.")
        return

    trx = sistem.transaksi[id_transaksi]
    if not trx.aktif():
        print("[INFO] Transaksi ini sudah selesai.")
        return
    trx.tampilkan_detail()
    print("Ketik batal pada kode alat untuk kembali.")

    while True:
        kode_alat = input("Kode alat      : ").strip()
        if kode_alat.lower() == "batal":
            return
        print("  [1] Baik   [2] Rusak ringan   [3] Rusak berat")
        kondisi = input("Pilih kondisi (angka atau teks): ").strip().lower()
        pilihan_kondisi = {"1": "baik", "2": "rusak ringan", "3": "rusak berat"}
        if kondisi in pilihan_kondisi:
            kondisi = pilihan_kondisi[kondisi]

        berhasil, pesan, hasil_trx = sistem.proses_pengembalian(
            id_transaksi,
            kode_alat,
            kondisi,
        )

        pesan_hasil(berhasil, pesan)

        if berhasil:
            trx.tampilkan_detail()

        if not trx.aktif():
            break

        if not konfirmasi("Kembalikan alat lain / coba lagi?"):
            break


def main():
    sistem = SistemLaboratorium()
    statistik = StatistikPeminjaman(sistem)

    while True:
        judul("LABORATORIUM | KELOMPOK 2")
        ringkasan(sistem, statistik)
        print("  DATA MASTER                     TRANSAKSI")
        print("  [1] Mahasiswa                   [3] Peminjaman baru")
        print("  [2] Peralatan                   [4] Daftar transaksi")
        print("                                  [5] Pengembalian alat")
        garis()
        print("  PEMANTAUAN                      LAPORAN")
        print("  [7] Alat tersedia               [6] Cari transaksi mahasiswa")
        print("  [8] Alat dipinjam              [10] Riwayat mahasiswa")
        print("  [9] Alat rusak                 [11] Statistik peminjaman")
        garis()
        print("  [12] Keluar  |  Data disimpan selama sesi berjalan")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            menu_mahasiswa(sistem)

        elif pilihan == "2":
            menu_alat(sistem)

        elif pilihan == "3":
            buat_transaksi(sistem)

        elif pilihan == "4":
            tampilkan_transaksi(sistem.semua_transaksi())

        elif pilihan == "5":
            proses_pengembalian(sistem)

        elif pilihan == "6":
            nim = input("Masukkan NIM mahasiswa: ").strip()
            tampilkan_transaksi(sistem.cari_transaksi_mahasiswa(nim))

        elif pilihan == "7":
            tampilkan_alat(sistem.alat_tersedia())

        elif pilihan == "8":
            tampilkan_alat(sistem.alat_dipinjam())

        elif pilihan == "9":
            tampilkan_alat(sistem.alat_rusak())

        elif pilihan == "10":
            nim = input("Masukkan NIM mahasiswa: ").strip()
            tampilkan_transaksi(sistem.riwayat_peminjaman(nim))

        elif pilihan == "11":
            statistik.tampilkan_statistik()

        elif pilihan == "12":
            if konfirmasi("Keluar? Data sesi ini tidak disimpan setelah program ditutup."):
                print("Program selesai. Terima kasih.")
                break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()

