from modules.mahasiswa import Mahasiswa


def cek(nama, kondisi):
    if kondisi:
        print("[LULUS]", nama)
        return 1
    else:
        print("[GAGAL]", nama)
        return 0


def main():
    lulus = 0
    total = 0

    mhs = Mahasiswa("K3525001", "Andi", "08123456789")

    total = total + 1
    lulus = lulus + cek("Data awal mahasiswa", mhs.nim == "K3525001" and mhs.nama == "Andi")

    total = total + 1
    lulus = lulus + cek("Awal boleh meminjam", mhs.boleh_meminjam())

    mhs.tambah_transaksi_aktif("TRX001")
    mhs.tambah_transaksi_aktif("TRX002")

    total = total + 1
    lulus = lulus + cek("Maksimal dua transaksi aktif", not mhs.boleh_meminjam())

    total = total + 1
    lulus = lulus + cek("Transaksi ketiga ditolak", not mhs.tambah_transaksi_aktif("TRX003"))

    mhs.hapus_transaksi_aktif("TRX001")

    total = total + 1
    lulus = lulus + cek("Boleh pinjam lagi setelah satu selesai", mhs.boleh_meminjam())

    print("\nHasil:", lulus, "dari", total, "pengujian lulus.")


if __name__ == "__main__":
    main()