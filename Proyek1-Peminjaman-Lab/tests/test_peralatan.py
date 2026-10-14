from modules.peralatan import Peralatan


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

    alat = Peralatan("A001", "Kamera Digital", "multimedia")

    total = total + 1
    lulus = lulus + cek("Alat baru tersedia", alat.dapat_dipinjam())

    alat.tandai_dipinjam()
    total = total + 1
    lulus = lulus + cek("Alat menjadi tidak tersedia saat dipinjam", not alat.tersedia)

    alat.proses_pengembalian("baik")
    total = total + 1
    lulus = lulus + cek("Alat kondisi baik tersedia lagi", alat.tersedia and alat.kondisi == "baik")

    alat.tandai_dipinjam()
    alat.proses_pengembalian("rusak ringan")
    total = total + 1
    lulus = lulus + cek("Rusak ringan tidak tersedia", not alat.tersedia and alat.kondisi == "rusak ringan")

    total = total + 1
    lulus = lulus + cek("Pencarian sebagian nama", alat.cocok_pencarian("kamera"))

    total = total + 1
    lulus = lulus + cek("Pencarian kategori", alat.cocok_pencarian("multimedia"))

    print("\nHasil:", lulus, "dari", total, "pengujian lulus.")


if __name__ == "__main__":
    main()