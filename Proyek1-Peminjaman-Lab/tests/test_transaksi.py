from datetime import date, timedelta

from modules.mahasiswa import Mahasiswa
from modules.peralatan import Peralatan
from modules.transaksi import TransaksiPeminjaman


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

    mhs = Mahasiswa("K3525001", "Andi", "0812")
    alat1 = Peralatan("A001", "Kamera", "multimedia")
    alat2 = Peralatan("A002", "Tripod", "multimedia")
    tanggal = date.today()

    trx = TransaksiPeminjaman(
        "TRX001",
        mhs,
        [alat1, alat2],
        tanggal,
        tanggal + timedelta(days=7)
    )

    total = total + 1
    lulus = lulus + cek("Transaksi berisi dua alat", len(trx.daftar_item) == 2)

    total = total + 1
    lulus = lulus + cek("Status awal dipinjam", trx.status == "dipinjam")

    berhasil, pesan, item = trx.kembalikan_alat("A001", "baik", tanggal)
    total = total + 1
    lulus = lulus + cek("Pengembalian satu alat berhasil", berhasil)

    total = total + 1
    lulus = lulus + cek("Status menjadi sebagian dikembalikan", trx.status == "sebagian dikembalikan")

    berhasil, pesan, item = trx.kembalikan_alat("A002", "baik", tanggal)
    total = total + 1
    lulus = lulus + cek("Status selesai setelah semua alat kembali", trx.status == "selesai")

    print("\nHasil:", lulus, "dari", total, "pengujian lulus.")


if __name__ == "__main__":
    main()