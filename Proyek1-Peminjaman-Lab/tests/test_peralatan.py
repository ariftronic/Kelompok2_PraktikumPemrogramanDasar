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

    berhasil, pesan = sistem.tambah_alat(
        "A001",
        "Kamera Digital",
        "multimedia",
    )
    total = total + 1
    lulus = lulus + cek("Tambah alat", berhasil)

    berhasil, pesan = sistem.tambah_alat(
        "A001",
        "Kamera Lain",
        "multimedia",
    )
    total = total + 1
    lulus = lulus + cek("Kode alat duplikat ditolak", not berhasil)

    alat = sistem.peralatan["A001"]
    total = total + 1
    lulus = lulus + cek("Alat baru dapat dipinjam", alat.dapat_dipinjam())

    total = total + 1
    lulus = lulus + cek(
        "Pencarian sebagian nama",
        len(sistem.cari_alat("kamera")) == 1,
    )

    total = total + 1
    lulus = lulus + cek(
        "Pencarian kategori",
        len(sistem.cari_alat("multimedia")) == 1,
    )

    berhasil, pesan = sistem.hapus_alat("A001")
    total = total + 1
    lulus = lulus + cek(
        "Hapus alat tanpa transaksi aktif",
        berhasil and "A001" not in sistem.peralatan,
    )

    print("\nHasil:", lulus, "dari", total, "pengujian lulus.")


if __name__ == "__main__":
    main()
