from datetime import date, timedelta
from typing import Dict, List, Optional

from modules.mahasiswa import Mahasiswa
from modules.peralatan import Peralatan
from modules.transaksi import TransaksiPeminjaman

KONDISI_VALID = ("baik", "rusak ringan", "rusak berat")
STATUS_AKTIF = ("dipinjam", "sebagian dikembalikan")
MAKS_HARI_PINJAM = 7

def _cocok(keyword: str, *teks: str) -> bool:
    k = keyword.strip().lower()
    return any(k in t.lower() for t in teks)

class SistemLaboratorium:
    def __init__(self):
        self.mahasiswa: Dict[str, Mahasiswa] = {}
        self.peralatan: Dict[str, Peralatan] = {}
        self.transaksi: Dict[str, TransaksiPeminjaman] = {}
        self._urutan_transaksi = 0

    def tambah_mahasiswa(self, data: dict) -> bool:
        """data: {"nim", "nama", "no_hp"}. Gagal -> ValueError."""
        nim = str(data.get("nim", "")).strip()
        nama = str(data.get("nama", "")).strip()
        if not nim:
            raise ValueError("NIM tidak boleh kosong.")
        if not nama:
            raise ValueError("Nama tidak boleh kosong.")
        if nim in self.mahasiswa:
            raise ValueError(f"NIM {nim} sudah terdaftar.")
        self.mahasiswa[nim] = Mahasiswa(nim, nama, str(data.get("no_hp", "")).strip())
        return True

    def edit_mahasiswa(self, nim: str, data: dict) -> bool:
        """data boleh berisi "nama" dan/atau "no_hp"; yang tidak diisi tidak berubah."""
        mhs = self.mahasiswa.get(nim)
        if mhs is None:
            raise ValueError(f"Mahasiswa {nim} tidak ditemukan.")
        nama = str(data.get("nama", mhs.nama)).strip()
        if not nama:
            raise ValueError("Nama tidak boleh kosong.")
        mhs.update_data(nama, str(data.get("no_hp", mhs.no_hp)).strip())
        return True

    def hapus_mahasiswa(self, nim: str) -> bool:
        if nim not in self.mahasiswa:
            raise ValueError(f"Mahasiswa {nim} tidak ditemukan.")
        if self.cari_transaksi_mahasiswa(nim):
            raise ValueError("Mahasiswa masih memiliki transaksi aktif; tidak dapat dihapus.")
        del self.mahasiswa[nim]
        return True

    def cari_mahasiswa(self, keyword: str) -> List[Mahasiswa]:
        """Cocokkan NIM atau sebagian nama (tanpa peka huruf besar/kecil). Kosong = semua."""
        return [m for m in self.mahasiswa.values() if _cocok(keyword, m.nim, m.nama)]

    def tambah_alat(self, data: dict) -> bool:
        """data: {"kode_alat", "nama_alat", "kategori"}. Gagal -> ValueError."""
        kode = str(data.get("kode_alat", "")).strip()
        nama = str(data.get("nama_alat", "")).strip()
        if not kode:
            raise ValueError("Kode alat tidak boleh kosong.")
        if not nama:
            raise ValueError("Nama alat tidak boleh kosong.")
        if kode in self.peralatan:
            raise ValueError(f"Kode alat {kode} sudah terdaftar.")
        self.peralatan[kode] = Peralatan(kode, nama, str(data.get("kategori", "")).strip())
        return True

    def edit_alat(self, kode: str, data: dict) -> bool:
        """data boleh berisi "nama_alat" dan/atau "kategori"."""
        alat = self.peralatan.get(kode)
        if alat is None:
            raise ValueError(f"Alat {kode} tidak ditemukan.")
        nama = str(data.get("nama_alat", alat.nama_alat)).strip()
        if not nama:
            raise ValueError("Nama alat tidak boleh kosong.")
        alat.update_data(nama, str(data.get("kategori", alat.kategori)).strip())
        return True

    def hapus_alat(self, kode: str) -> bool:
        if kode not in self.peralatan:
            raise ValueError(f"Alat {kode} tidak ditemukan.")
        for trx in self.transaksi.values():
            if trx.status in STATUS_AKTIF and any(
                i.alat.kode_alat == kode for i in trx.daftar_item
            ):
                raise ValueError(
                    f"Alat masih tercatat pada transaksi aktif {trx.id_transaksi}; tidak dapat dihapus."
                )
        del self.peralatan[kode]
        return True

    def cari_alat(self, keyword: str) -> List[Peralatan]:
        """Tantangan A: kode (persis), sebagian nama, atau kategori; tanpa peka huruf besar/kecil."""
        k = keyword.strip().lower()
        return [a for a in self.peralatan.values()
                if k == a.kode_alat.lower() or k in a.nama_alat.lower() or k in a.kategori.lower()]

    def alat_tersedia(self) -> List[Peralatan]:
        return [a for a in self.peralatan.values() if a.tersedia]

    def alat_dipinjam(self) -> List[Peralatan]:
        return [a for a in self.peralatan.values() if not a.tersedia and a.kondisi == "baik"]

    def alat_rusak(self) -> List[Peralatan]:
        return [a for a in self.peralatan.values() if a.kondisi != "baik"]

    def buat_transaksi(self, nim: str, daftar_kode: List[str],
                       lama_hari: int = MAKS_HARI_PINJAM,
                       tanggal_pinjam: Optional[date] = None) -> TransaksiPeminjaman:
        tanggal_pinjam = tanggal_pinjam or date.today()
        mhs = self.mahasiswa.get(nim)
        if mhs is None:
            raise ValueError(f"Mahasiswa {nim} tidak ditemukan.")
        if not daftar_kode:
            raise ValueError("Transaksi minimal berisi 1 alat.")
        if len(set(daftar_kode)) != len(daftar_kode):
            raise ValueError("Kode alat duplikat dalam satu transaksi.")
        if not mhs.boleh_meminjam():
            raise ValueError("Mahasiswa sudah memiliki 2 transaksi aktif.")
        if not 1 <= lama_hari <= MAKS_HARI_PINJAM:
            raise ValueError(f"Lama pinjam harus 1-{MAKS_HARI_PINJAM} hari.")
        daftar_alat = []
        for kode in daftar_kode:
            alat = self.peralatan.get(kode)
            if alat is None:
                raise ValueError(f"Alat {kode} tidak ditemukan.")
            if not alat.dapat_dipinjam():
                raise ValueError(f"Alat {kode} tidak tersedia.")
            daftar_alat.append(alat)
        self._urutan_transaksi += 1
        id_trx = f"TRX{self._urutan_transaksi:03d}"
        trx = TransaksiPeminjaman(id_trx, mhs, tanggal_pinjam,
                                  tanggal_pinjam + timedelta(days=lama_hari))
        for alat in daftar_alat:
            trx.tambah_item(alat)
            alat.tandai_dipinjam()
        mhs.tambah_transaksi_aktif(id_trx)
        self.transaksi[id_trx] = trx
        return trx

    def proses_pengembalian(self, id_transaksi: str, kode_alat: str, kondisi: str,
                            tanggal: Optional[date] = None) -> bool:
        """Kembalikan satu alat. True jika berhasil; status baru ada di transaksi[id].status."""
        tanggal = tanggal or date.today()
        kondisi = kondisi.strip().lower()
        trx = self.transaksi.get(id_transaksi)
        if trx is None:
            raise ValueError(f"Transaksi {id_transaksi} tidak ditemukan.")
        if kondisi not in KONDISI_VALID:
            raise ValueError(f"Kondisi harus salah satu dari: {', '.join(KONDISI_VALID)}.")
        item_alat = [i for i in trx.daftar_item if i.alat.kode_alat == kode_alat]
        if not item_alat:
            raise ValueError(f"Alat {kode_alat} tidak ada pada transaksi {id_transaksi}.")
        item = item_alat[0]
        if not item.masih_dipinjam():
            raise ValueError(f"Alat {kode_alat} sudah dikembalikan sebelumnya.")
        item.kembalikan(kondisi, tanggal)
        item.alat.proses_pengembalian(kondisi)
        trx.update_status()
        if trx.seluruh_alat_kembali():
            trx.mahasiswa.hapus_transaksi_aktif(id_transaksi)
        return True

    def cari_transaksi_mahasiswa(self, nim: str) -> List[TransaksiPeminjaman]:
        """Transaksi AKTIF milik mahasiswa (dipinjam / sebagian dikembalikan)."""
        return [t for t in self.transaksi.values()
                if t.mahasiswa.nim == nim and t.status in STATUS_AKTIF]

    def riwayat_peminjaman(self, nim: str) -> List[TransaksiPeminjaman]:
        """Semua transaksi (aktif + selesai) milik mahasiswa."""
        if nim not in self.mahasiswa:
            raise ValueError(f"Mahasiswa {nim} tidak ditemukan.")
        return [t for t in self.transaksi.values() if t.mahasiswa.nim == nim]