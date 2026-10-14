from modules.konstanta import MAKS_HARI_PINJAM
from modules.sistem_lab import SistemLaboratorium
from modules.statistik import StatistikPeminjaman


def garis():
    print("=" * 60)


def tampilkan_mahasiswa(daftar):
    if len(daftar) == 0:
        print("Tidak ada data mahasiswa.")
        return

    print("\nDAFTAR MAHASISWA")
    garis()

    for mhs in daftar:
        mhs.tampilkan_info()
        garis()


def tampilkan_alat(daftar):
    if len(daftar) == 0:
        print("Tidak ada data alat.")
        return

    print("\nDAFTAR PERALATAN")
    garis()

    for alat in daftar:
        alat.tampilkan_info()
        garis()


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
        print("\n===== KELOLA DATA MAHASISWA =====")
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
            print(pesan)

        elif pilihan == "2":
            nim = input("NIM mahasiswa yang diedit: ").strip()

            if nim not in sistem.mahasiswa:
                print("Mahasiswa tidak ditemukan.")
                continue

            print("Kosongkan data jika tidak ingin mengubah nilainya.")
            nama = input("Nama baru              : ")
            no_hp = input("Nomor HP baru          : ")
            berhasil, pesan = sistem.edit_mahasiswa(nim, nama, no_hp)
            print(pesan)

        elif pilihan == "3":
            nim = input("NIM mahasiswa yang dihapus: ")
            berhasil, pesan = sistem.hapus_mahasiswa(nim)
            print(pesan)

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
        print("\n===== KELOLA DATA ALAT =====")
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
            print(pesan)

        elif pilihan == "2":
            kode = input("Kode alat yang diedit: ").strip()

            if kode not in sistem.peralatan:
                print("Peralatan tidak ditemukan.")
                continue

            print("Kosongkan data jika tidak ingin mengubah nilainya.")
            nama = input("Nama alat baru        : ")
            kategori = input("Kategori baru         : ")
            berhasil, pesan = sistem.edit_alat(kode, nama, kategori)
            print(pesan)

        elif pilihan == "3":
            kode = input("Kode alat yang dihapus: ")
            berhasil, pesan = sistem.hapus_alat(kode)
            print(pesan)

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
    print("\n===== BUAT TRANSAKSI PEMINJAMAN =====")
    nim = input("NIM mahasiswa: ").strip()

    if nim not in sistem.mahasiswa:
        print("Mahasiswa tidak ditemukan.")
        return

    if not sistem.mahasiswa[nim].boleh_meminjam():
        print("Mahasiswa sudah mencapai batas transaksi aktif.")
        return

    daftar_kode = []
    print("Masukkan kode alat satu per satu.")
    print("Ketik 'selesai' jika sudah selesai memilih alat.")

    while True:
        kode = input("Kode alat: ").strip()

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

    lama_text = input(
        "Lama peminjaman (1-"
        + str(MAKS_HARI_PINJAM)
        + " hari): "
    ).strip()

    if not lama_text.isdigit():
        print("Lama peminjaman harus berupa angka.")
        return

    lama_hari = int(lama_text)
    berhasil, pesan, trx = sistem.buat_transaksi(
        nim,
        daftar_kode,
        lama_hari,
    )
    print(pesan)

    if berhasil:
        trx.tampilkan_detail()


def proses_pengembalian(sistem):
    print("\n===== PROSES PENGEMBALIAN =====")
    id_transaksi = input("ID transaksi: ").strip()

    if id_transaksi not in sistem.transaksi:
        print("Transaksi tidak ditemukan.")
        return

    trx = sistem.transaksi[id_transaksi]

    while True:
        kode_alat = input("Kode alat      : ").strip()
        print("Kondisi: baik / rusak ringan / rusak berat")
        kondisi = input("Kondisi kembali: ").strip()

        berhasil, pesan, trx = sistem.proses_pengembalian(
            id_transaksi,
            kode_alat,
            kondisi,
        )

        print(pesan)

        if berhasil:
            trx.tampilkan_detail()

        if not trx.aktif():
            break

        lanjut = input(
            "Kembalikan alat lain dari transaksi ini? (y/n): "
        ).strip().lower()

        if lanjut != "y":
            break


def main():
    sistem = SistemLaboratorium()
    statistik = StatistikPeminjaman(sistem)

    while True:
        print("\n")
        garis()
        print(" SISTEM PENGELOLAAN PEMINJAMAN PERALATAN LABORATORIUM")
        garis()
        print("1.  Kelola data mahasiswa")
        print("2.  Kelola data alat")
        print("3.  Buat transaksi peminjaman")
        print("4.  Tampilkan transaksi")
        print("5.  Proses pengembalian alat")
        print("6.  Cari transaksi berdasarkan mahasiswa")
        print("7.  Tampilkan alat yang tersedia")
        print("8.  Tampilkan alat yang sedang dipinjam")
        print("9.  Tampilkan alat yang rusak")
        print("10. Tampilkan riwayat peminjaman mahasiswa")
        print("11. Tampilkan statistik peminjaman")
        print("12. Keluar")

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
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
