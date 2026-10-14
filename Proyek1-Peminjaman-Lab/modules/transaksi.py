from datetime import timedelta

STATUS_DIPINJAM = "dipinjam"
STATUS_SEBAGIAN = "sebagian dikembalikan"
STATUS_SELESAI = "selesai"
MAKS_HARI_PINJAM = 7


class ItemPeminjaman:
    def __init__(self, alat):
        self.alat = alat
        self.sudah_dikembalikan = False
        self.tanggal_kembali = None
        self.kondisi_kembali = None

    def masih_dipinjam(self):
        if self.sudah_dikembalikan:
            return False
        else:
            return True

    def kembalikan(self, kondisi, tanggal):
        if self.sudah_dikembalikan:
            return False, "Alat sudah dikembalikan sebelumnya."

        kondisi = str(kondisi).strip().lower()
        if kondisi not in ("baik", "rusak ringan", "rusak berat"):
            return False, "Kondisi alat tidak valid."

        self.sudah_dikembalikan = True
        self.tanggal_kembali = tanggal
        self.kondisi_kembali = kondisi
        return True, "Pengembalian item berhasil."


class TransaksiPeminjaman:
    def __init__(self, id_transaksi, mahasiswa, daftar_alat, tanggal_pinjam, batas_kembali=None):
        self.id_transaksi = str(id_transaksi).strip()
        self.mahasiswa = mahasiswa
        self.daftar_item = []
        self.tanggal_pinjam = tanggal_pinjam

        if batas_kembali is None:
            self.batas_kembali = tanggal_pinjam + timedelta(days=MAKS_HARI_PINJAM)
        else:
            self.batas_kembali = batas_kembali

        self.status = STATUS_DIPINJAM

        for alat in daftar_alat:
            self.tambah_item(alat)

    def tambah_item(self, alat):
        for item in self.daftar_item:
            if item.alat.kode_alat == alat.kode_alat:
                return False

        self.daftar_item.append(ItemPeminjaman(alat))
        self.update_status()
        return True

    def cari_item(self, kode_alat):
        kode_alat = str(kode_alat).strip()

        for item in self.daftar_item:
            if item.alat.kode_alat == kode_alat:
                return item

        return None

    def hitung_item_belum_kembali(self):
        jumlah = 0

        for item in self.daftar_item:
            if item.masih_dipinjam():
                jumlah = jumlah + 1

        return jumlah

    def seluruh_alat_kembali(self):
        if len(self.daftar_item) == 0:
            return False

        if self.hitung_item_belum_kembali() == 0:
            return True
        else:
            return False

    def update_status(self):
        total = len(self.daftar_item)
        belum = self.hitung_item_belum_kembali()

        if total == 0:
            self.status = STATUS_DIPINJAM
        elif belum == total:
            self.status = STATUS_DIPINJAM
        elif belum == 0:
            self.status = STATUS_SELESAI
        else:
            self.status = STATUS_SEBAGIAN

        return self.status

    def aktif(self):
        if self.status == STATUS_SELESAI:
            return False
        else:
            return True

    def kembalikan_alat(self, kode_alat, kondisi, tanggal):
        if tanggal < self.tanggal_pinjam:
            return False, "Tanggal pengembalian tidak boleh sebelum tanggal peminjaman.", None

        item = self.cari_item(kode_alat)
        if item is None:
            return False, "Alat tidak ada pada transaksi ini.", None

        berhasil, pesan = item.kembalikan(kondisi, tanggal)
        if not berhasil:
            return False, pesan, item

        self.update_status()
        return True, "Alat berhasil dikembalikan.", item

    def tampilkan_detail(self):
        print("ID Transaksi   :", self.id_transaksi)
        print("Mahasiswa      :", self.mahasiswa.nama, "(", self.mahasiswa.nim, ")")
        print("Tanggal pinjam :", self.tanggal_pinjam)
        print("Batas kembali  :", self.batas_kembali)
        print("Status          :", self.status)
        print("Daftar alat:")

        nomor = 1
        for item in self.daftar_item:
            if item.sudah_dikembalikan:
                status_item = "Sudah kembali - " + str(item.kondisi_kembali)
            else:
                status_item = "Masih dipinjam"

            print(
                " ", nomor, ".",
                item.alat.kode_alat, "-", item.alat.nama_alat,
                "|", status_item
            )
            nomor = nomor + 1
