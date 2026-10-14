class Mahasiswa:
    def __init__(self, nim, nama, no_hp):
        self.nim = nim.strip()
        self.nama = nama.strip()
        self.no_hp = no_hp.strip()
        self.transaksi_aktif = []

    def update_data(self, nama, no_hp):
        nama = nama.strip()
        no_hp = no_hp.strip()
        if nama == "" or no_hp == "":
            return False
        self.nama = nama
        self.no_hp = no_hp
        return True

    def jumlah_transaksi_aktif(self):
        return len(self.transaksi_aktif)

    def boleh_meminjam(self):
        if self.jumlah_transaksi_aktif() < 2:
            return True
        else:
            return False

    def tambah_transaksi_aktif(self, id_transaksi):
        if id_transaksi in self.transaksi_aktif:
            return False
        if not self.boleh_meminjam():
            return False
        self.transaksi_aktif.append(id_transaksi)
        return True

    def hapus_transaksi_aktif(self, id_transaksi):
        if id_transaksi not in self.transaksi_aktif:
            return False
        self.transaksi_aktif.remove(id_transaksi)
        return True

    def tampilkan_info(self):
        print("NIM                 :", self.nim)
        print("Nama                :", self.nama)
        print("Nomor HP            :", self.no_hp)
        print("Jumlah transaksi    :", self.jumlah_transaksi_aktif())
        if self.jumlah_transaksi_aktif() > 0:
            print("Status peminjaman   : Aktif")
        else:
            print("Status peminjaman   : Tidak aktif")