from datetime import date, timedelta
from typing import Dict, List, Optional

STATUS_DIPINJAM = "dipinjam"
STATUS_SEBAGIAN = "sebagian dikembalikan"
STATUS_SELESAI = "selesai"

MAKS_HARI_PINJAM = 7
MAKS_TRANSAKSI_AKTIF = 2


class ItemPeminjaman:
    def __init__(self, alat):
        self.alat = alat
        self.sudah_dikembalikan: bool = False
        self.tanggal_kembali: Optional[date] = None
        self.kondisi_kembali: Optional[str] = None

    def masih_dipinjam(self) -> bool:
        return not self.sudah_dikembalikan

    def kembalikan(self, kondisi: str, tanggal: date) -> None:
        if self.sudah_dikembalikan:
            raise ValueError(
                f"Alat '{self.alat.kode}' sudah dikembalikan pada {self.tanggal_kembali}."
            )
        if not kondisi or not str(kondisi).strip():
            raise ValueError("Kondisi saat dikembalikan wajib diisi.")
        self.sudah_dikembalikan = True
        self.tanggal_kembali = tanggal
        self.kondisi_kembali = str(kondisi).strip()

    def __repr__(self) -> str:
        status = "kembali" if self.sudah_dikembalikan else "dipinjam"
        return f"ItemPeminjaman({self.alat.kode}, {status})"


class TransaksiPeminjaman:
    """Satu transaksi peminjaman milik satu mahasiswa, berisi satu atau lebih item."""

    def __init__(self, id_transaksi: str, mahasiswa, daftar_alat: List,
                 tanggal_pinjam: date, batas_kembali: Optional[date] = None):
        if not daftar_alat:
            raise ValueError("Satu transaksi wajib berisi minimal satu alat.")
        if batas_kembali is None:
            batas_kembali = tanggal_pinjam + timedelta(days=MAKS_HARI_PINJAM)
        if batas_kembali < tanggal_pinjam:
            raise ValueError("Batas kembali tidak boleh sebelum tanggal pinjam.")
        if batas_kembali > tanggal_pinjam + timedelta(days=MAKS_HARI_PINJAM):
            raise ValueError(
                f"Batas kembali maksimal {MAKS_HARI_PINJAM} hari dari tanggal pinjam."
            )

        self.id_transaksi = id_transaksi
        self.mahasiswa = mahasiswa
        self.daftar_item: List[ItemPeminjaman] = []
        self.tanggal_pinjam = tanggal_pinjam
        self.batas_kembali = batas_kembali
        self.status = STATUS_DIPINJAM

        for alat in daftar_alat:
            self.tambah_item(alat)

    # ---- item ----
    def tambah_item(self, alat) -> ItemPeminjaman:
        """Tambah satu alat ke transaksi. Kode alat tidak boleh duplikat."""
        if any(item.alat.kode == alat.kode for item in self.daftar_item):
            raise ValueError(f"Alat '{alat.kode}' sudah ada di transaksi ini.")
        if self.daftar_item and self.seluruh_alat_kembali():
            raise ValueError("Transaksi sudah selesai; tidak bisa menambah item.")
        item = ItemPeminjaman(alat)
        self.daftar_item.append(item)
        self.update_status()
        return item

    def cari_item(self, kode_alat: str) -> Optional[ItemPeminjaman]:
        for item in self.daftar_item:
            if item.alat.kode == kode_alat:
                return item
        return None

    def kembalikan_alat(self, kode_alat: str, kondisi: str, tanggal: date) -> ItemPeminjaman:
        """Kembalikan satu item berdasarkan kode alat, lalu perbarui status transaksi."""
        item = self.cari_item(kode_alat)
        if item is None:
            raise KeyError(f"Alat '{kode_alat}' tidak ada di transaksi {self.id_transaksi}.")
        item.kembalikan(kondisi, tanggal)
        self.update_status()
        return item

    # ---- status ----
    def hitung_item_belum_kembali(self) -> int:
        return sum(1 for item in self.daftar_item if item.masih_dipinjam())

    def seluruh_alat_kembali(self) -> bool:
        return bool(self.daftar_item) and self.hitung_item_belum_kembali() == 0

    def update_status(self) -> str:
        belum = self.hitung_item_belum_kembali()
        total = len(self.daftar_item)
        if belum == total:
            self.status = STATUS_DIPINJAM
        elif belum == 0:
            self.status = STATUS_SELESAI
        else:
            self.status = STATUS_SEBAGIAN
        return self.status

    def aktif(self) -> bool:
        """Transaksi dianggap aktif selama belum selesai."""
        return self.status != STATUS_SELESAI

    # ---- tampilan ----
    def tampilkan_detail(self) -> str:
        baris = [
            f"ID Transaksi  : {self.id_transaksi}",
            f"Mahasiswa     : {self.mahasiswa.nama} ({self.mahasiswa.nim})",
            f"Tanggal pinjam: {self.tanggal_pinjam}",
            f"Batas kembali : {self.batas_kembali}",
            f"Status        : {self.status}",
            f"Item belum kembali: {self.hitung_item_belum_kembali()} dari {len(self.daftar_item)}",
            "Daftar alat   :",
        ]
        for no, item in enumerate(self.daftar_item, start=1):
            if item.sudah_dikembalikan:
                ket = f"kembali {item.tanggal_kembali}, kondisi {item.kondisi_kembali}"
            else:
                ket = "masih dipinjam"
            baris.append(f"  {no}. {item.alat.kode} - {item.alat.nama} ({ket})")
        teks = "\n".join(baris)
        print(teks)
        return teks

    def __repr__(self) -> str:
        return f"TransaksiPeminjaman({self.id_transaksi}, {self.mahasiswa.nim}, {self.status})"


