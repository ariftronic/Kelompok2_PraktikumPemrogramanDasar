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

    sistem.tambah_mahasiswa("M001", "Andi", "0812")
    sistem.tambah_alat("A001", "Kamera", "multimedia")
    sistem.tambah_alat("A002", "Tripod", "multimedia")

    berhasil, pesan, trx = sistem.buat_transaksi(
        "M001",
        ["A001", "A002"],
        7,
    )

    berhasil1, pesan1, trx1 = sistem.proses_pengembalian(
        trx.id_transaksi,
        "A001",
        "baik",
    )
    total = total + 1
    lulus = lulus + cek(
        "Pengembalian sebagian berhasil",
        berhasil1 and trx1.status == "sebagian dikembalikan",
    )

    total = total + 1
    lulus = lulus + cek(
        "Alat baik kembali tersedia",
        sistem.peralatan["A001"].tersedia,
    )

    hapus, pesan_hapus = sistem.hapus_alat("A001")
    total = total + 1
    lulus = lulus + cek(
        "Alat dalam transaksi aktif belum boleh dihapus",
        not hapus,
    )

    berhasil2, pesan2, trx2 = sistem.proses_pengembalian(
        trx.id_transaksi,
        "A002",
        "rusak berat",
    )
    total = total + 1
    lulus = lulus + cek(
        "Transaksi selesai setelah seluruh alat kembali",
        berhasil2 and trx2.status == "selesai",
    )

    total = total + 1
    lulus = lulus + cek(
        "Alat rusak berat tidak tersedia",
        not sistem.peralatan["A002"].tersedia,
    )

    hapus2, pesan_hapus2 = sistem.hapus_alat("A001")
    total = total + 1
    lulus = lulus + cek(
        "Alat boleh dihapus setelah transaksi selesai",
        hapus2 and "A001" not in sistem.peralatan,
    )

    print("\nHasil:", lulus, "dari", total, "pengujian lulus.")


if __name__ == "__main__":
    main()
