class StatistikPeminjaman:
    def __init__(self, sistem):
        self.sistem = sistem

    def alat_terpopuler(self):
        jumlah = {}
        objek = {}

        for trx in self.sistem.transaksi.values():
            for item in trx.daftar_item:
                kode = item.alat.kode_alat

                if kode in jumlah:
                    jumlah[kode] = jumlah[kode] + 1
                else:
                    jumlah[kode] = 1
                    objek[kode] = item.alat

        kode_terpilih = None
        nilai_terbesar = 0

        for kode in jumlah:
            if jumlah[kode] > nilai_terbesar:
                nilai_terbesar = jumlah[kode]
                kode_terpilih = kode

        if kode_terpilih is None:
            return None, 0

        return objek[kode_terpilih], nilai_terbesar

    def mahasiswa_teraktif(self):
        jumlah = {}
        objek = {}

        for trx in self.sistem.transaksi.values():
            nim = trx.mahasiswa.nim

            if nim in jumlah:
                jumlah[nim] = jumlah[nim] + 1
            else:
                jumlah[nim] = 1
                objek[nim] = trx.mahasiswa

        nim_terpilih = None
        nilai_terbesar = 0

        for nim in jumlah:
            if jumlah[nim] > nilai_terbesar:
                nilai_terbesar = jumlah[nim]
                nim_terpilih = nim

        if nim_terpilih is None:
            return None, 0

        return objek[nim_terpilih], nilai_terbesar

    def jumlah_transaksi_selesai(self):
        jumlah = 0

        for trx in self.sistem.transaksi.values():
            if trx.status == "selesai":
                jumlah = jumlah + 1

        return jumlah

    def jumlah_transaksi_aktif(self):
        jumlah = 0

        for trx in self.sistem.transaksi.values():
            if trx.status == "dipinjam" or trx.status == "sebagian dikembalikan":
                jumlah = jumlah + 1

        return jumlah

    def tampilkan_statistik(self):
        alat, jumlah_alat = self.alat_terpopuler()
        mahasiswa, jumlah_mahasiswa = self.mahasiswa_teraktif()

        print("\n===== STATISTIK PEMINJAMAN =====")

        if alat is None:
            print("Alat paling sering dipinjam      : Belum ada data")
        else:
            print(
                "Alat paling sering dipinjam      :",
                alat.nama_alat,
                "(", jumlah_alat, "kali )"
            )

        if mahasiswa is None:
            print("Mahasiswa paling sering meminjam : Belum ada data")
        else:
            print(
                "Mahasiswa paling sering meminjam :",
                mahasiswa.nama,
                "(", jumlah_mahasiswa, "transaksi )"
            )

        print("Jumlah transaksi selesai         :", self.jumlah_transaksi_selesai())
        print("Jumlah transaksi aktif           :", self.jumlah_transaksi_aktif())
