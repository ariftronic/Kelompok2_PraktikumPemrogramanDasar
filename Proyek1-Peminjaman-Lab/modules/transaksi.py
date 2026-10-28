from datetime import date

from modules.konstanta import (
    KONDISI_ALAT,
    STATUS_DIPINJAM,
    STATUS_SEBAGIAN,
    STATUS_SELESAI,
)


class ItemPeminjaman:
    def __init__(self, alat):
        self.alat = alat
        self.nama_alat_saat_pinjam = alat.nama_alat
        self.kategori_saat_pinjam = alat.kategori
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

        if kondisi not in KONDISI_ALAT:
            return False, "Kondisi alat tidak valid."

        self.sudah_dikembalikan = True
        self.tanggal_kembali = tanggal
        self.kondisi_kembali = kondisi
        return True, "Pengembalian item berhasil."

    def jumlah_hari_terlambat(self, batas_kembali, tanggal_acuan=None):
        if self.sudah_dikembalikan:
            tanggal_dibandingkan = self.tanggal_kembali
        else:
            if tanggal_acuan is None:
                tanggal_dibandingkan = date.today()
            else:
                tanggal_dibandingkan = tanggal_acuan

        if tanggal_dibandingkan <= batas_kembali:
            return 0

        selisih = tanggal_dibandingkan - batas_kembali
        return selisih.days


class TransaksiPeminjaman:
    def __init__(self, id_transaksi, mahasiswa, daftar_alat, tanggal_pinjam, batas_kembali):
        self.id_transaksi = str(id_transaksi).strip()
        self.mahasiswa = mahasiswa
        self.nama_mahasiswa_saat_pinjam = mahasiswa.nama
        self.daftar_item = []
        self.tanggal_pinjam = tanggal_pinjam
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
        print(f"ID Transaksi   : {self.id_transaksi}")
        print(f"Mahasiswa      : {self.nama_mahasiswa_saat_pinjam} ({self.mahasiswa.nim})")
        print(f"Tanggal pinjam : {self.tanggal_pinjam}")
        print(f"Batas kembali  : {self.batas_kembali}")
        print(f"Status         : {self.status}")
        print("Daftar alat:")

        nomor = 1

        for item in self.daftar_item:
            if item.sudah_dikembalikan:
                status_item = (
                    f"Sudah kembali {item.tanggal_kembali} - "
                    f"{item.kondisi_kembali}"
                )
            else:
                status_item = "Masih dipinjam"

            hari_terlambat = item.jumlah_hari_terlambat(self.batas_kembali)

            if hari_terlambat > 0:
                status_item = status_item + f" | TERLAMBAT {hari_terlambat} hari"

            print(
                f"  {nomor}. {item.alat.kode_alat} - "
                f"{item.nama_alat_saat_pinjam} | {status_item}"
            )
            nomor = nomor + 1

