from datetime import date, timedelta

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

    tanggal = date.today()
    berhasil, pesan, trx = sistem.buat_transaksi(
        "M001",
        ["A001", "A002"],
        7,
        tanggal,
    )

    total = total + 1
    lulus = lulus + cek("Transaksi beberapa alat berhasil", berhasil)

    total = total + 1
    lulus = lulus + cek(
        "Dua item tersimpan dalam transaksi",
        len(trx.daftar_item) == 2,
    )

    total = total + 1
    lulus = lulus + cek(
        "Status awal dipinjam",
        trx.status == "dipinjam",
    )

    berhasil2, pesan2, trx2 = sistem.buat_transaksi(
        "M001",
        ["A001"],
        7,
        tanggal,
    )
    total = total + 1
    lulus = lulus + cek(
        "Alat tidak tersedia ditolak",
        not berhasil2,
    )

    berhasil3, pesan3, trx3 = sistem.buat_transaksi(
        "M001",
        ["A002", "A002"],
        7,
        tanggal,
    )
    total = total + 1
    lulus = lulus + cek(
        "Kode alat duplikat ditolak",
        not berhasil3,
    )

    item = trx.daftar_item[0]
    item.sudah_dikembalikan = True
    item.tanggal_kembali = tanggal + timedelta(days=9)
    total = total + 1
    lulus = lulus + cek(
        "Keterlambatan terdokumentasi",
        item.jumlah_hari_terlambat(trx.batas_kembali) == 2,
    )

    print("\nHasil:", lulus, "dari", total, "pengujian lulus.")


if __name__ == "__main__":
    main()
