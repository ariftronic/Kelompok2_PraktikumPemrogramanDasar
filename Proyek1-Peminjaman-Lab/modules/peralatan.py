KONDISI_ALAT = ("baik", "rusak ringan", "rusak berat")


class Peralatan:
    def __init__(self, kode_alat, nama_alat, kategori):
        self.kode_alat = str(kode_alat).strip()
        self.nama_alat = str(nama_alat).strip()
        self.kategori = str(kategori).strip()
        self.kondisi = "baik"
        self.tersedia = True

    def update_data(self, nama_alat, kategori):
        nama_alat = str(nama_alat).strip()
        kategori = str(kategori).strip()

        if nama_alat == "":
            return False

        self.nama_alat = nama_alat
        self.kategori = kategori
        return True

    def dapat_dipinjam(self):
        if self.tersedia and self.kondisi == "baik":
            return True
        else:
            return False

    def tandai_dipinjam(self):
        if not self.dapat_dipinjam():
            return False

        self.tersedia = False
        return True

    def proses_pengembalian(self, kondisi):
        kondisi = str(kondisi).strip().lower()

        if kondisi not in KONDISI_ALAT:
            return False

        self.kondisi = kondisi

        if kondisi == "baik":
            self.tersedia = True
        else:
            self.tersedia = False

        return True

    def cocok_pencarian(self, keyword):
        keyword = str(keyword).strip().lower()

        if keyword == "":
            return True

        if keyword == self.kode_alat.lower():
            return True

        if keyword in self.nama_alat.lower():
            return True

        if keyword in self.kategori.lower():
            return True

        return False

    def tampilkan_info(self):
        print("Kode      :", self.kode_alat)
        print("Nama      :", self.nama_alat)
        print("Kategori  :", self.kategori)
        print("Kondisi   :", self.kondisi)

        if self.tersedia:
            print("Status    : Tersedia")
        else:
            print("Status    : Tidak tersedia")
