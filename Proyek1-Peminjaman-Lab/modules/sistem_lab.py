from datetime import date, timedelta

from modules.konstanta import (
    KONDISI_ALAT,
    MAKS_HARI_PINJAM,
    MAKS_TRANSAKSI_AKTIF,
)
from modules.mahasiswa import Mahasiswa
from modules.peralatan import Peralatan
from modules.transaksi import TransaksiPeminjaman


class SistemLaboratorium:
    def __init__(self):
        self.mahasiswa = {}
        self.peralatan = {}
        self.transaksi = {}
        self.urutan_transaksi = 0

    def tambah_mahasiswa(self, nim, nama, no_hp):
        nim = str(nim).strip()
        nama = str(nama).strip()
        no_hp = str(no_hp).strip()

        if nim == "":
            return False, "NIM tidak boleh kosong."

        if nama == "":
            return False, "Nama tidak boleh kosong."

        if nim in self.mahasiswa:
            return False, "NIM sudah terdaftar."

        self.mahasiswa[nim] = Mahasiswa(nim, nama, no_hp)
        return True, "Mahasiswa berhasil ditambahkan."

    def edit_mahasiswa(self, nim, nama, no_hp):
        nim = str(nim).strip()

        if nim not in self.mahasiswa:
            return False, "Mahasiswa tidak ditemukan."

        mhs = self.mahasiswa[nim]
        nama = str(nama).strip()
        no_hp = str(no_hp).strip()

        if nama == "":
            nama = mhs.nama

        if no_hp == "":
            no_hp = mhs.no_hp

        berhasil = mhs.update_data(nama, no_hp)

        if not berhasil:
            return False, "Data mahasiswa tidak valid."

        return True, "Data mahasiswa berhasil diperbarui."

    def hapus_mahasiswa(self, nim):
        nim = str(nim).strip()

        if nim not in self.mahasiswa:
            return False, "Mahasiswa tidak ditemukan."

        if self.mahasiswa[nim].jumlah_transaksi_aktif() > 0:
            return False, "Mahasiswa masih memiliki transaksi aktif dan tidak dapat dihapus."

        del self.mahasiswa[nim]
        return True, "Mahasiswa berhasil dihapus."

    def cari_mahasiswa(self, keyword):
        keyword = str(keyword).strip().lower()
        hasil = []

        for mhs in self.mahasiswa.values():
            if keyword == "":
                hasil.append(mhs)
            elif keyword in mhs.nim.lower() or keyword in mhs.nama.lower():
                hasil.append(mhs)

        return hasil

    def tambah_alat(self, kode_alat, nama_alat, kategori):
        kode_alat = str(kode_alat).strip()
        nama_alat = str(nama_alat).strip()
        kategori = str(kategori).strip()

        if kode_alat == "":
            return False, "Kode alat tidak boleh kosong."

        if nama_alat == "":
            return False, "Nama alat tidak boleh kosong."

        if kategori == "":
            return False, "Kategori alat tidak boleh kosong."

        if kode_alat in self.peralatan:
            return False, "Kode alat sudah terdaftar."

        self.peralatan[kode_alat] = Peralatan(kode_alat, nama_alat, kategori)
        return True, "Peralatan berhasil ditambahkan."

    def edit_alat(self, kode_alat, nama_alat, kategori):
        kode_alat = str(kode_alat).strip()

        if kode_alat not in self.peralatan:
            return False, "Peralatan tidak ditemukan."

        alat = self.peralatan[kode_alat]
        nama_alat = str(nama_alat).strip()
        kategori = str(kategori).strip()

        if nama_alat == "":
            nama_alat = alat.nama_alat

        if kategori == "":
            kategori = alat.kategori

        berhasil = alat.update_data(nama_alat, kategori)

        if not berhasil:
            return False, "Data peralatan tidak valid."

        return True, "Data peralatan berhasil diperbarui."

    def hapus_alat(self, kode_alat):
        kode_alat = str(kode_alat).strip()

        if kode_alat not in self.peralatan:
            return False, "Peralatan tidak ditemukan."

        for trx in self.transaksi.values():
            if trx.aktif():
                for item in trx.daftar_item:
                    if item.alat.kode_alat == kode_alat:
                        return False, "Alat masih tercatat dalam transaksi aktif dan tidak dapat dihapus."

        del self.peralatan[kode_alat]
        return True, "Peralatan berhasil dihapus."

    def cari_alat(self, keyword):
        hasil = []

        for alat in self.peralatan.values():
            if alat.cocok_pencarian(keyword):
                hasil.append(alat)

        return hasil

    def alat_tersedia(self):
        hasil = []

        for alat in self.peralatan.values():
            if alat.tersedia:
                hasil.append(alat)

        return hasil

    def alat_dipinjam(self):
        hasil = []

        for alat in self.peralatan.values():
            if not alat.tersedia and alat.kondisi == "baik":
                hasil.append(alat)

        return hasil

    def alat_rusak(self):
        hasil = []

        for alat in self.peralatan.values():
            if alat.kondisi != "baik":
                hasil.append(alat)

        return hasil

    def buat_transaksi(self, nim, daftar_kode, lama_hari=MAKS_HARI_PINJAM, tanggal_pinjam=None):
        nim = str(nim).strip()

        if tanggal_pinjam is None:
            tanggal_pinjam = date.today()

        if nim not in self.mahasiswa:
            return False, "Mahasiswa tidak ditemukan.", None

        mhs = self.mahasiswa[nim]

        if not mhs.boleh_meminjam():
            return (
                False,
                "Mahasiswa sudah memiliki maksimal "
                + str(MAKS_TRANSAKSI_AKTIF)
                + " transaksi aktif.",
                None,
            )

        if len(daftar_kode) == 0:
            return False, "Transaksi minimal berisi 1 alat.", None

        if lama_hari < 1 or lama_hari > MAKS_HARI_PINJAM:
            return (
                False,
                "Lama peminjaman harus antara 1 sampai "
                + str(MAKS_HARI_PINJAM)
                + " hari.",
                None,
            )

        kode_unik = []
        daftar_alat = []

        for kode in daftar_kode:
            kode = str(kode).strip()

            if kode == "":
                continue

            if kode in kode_unik:
                return False, "Kode alat tidak boleh duplikat dalam satu transaksi.", None

            kode_unik.append(kode)

            if kode not in self.peralatan:
                return False, "Alat " + kode + " tidak ditemukan.", None

            alat = self.peralatan[kode]

            if not alat.dapat_dipinjam():
                return False, "Alat " + kode + " tidak tersedia.", None

            daftar_alat.append(alat)

        if len(daftar_alat) == 0:
            return False, "Tidak ada alat valid yang dipilih.", None

        self.urutan_transaksi = self.urutan_transaksi + 1
        id_transaksi = "TRX" + str(self.urutan_transaksi).zfill(3)
        batas_kembali = tanggal_pinjam + timedelta(days=lama_hari)

        trx = TransaksiPeminjaman(
            id_transaksi,
            mhs,
            daftar_alat,
            tanggal_pinjam,
            batas_kembali,
        )

        for alat in daftar_alat:
            alat.tandai_dipinjam()

        berhasil_tambah = mhs.tambah_transaksi_aktif(id_transaksi)

        if not berhasil_tambah:
            for alat in daftar_alat:
                alat.tersedia = True

            return False, "Transaksi gagal dicatat pada data mahasiswa.", None

        self.transaksi[id_transaksi] = trx

        return True, "Transaksi berhasil dibuat dengan ID " + id_transaksi + ".", trx

    def proses_pengembalian(self, id_transaksi, kode_alat, kondisi, tanggal_kembali=None):
        id_transaksi = str(id_transaksi).strip()
        kode_alat = str(kode_alat).strip()
        kondisi = str(kondisi).strip().lower()

        if tanggal_kembali is None:
            tanggal_kembali = date.today()

        if id_transaksi not in self.transaksi:
            return False, "Transaksi tidak ditemukan.", None

        if kondisi not in KONDISI_ALAT:
            return False, "Kondisi harus: baik, rusak ringan, atau rusak berat.", None

        trx = self.transaksi[id_transaksi]

        berhasil, pesan, item = trx.kembalikan_alat(
            kode_alat,
            kondisi,
            tanggal_kembali,
        )

        if not berhasil:
            return False, pesan, trx

        item.alat.proses_pengembalian(kondisi)

        if trx.seluruh_alat_kembali():
            trx.mahasiswa.hapus_transaksi_aktif(id_transaksi)

        hari_terlambat = item.jumlah_hari_terlambat(trx.batas_kembali)

        pesan_hasil = "Pengembalian berhasil. Status transaksi: " + trx.status + "."

        if hari_terlambat > 0:
            pesan_hasil = (
                pesan_hasil
                + " TERLAMBAT "
                + str(hari_terlambat)
                + " hari."
            )

        return True, pesan_hasil, trx

    def semua_transaksi(self):
        hasil = []

        for trx in self.transaksi.values():
            hasil.append(trx)

        return hasil

    def cari_transaksi_mahasiswa(self, nim):
        nim = str(nim).strip()
        hasil = []

        for trx in self.transaksi.values():
            if trx.mahasiswa.nim == nim:
                hasil.append(trx)

        return hasil

    def riwayat_peminjaman(self, nim):
        return self.cari_transaksi_mahasiswa(nim)
