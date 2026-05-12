# arayuz.py — Konsol menüsü ve kullanıcı etkileşimi

from depo import Depo


class Arayuz:
    """Menü gösterimi ve kullanıcıdan veri alma işlemlerini yönetir."""

    def __init__(self, depo: Depo):
        self.__depo = depo

    # ── Yardımcı giriş fonksiyonları ──────────────────────────────────────────
    @staticmethod
    def _gir(mesaj: str) -> str:
        return input(f"  {mesaj}: ").strip()

    @staticmethod
    def _gir_int(mesaj: str) -> int:
        while True:
            try:
                return int(input(f"  {mesaj}: ").strip())
            except ValueError:
                print("  ⚠ Lütfen geçerli bir sayı girin.")

    @staticmethod
    def _gir_float(mesaj: str) -> float:
        while True:
            try:
                return float(input(f"  {mesaj}: ").strip())
            except ValueError:
                print("  ⚠ Lütfen geçerli bir sayı girin.")

    @staticmethod
    def _baslik(metin: str):
        print(f"\n{'─'*45}")
        print(f"  {metin}")
        print(f"{'─'*45}")

    # ── Gözlük ekranları ──────────────────────────────────────────────────────
    def gozluk_ekle(self):
        self._baslik("YENİ GÖZLÜK EKLE")
        marka = self._gir("Marka")
        model = self._gir("Model")
        ucret = self._gir_float("Günlük ücret (TL)")
        g = self.__depo.gozluk_ekle(marka, model, ucret)
        print(f"\n  ✅ Eklendi → {g}")

    def gozluk_listele(self):
        self._baslik("TÜM GÖZLÜKLER")
        liste = self.__depo.tum_gozlukler()
        if not liste:
            print("  Henüz gözlük eklenmedi.")
            return
        for g in liste:
            print(f"  {g}")

    # ── Müşteri ekranları ─────────────────────────────────────────────────────
    def musteri_ekle(self):
        self._baslik("YENİ MÜŞTERİ EKLE")
        ad = self._gir("Ad")
        soyad = self._gir("Soyad")
        tel = self._gir("Telefon")
        m = self.__depo.musteri_ekle(ad, soyad, tel)
        print(f"\n  ✅ Eklendi → {m}")

    def musteri_listele(self):
        self._baslik("TÜM MÜŞTERİLER")
        liste = self.__depo.tum_musteriler()
        if not liste:
            print("  Henüz müşteri eklenmedi.")
            return
        for m in liste:
            print(f"  {m}")

    # ── Kiralama ekranları ────────────────────────────────────────────────────
    def kiralama_baslat(self):
        self._baslik("GÖZLÜK KİRALA")
        musaitler = self.__depo.musait_gozlukler()
        if not musaitler:
            print("  Müsait gözlük yok.")
            return
        print("  Müsait gözlükler:")
        for g in musaitler:
            print(f"    {g}")
        gid = self._gir_int("Gözlük ID")
        gozluk = self.__depo.gozluk_bul(gid)
        if not gozluk:
            print("  ⚠ Gözlük bulunamadı.")
            return

        self.musteri_listele()
        mid = self._gir_int("Müşteri ID")
        musteri = self.__depo.musteri_bul(mid)
        if not musteri:
            print("  ⚠ Müşteri bulunamadı.")
            return

        try:
            k = self.__depo.kiralama_baslat(musteri, gozluk)
            print(f"\n  ✅ Kiralama başlatıldı → {k}")
        except ValueError as e:
            print(f"  ⚠ {e}")

    def kiralama_iade(self):
        self._baslik("İADE AL")
        aktifler = self.__depo.aktif_kiralamalar()
        if not aktifler:
            print("  Aktif kiralama yok.")
            return
        print("  Aktif kiralamalar:")
        for k in aktifler:
            print(f"    {k}")
        kid = self._gir_int("İade edilecek Kayıt #")
        try:
            k = self.__depo.kiralama_iade(kid)
            print(f"\n  ✅ İade alındı. Toplam ücret: {k.toplam_ucret():.2f} TL")
        except ValueError as e:
            print(f"  ⚠ {e}")

    # ── Rapor ekranı ──────────────────────────────────────────────────────────
    def rapor_goster(self):
        self._baslik("KİRALAMA GEÇMİŞİ & RAPOR")
        kayitlar = self.__depo.tum_kayitlar()
        if not kayitlar:
            print("  Henüz kiralama kaydı yok.")
            return
        toplam = 0.0
        for k in kayitlar:
            print(f"  {k}")
            toplam += k.toplam_ucret()
        print(f"\n  {'─'*40}")
        print(f"  Toplam kazanç (tüm kayıtlar): {toplam:.2f} TL")
        print(f"  Aktif kiralama sayısı       : {len(self.__depo.aktif_kiralamalar())}")
