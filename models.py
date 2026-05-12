# models.py — Temel veri sınıfları (OOP: Sınıf, Kapsülleme, Kalıtım)

from datetime import date


class Gozluk:
    """Bir gözlük çerçevesini temsil eder."""

    def __init__(self, gozluk_id: int, marka: str, model: str, gunluk_ucret: float):
        self.__id = gozluk_id
        self.__marka = marka
        self.__model = model
        self.__gunluk_ucret = gunluk_ucret
        self.__musait = True          # Kapsülleme: dışarıdan doğrudan değiştirilemiyor

    # --- Getter'lar ---
    @property
    def id(self):
        return self.__id

    @property
    def marka(self):
        return self.__marka

    @property
    def model(self):
        return self.__model

    @property
    def gunluk_ucret(self):
        return self.__gunluk_ucret

    @property
    def musait(self):
        return self.__musait

    # --- Durum değiştirme ---
    def kirala(self):
        if not self.__musait:
            raise ValueError(f"{self.__marka} {self.__model} zaten kirada!")
        self.__musait = False

    def iade_al(self):
        self.__musait = True

    def __str__(self):
        durum = "Müsait" if self.__musait else "Kirada"
        return (f"[{self.__id}] {self.__marka} {self.__model} "
                f"| {self.__gunluk_ucret:.2f} TL/gün | {durum}")


class Musteri:
    """Bir müşteriyi temsil eder."""

    def __init__(self, musteri_id: int, ad: str, soyad: str, telefon: str):
        self.__id = musteri_id
        self.__ad = ad
        self.__soyad = soyad
        self.__telefon = telefon

    @property
    def id(self):
        return self.__id

    @property
    def ad_soyad(self):
        return f"{self.__ad} {self.__soyad}"

    @property
    def telefon(self):
        return self.__telefon

    def __str__(self):
        return f"[{self.__id}] {self.ad_soyad} | Tel: {self.__telefon}"


class KiralamaKaydi:
    """Bir kiralama işlemini temsil eder (Kalıtım için temel sınıf)."""

    def __init__(self, kayit_id: int, musteri: Musteri, gozluk: Gozluk):
        self._kayit_id = kayit_id
        self._musteri = musteri
        self._gozluk = gozluk
        self._baslangic = date.today()
        self._bitis = None

    def iade_et(self):
        self._bitis = date.today()
        self._gozluk.iade_al()

    def toplam_ucret(self) -> float:
        bitis = self._bitis if self._bitis else date.today()
        gun = max((bitis - self._baslangic).days, 1)
        return gun * self._gozluk.gunluk_ucret

    def aktif_mi(self) -> bool:
        return self._bitis is None

    def __str__(self):
        bitis_str = str(self._bitis) if self._bitis else "Devam ediyor"
        return (f"Kayıt #{self._kayit_id} | {self._musteri.ad_soyad} → "
                f"{self._gozluk.marka} {self._gozluk.model} | "
                f"Başlangıç: {self._baslangic} | Bitiş: {bitis_str} | "
                f"Ücret: {self.toplam_ucret():.2f} TL")
