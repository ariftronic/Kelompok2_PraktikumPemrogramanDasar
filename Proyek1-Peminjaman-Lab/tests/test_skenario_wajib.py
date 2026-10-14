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

    sistem.tambah_mahasiswa("M001", "Andi", "0811")
    sistem.tambah_mahasiswa("M002", "Budi", "0822")
    sistem.tambah_alat("A001", "Kamera Digital", "multimedia")
    sistem.tambah_alat("A002", "Tripod", "multimedia")
    sistem.tambah_alat("A003", "Kabel LAN", "jaringan")

    total = total + 1
    lulus = lulus + cek("Skenario 1 - tambah mahasiswa dan alat", len(sistem.mahasiswa) == 2 and len(sistem.peralatan) == 3)

    berhasil, pesan, trx = sistem.buat_transaksi("M001", ["A001", "A002"], 7)
    total = total + 1
    lulus = lulus + cek("Skenario 2 - pinjam beberapa alat", berhasil and not sistem.peralatan["A001"].tersedia and not sistem.peralatan["A002"].tersedia)

    berhasil2, pesan2, trx2 = sistem.buat_transaksi("M002", ["A001"], 7)
    total = total + 1
    lulus = lulus + cek("Skenario 3 - alat tidak tersedia ditolak", not berhasil2)

    berhasil3, pesan3, trx3 = sistem.proses_pengembalian(trx.id_transaksi, "A001", "baik")
    total = total + 1
    lulus = lulus + cek("Skenario 4 - pengembalian sebagian", berhasil3 and trx3.status == "sebagian dikembalikan" and sistem.peralatan["A001"].tersedia and not sistem.peralatan["A002"].tersedia)

    berhasil4, pesan4, trx4 = sistem.proses_pengembalian(trx.id_transaksi, "A002", "rusak ringan")
    total = total + 1
    lulus = lulus + cek("Skenario 5 - alat rusak tidak tersedia", berhasil4 and not sistem.peralatan["A002"].tersedia and sistem.peralatan["A002"].kondisi == "rusak ringan")

    berhasil5, pesan5, trx5 = sistem.buat_transaksi("M001", ["A003"], 3)
    hapus, pesan_hapus = sistem.hapus_mahasiswa("M001")
    total = total + 1
    lulus = lulus + cek("Skenario 6 - mahasiswa aktif tidak boleh dihapus", berhasil5 and not hapus)

    print("\nTOTAL:", lulus, "dari", total, "skenario wajib lulus.")


if __name__ == "__main__":
    main()