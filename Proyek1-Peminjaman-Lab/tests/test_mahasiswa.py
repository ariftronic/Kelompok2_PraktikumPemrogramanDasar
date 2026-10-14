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

    berhasil, pesan = sistem.tambah_mahasiswa(
        "K3525001",
        "Andi",
        "08123456789",
    )
    total = total + 1
    lulus = lulus + cek("Tambah mahasiswa", berhasil)

    berhasil, pesan = sistem.tambah_mahasiswa(
        "K3525001",
        "Andi Dua",
        "0812",
    )
    total = total + 1
    lulus = lulus + cek("NIM duplikat ditolak", not berhasil)

    berhasil, pesan = sistem.edit_mahasiswa(
        "K3525001",
        "Andi Saputra",
        "089999999",
    )
    total = total + 1
    lulus = lulus + cek(
        "Edit mahasiswa",
        berhasil and sistem.mahasiswa["K3525001"].nama == "Andi Saputra",
    )

    hasil = sistem.cari_mahasiswa("saputra")
    total = total + 1
    lulus = lulus + cek(
        "Cari mahasiswa berdasarkan nama",
        len(hasil) == 1,
    )

    berhasil, pesan = sistem.hapus_mahasiswa("K3525001")
    total = total + 1
    lulus = lulus + cek(
        "Hapus mahasiswa tanpa transaksi aktif",
        berhasil and "K3525001" not in sistem.mahasiswa,
    )

    print("\nHasil:", lulus, "dari", total, "pengujian lulus.")


if __name__ == "__main__":
    main()
