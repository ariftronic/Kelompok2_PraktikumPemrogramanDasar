from collections import Counter
from typing import List, Optional, Tuple

from modules.mahasiswa import Mahasiswa
from modules.peralatan import Peralatan
from modules.sistem_lab import SistemLaboratorium, STATUS_AKTIF

class StatistikPeminjaman:
    def __init__(self, sistem: SistemLaboratorium):
        self.sistem = sistem

    def ranking_alat(self) -> List[Tuple[Peralatan, int]]:
        hitung, objek = Counter(), {}
        for trx in self.sistem.transaksi.values():
            for item in trx.daftar_item:
                hitung[item.alat.kode_alat] += 1
                objek[item.alat.kode_alat] = item.alat
        return [(objek[k], n) for k, n in hitung.most_common()]

    def ranking_mahasiswa(self) -> List[Tuple[Mahasiswa, int]]:
        hitung, objek = Counter(), {}
        for trx in self.sistem.transaksi.values():
            hitung[trx.mahasiswa.nim] += 1
            objek[trx.mahasiswa.nim] = trx.mahasiswa
        return [(objek[k], n) for k, n in hitung.most_common()]

    def alat_terpopuler(self) -> Optional[Peralatan]:
        """Alat paling sering dipinjam (seri: yang pertama kali dipinjam). None jika belum ada data."""
        ranking = self.ranking_alat()
        return ranking[0][0] if ranking else None

    def mahasiswa_teraktif(self) -> Optional[Mahasiswa]:
        """Mahasiswa dengan transaksi terbanyak. None jika belum ada data."""
        ranking = self.ranking_mahasiswa()
        return ranking[0][0] if ranking else None

    def jumlah_transaksi_selesai(self) -> int:
        return sum(t.status == "selesai" for t in self.sistem.transaksi.values())

    def jumlah_transaksi_aktif(self) -> int:
        return sum(t.status in STATUS_AKTIF for t in self.sistem.transaksi.values())