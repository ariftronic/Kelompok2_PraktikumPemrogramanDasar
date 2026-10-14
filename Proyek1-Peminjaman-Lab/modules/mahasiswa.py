from modules.konstanta import MAKS_TRANSAKSI_AKTIF


class Mahasiswa:
    def __init__(self, nim, nama, no_hp):
        self.nim = str(nim).strip()
        self.nama = str(nama).strip()
        self.no_hp = str(no_hp).strip()
        self.transaksi_aktif = []
        self.aktif = True

    def update_data(self, nama, no_hp):
        nama = str(nama).strip()
        no_hp = str(no_hp).strip()

        if nama == "":
            return False

        self.nama = nama
        self.no_hp = no_hp
        return True

    def jumlah_transaksi_aktif(self):
        return len(self.transaksi_aktif)

    def boleh_meminjam(self):
        if self.aktif and self.jumlah_transaksi_aktif() < MAKS_TRANSAKSI_AKTIF:
            return True
        else:
            return False

    def tambah_transaksi_aktif(self, id_transaksi):
        id_transaksi = str(id_transaksi).strip()

        if id_transaksi == "":
            return False

        if id_transaksi in self.transaksi_aktif:
            return False

        if not self.boleh_meminjam():
            return False

        self.transaksi_aktif.append(id_transaksi)
        return True

    def hapus_transaksi_aktif(self, id_transaksi):
        id_transaksi = str(id_transaksi).strip()

        if id_transaksi not in self.transaksi_aktif:
            return False

        self.transaksi_aktif.remove(id_transaksi)
        return True

    def status_aktif_peminjaman(self):
        if self.jumlah_transaksi_aktif() > 0:
            return True
        else:
            return False

    def nonaktifkan(self):
        if self.jumlah_transaksi_aktif() > 0:
            return False

        self.aktif = False
        return True

    def tampilkan_info(self):
        print(f"NIM             : {self.nim}")
        print(f"Nama            : {self.nama}")
        print(f"Nomor HP        : {self.no_hp}")
        print(f"Transaksi aktif : {self.jumlah_transaksi_aktif()}")

        if self.status_aktif_peminjaman():
            print("Status pinjaman : Aktif")
        else:
            print("Status pinjaman : Tidak aktif")
