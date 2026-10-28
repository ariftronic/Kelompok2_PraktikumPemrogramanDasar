from modules.sistem_lab import SistemLaboratorium
from modules.statistik import StatistikPeminjaman
from tests.test_mahasiswa import cek


def main():
    hasil = []
    sistem = SistemLaboratorium()
    sistem.tambah_mahasiswa("M001", "Andi", "0812")
    for kode in ["A001", "A002", "A003", "A004"]:
        sistem.tambah_alat(kode, "Alat " + kode, "praktikum")

    for hari in [0, 8]:
        berhasil, pesan, trx = sistem.buat_transaksi("M001", ["A001"], hari)
        hasil.append(cek("Durasi " + str(hari) + " hari ditolak",
                         not berhasil and len(sistem.transaksi) == 0
                         and sistem.peralatan["A001"].tersedia))

    berhasil, pesan, pertama = sistem.buat_transaksi("M001", ["A001", "A002"], 1)
    hasil.append(cek("Durasi satu hari diterima", berhasil))
    berhasil, pesan, kedua = sistem.buat_transaksi("M001", ["A003"], 7)
    hasil.append(cek("Transaksi kedua dan durasi tujuh hari diterima", berhasil))
    berhasil, pesan, trx = sistem.buat_transaksi("M001", ["A004"])
    hasil.append(cek("Transaksi ketiga ditolak tanpa mengubah stok",
                     not berhasil and sistem.peralatan["A004"].tersedia
                     and len(sistem.transaksi) == 2))

    berhasil, pesan, trx = sistem.proses_pengembalian(pertama.id_transaksi, "A001", "bagus")
    hasil.append(cek("Kondisi salah ditolak tanpa mengubah data",
                     not berhasil and pertama.status == "dipinjam"
                     and not pertama.daftar_item[0].sudah_dikembalikan
                     and not sistem.peralatan["A001"].tersedia))
    sistem.proses_pengembalian(pertama.id_transaksi, "A001", "baik")
    berhasil, pesan, trx = sistem.buat_transaksi("M001", ["A004"])
    hasil.append(cek("Pengembalian sebagian tetap dihitung aktif", not berhasil))
    sistem.proses_pengembalian(pertama.id_transaksi, "A002", "baik")
    hasil.append(cek("Transaksi selesai mengurangi jumlah aktif",
                     sistem.mahasiswa["M001"].jumlah_transaksi_aktif() == 1))
    berhasil, pesan, ketiga = sistem.buat_transaksi("M001", ["A004"])
    hasil.append(cek("Boleh meminjam lagi setelah satu transaksi selesai", berhasil))
    berhasil, pesan, trx = sistem.proses_pengembalian(pertama.id_transaksi, "A001", "rusak berat")
    hasil.append(cek("Pengembalian ulang ditolak tanpa mengubah kondisi",
                     not berhasil and sistem.peralatan["A001"].kondisi == "baik"))

    berhasil, pesan = sistem.hapus_alat("A001")
    hasil.append(cek("Alat dengan transaksi selesai boleh dihapus", berhasil))
    berhasil, pesan = sistem.tambah_alat("A001", "Laptop Baru", "komputasi")
    hasil.append(cek("Kode dengan riwayat tidak boleh digunakan ulang",
                     not berhasil and "A001" not in sistem.peralatan))
    sistem.proses_pengembalian(kedua.id_transaksi, "A003", "baik")
    sistem.proses_pengembalian(ketiga.id_transaksi, "A004", "baik")
    berhasil, pesan = sistem.hapus_mahasiswa("M001")
    hasil.append(cek("Mahasiswa tanpa transaksi aktif boleh dihapus", berhasil))
    berhasil, pesan = sistem.tambah_mahasiswa("M001", "Budi", "0899")
    hasil.append(cek("NIM dengan riwayat tidak boleh digunakan ulang",
                     not berhasil and "M001" not in sistem.mahasiswa))
    statistik = StatistikPeminjaman(sistem)
    mahasiswa, jumlah = statistik.mahasiswa_teraktif()
    hasil.append(cek("Riwayat dan statistik identitas lama tetap utuh",
                     mahasiswa.nama == "Andi" and jumlah == 3
                     and len(sistem.riwayat_peminjaman("M001")) == 3
                     and statistik.jumlah_transaksi_selesai() == 3
                     and statistik.jumlah_transaksi_aktif() == 0))

    lulus = 0
    for nilai in hasil:
        lulus = lulus + nilai
    print("\nHasil:", lulus, "dari", len(hasil), "pengujian lulus.")


if __name__ == "__main__":
    main()
