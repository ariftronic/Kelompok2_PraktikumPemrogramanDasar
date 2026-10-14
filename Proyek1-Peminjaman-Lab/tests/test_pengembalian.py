from modules.sistem_lab import SistemLaboratorium


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
    sistem = SistemLaboratorium()

    sistem.tambah_mahasiswa("K3525001", "Andi", "0812")
    sistem.tambah_alat("A001", "Kamera", "multimedia")
    sistem.tambah_alat("A002", "Tripod", "multimedia")

    berhasil, pesan, trx = sistem.buat_transaksi("K3525001", ["A001", "A002"], 7)
    total = total + 1
    lulus = lulus + cek("Transaksi berhasil dibuat", berhasil)

    berhasil, pesan, trx = sistem.proses_pengembalian(trx.id_transaksi, "A001", "baik")
    total = total + 1
    lulus = lulus + cek("Pengembalian sebagian", berhasil and trx.status == "sebagian dikembalikan")

    total = total + 1
    lulus = lulus + cek("Alat baik kembali tersedia", sistem.peralatan["A001"].tersedia)

    berhasil, pesan, trx = sistem.proses_pengembalian(trx.id_transaksi, "A002", "rusak berat")
    total = total + 1
    lulus = lulus + cek("Transaksi selesai", berhasil and trx.status == "selesai")

    total = total + 1
    lulus = lulus + cek("Alat rusak berat tidak tersedia", not sistem.peralatan["A002"].tersedia)

    total = total + 1
    lulus = lulus + cek("Transaksi aktif mahasiswa kembali nol", sistem.mahasiswa["K3525001"].jumlah_transaksi_aktif() == 0)

    print("\nHasil:", lulus, "dari", total, "pengujian lulus.")


if __name__ == "__main__":
    main()