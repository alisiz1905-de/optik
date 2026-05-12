# depo.py — Stok ve müşteri yönetimi (repository katmanı)

from models import Gozluk, Musteri, KiralamaKaydi


class Depo:
    """Gözlük stoğunu, müşteri listesini ve kiralama kayıtlarını tutar."""

    def __init__(self):
        self.__gozlukler: list[Gozluk] = []
        self.__musteriler: list[Musteri] = []
        self.__kayitlar: list[KiralamaKaydi] = []
        self.__g_sayac = 1          # Otomatik ID üreteci
        self.__m_sayac = 1
        self.__k_sayac = 1

    # ── Gözlük işlemleri ──────────────────────────────────────────────────────
    def gozluk_ekle(self, marka: str, model: str, ucret: float) -> Gozluk:
        g = Gozluk(self.__g_sayac, marka, model, ucret)
        self.__gozlukler.append(g)
        self.__g_sayac += 1
        return g

    def tum_gozlukler(self) -> list[Gozluk]:
        return list(self.__gozlukler)

    def musait_gozlukler(self) -> list[Gozluk]:
        return [g for g in self.__gozlukler if g.musait]

    def gozluk_bul(self, gid: int) -> Gozluk | None:
        return next((g for g in self.__gozlukler if g.id == gid), None)

    # ── Müşteri işlemleri ─────────────────────────────────────────────────────
    def musteri_ekle(self, ad: str, soyad: str, telefon: str) -> Musteri:
        m = Musteri(self.__m_sayac, ad, soyad, telefon)
        self.__musteriler.append(m)
        self.__m_sayac += 1
        return m

    def tum_musteriler(self) -> list[Musteri]:
        return list(self.__musteriler)

    def musteri_bul(self, mid: int) -> Musteri | None:
        return next((m for m in self.__musteriler if m.id == mid), None)

    # ── Kiralama işlemleri ────────────────────────────────────────────────────
    def kiralama_baslat(self, musteri: Musteri, gozluk: Gozluk) -> KiralamaKaydi:
        gozluk.kirala()                                   # ValueError fırlatabilir
        k = KiralamaKaydi(self.__k_sayac, musteri, gozluk)
        self.__kayitlar.append(k)
        self.__k_sayac += 1
        return k

    def kiralama_iade(self, kayit_id: int) -> KiralamaKaydi:
        k = next((r for r in self.__kayitlar if r._kayit_id == kayit_id and r.aktif_mi()), None)
        if not k:
            raise ValueError("Aktif kiralama kaydı bulunamadı.")
        k.iade_et()
        return k

    def tum_kayitlar(self) -> list[KiralamaKaydi]:
        return list(self.__kayitlar)

    def aktif_kiralamalar(self) -> list[KiralamaKaydi]:
        return [k for k in self.__kayitlar if k.aktif_mi()]