# ---------------------------------------------------------------------------
# Fungsi pendukung (dipakai buat_transaksi dan modul riwayat)
# ---------------------------------------------------------------------------

def hitung_transaksi_aktif(daftar_transaksi: List[TransaksiPeminjaman], nim: str) -> int:
    """Jumlah transaksi aktif (belum selesai) milik satu mahasiswa."""
    return sum(1 for t in daftar_transaksi if t.mahasiswa.nim == nim and t.aktif())


def id_transaksi_unik(daftar_transaksi: List[TransaksiPeminjaman], id_baru: str) -> bool:
    return all(t.id_transaksi != id_baru for t in daftar_transaksi)


def cari_transaksi_mahasiswa(daftar_transaksi: List[TransaksiPeminjaman],
                             nim: str) -> List[TransaksiPeminjaman]:
    """Semua transaksi (aktif maupun selesai) milik satu mahasiswa."""
    return [t for t in daftar_transaksi if t.mahasiswa.nim == nim]


def riwayat_peminjaman(daftar_transaksi: List[TransaksiPeminjaman],
                       nim: str) -> List[Dict]:
    """Riwayat per item untuk satu mahasiswa, urut dari tanggal pinjam terbaru."""
    hasil = []
    for t in sorted(cari_transaksi_mahasiswa(daftar_transaksi, nim),
                    key=lambda x: x.tanggal_pinjam, reverse=True):
        for item in t.daftar_item:
            hasil.append({
                "id_transaksi": t.id_transaksi,
                "kode_alat": item.alat.kode,
                "nama_alat": item.alat.nama,
                "tanggal_pinjam": t.tanggal_pinjam,
                "batas_kembali": t.batas_kembali,
                "tanggal_kembali": item.tanggal_kembali,
                "kondisi_kembali": item.kondisi_kembali,
                "status_transaksi": t.status,
            })
    return hasil

def statistik_penggunaan_alat(daftar_transaksi: List[TransaksiPeminjaman]) -> Dict[str, int]:
    statistik: Dict[str, int] = {}
    for t in daftar_transaksi:
        for item in t.daftar_item:
            statistik[item.alat.kode] = statistik.get(item.alat.kode, 0) + 1
    return statistik
