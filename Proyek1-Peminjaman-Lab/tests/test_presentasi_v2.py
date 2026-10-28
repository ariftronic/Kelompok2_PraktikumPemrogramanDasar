from modules.sistem_lab import SistemLaboratorium
from modules.mahasiswa import Mahasiswa
from tests.test_mahasiswa import cek


def main():
    hasil = []
    sistem = SistemLaboratorium()
    berhasil, pesan = sistem.tambah_mahasiswa("M1", "Andi", "   ")
    hasil.append(cek("Nomor HP kosong ditolak", not berhasil and len(sistem.mahasiswa) == 0))
    mhs = Mahasiswa("M1", "Andi", "0812")
    hasil.append(cek("Update langsung menolak HP kosong",
                     not mhs.update_data("Budi", "") and mhs.nama == "Andi"))
    for kode in ["selesai", "SELESAI", " selesai ", "batal", "BaTaL"]:
        berhasil, pesan = sistem.tambah_alat(kode, "Kamera", "media")
        hasil.append(cek("Kode perintah " + kode + " ditolak", not berhasil))

    sistem.tambah_mahasiswa("M1", "Andi", "0812")
    sistem.tambah_alat("A1", "Kamera", "media")
    berhasil, pesan, trx = sistem.buat_transaksi("M1", ["A1"])
    sistem.edit_mahasiswa("M1", "Andi Baru", "0899")
    sistem.edit_alat("A1", "Kamera Baru", "multimedia")
    hasil.append(cek("Nama peminjam saat transaksi tetap",
                     trx.nama_mahasiswa_saat_pinjam == "Andi"
                     and sistem.mahasiswa["M1"].nama == "Andi Baru"))
    item = trx.daftar_item[0]
    hasil.append(cek("Nama dan kategori saat transaksi tetap",
                     item.nama_alat_saat_pinjam == "Kamera"
                     and item.kategori_saat_pinjam == "media"
                     and sistem.peralatan["A1"].nama_alat == "Kamera Baru"))
    berhasil, pesan, trx = sistem.proses_pengembalian(trx.id_transaksi, "A1", "baik")
    hasil.append(cek("Pengembalian tetap memperbarui objek alat asli",
                     berhasil and sistem.peralatan["A1"].tersedia
                     and sistem.mahasiswa["M1"].jumlah_transaksi_aktif() == 0))
    sistem.edit_mahasiswa("M1", "", "")
    hasil.append(cek("Edit kosong mempertahankan data mahasiswa",
                     sistem.mahasiswa["M1"].nama == "Andi Baru"
                     and sistem.mahasiswa["M1"].no_hp == "0899"))
    berhasil, pesan, baru = sistem.buat_transaksi("M1", ["A1"])
    hasil.append(cek("Transaksi baru menyimpan nama terbaru",
                     berhasil and baru.nama_mahasiswa_saat_pinjam == "Andi Baru"
                     and baru.daftar_item[0].nama_alat_saat_pinjam == "Kamera Baru"))

    lulus = 0
    for nilai in hasil:
        lulus = lulus + nilai
    print("\nHasil:", lulus, "dari", len(hasil), "pengujian lulus.")


if __name__ == "__main__":
    main()
