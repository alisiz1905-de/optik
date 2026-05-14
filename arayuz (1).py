# arayuz.py — Modern konsol arayüzü ve kullanıcı etkileşimi

from depo import Depo
import os
import sys


class Renkler:
    """ANSI renk kodları — terminal görselleştirmesi için"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    MAVI = '\033[94m'
    YESIL = '\033[92m'
    SARI = '\033[93m'
    KIRMIZI = '\033[91m'
    TURKUAZ = '\033[96m'
    MOR = '\033[95m'
    BEYAZ = '\033[97m'
    GRI = '\033[90m'


class Arayuz:
    """Modern menü gösterimi ve kullanıcıdan veri alma işlemlerini yönetir."""

    def __init__(self, depo: Depo):
        self.__depo = depo

    # ── Ekran temizleme ───────────────────────────────────────────────────────
    @staticmethod
    def ekran_temizle():
        os.system('cls' if os.name == 'nt' else 'clear')

    # ── Yardımcı giriş fonksiyonları ──────────────────────────────────────────
    @staticmethod
    def _gir(mesaj: str) -> str:
        return input(f"{Renkler.TURKUAZ}  ▸ {mesaj}: {Renkler.RESET}").strip()

    @staticmethod
    def _gir_int(mesaj: str) -> int:
        while True:
            try:
                return int(input(f"{Renkler.TURKUAZ}  ▸ {mesaj}: {Renkler.RESET}").strip())
            except ValueError:
                print(f"{Renkler.KIRMIZI}  ✖ Lütfen geçerli bir sayı girin.{Renkler.RESET}")

    @staticmethod
    def _gir_float(mesaj: str) -> float:
        while True:
            try:
                return float(input(f"{Renkler.TURKUAZ}  ▸ {mesaj}: {Renkler.RESET}").strip())
            except ValueError:
                print(f"{Renkler.KIRMIZI}  ✖ Lütfen geçerli bir sayı girin.{Renkler.RESET}")

    @staticmethod
    def _baslik(metin: str, renk=Renkler.MAVI):
        print(f"\n{renk}{'═'*60}{Renkler.RESET}")
        print(f"{renk}{Renkler.BOLD}  {metin}{Renkler.RESET}")
        print(f"{renk}{'═'*60}{Renkler.RESET}")

    @staticmethod
    def _devam():
        input(f"\n{Renkler.GRI}  [Enter] tuşuna basarak devam edin...{Renkler.RESET}")

    # ── Gözlük ekranları ──────────────────────────────────────────────────────
    def gozluk_ekle(self):
        self.ekran_temizle()
        self._baslik("👓  YENİ GÖZLÜK EKLE", Renkler.YESIL)
        print(f"{Renkler.GRI}  Lütfen aşağıdaki bilgileri girin:{Renkler.RESET}\n")
        
        marka = self._gir("Marka")
        model = self._gir("Model")
        ucret = self._gir_float("Günlük ücret (TL)")
        
        g = self.__depo.gozluk_ekle(marka, model, ucret)
        print(f"\n{Renkler.YESIL}  ✔ Başarıyla eklendi!{Renkler.RESET}")
        print(f"{Renkler.BEYAZ}  {g}{Renkler.RESET}")
        self._devam()

    def gozluk_listele(self):
        self.ekran_temizle()
        self._baslik("👓  TÜM GÖZLÜKLER", Renkler.MAVI)
        liste = self.__depo.tum_gozlukler()
        
        if not liste:
            print(f"{Renkler.SARI}  ⚠ Henüz gözlük eklenmedi.{Renkler.RESET}")
            self._devam()
            return
            
        print(f"{Renkler.GRI}  Toplam {len(liste)} adet gözlük bulundu:\n{Renkler.RESET}")
        for g in liste:
            durum_renk = Renkler.YESIL if g.musait else Renkler.KIRMIZI
            print(f"  {durum_renk}●{Renkler.RESET} {g}")
        self._devam()

    # ── Müşteri ekranları ─────────────────────────────────────────────────────
    def musteri_ekle(self):
        self.ekran_temizle()
        self._baslik("👤  YENİ MÜŞTERİ EKLE", Renkler.YESIL)
        print(f"{Renkler.GRI}  Lütfen aşağıdaki bilgileri girin:{Renkler.RESET}\n")
        
        ad = self._gir("Ad")
        soyad = self._gir("Soyad")
        tel = self._gir("Telefon")
        
        m = self.__depo.musteri_ekle(ad, soyad, tel)
        print(f"\n{Renkler.YESIL}  ✔ Başarıyla eklendi!{Renkler.RESET}")
        print(f"{Renkler.BEYAZ}  {m}{Renkler.RESET}")
        self._devam()

    def musteri_listele(self):
        self.ekran_temizle()
        self._baslik("👤  TÜM MÜŞTERİLER", Renkler.MAVI)
        liste = self.__depo.tum_musteriler()
        
        if not liste:
            print(f"{Renkler.SARI}  ⚠ Henüz müşteri eklenmedi.{Renkler.RESET}")
            self._devam()
            return
            
        print(f"{Renkler.GRI}  Toplam {len(liste)} müşteri kayıtlı:\n{Renkler.RESET}")
        for m in liste:
            print(f"  {Renkler.TURKUAZ}●{Renkler.RESET} {m}")
        self._devam()

    # ── Kiralama ekranları ────────────────────────────────────────────────────
    def kiralama_baslat(self):
        self.ekran_temizle()
        self._baslik("🔑  GÖZLÜK KİRALAMA İŞLEMİ", Renkler.MOR)
        
        musaitler = self.__depo.musait_gozlukler()
        if not musaitler:
            print(f"{Renkler.KIRMIZI}  ✖ Şu anda müsait gözlük bulunmuyor.{Renkler.RESET}")
            self._devam()
            return
            
        print(f"{Renkler.YESIL}  ✔ Müsait gözlükler:{Renkler.RESET}\n")
        for g in musaitler:
            print(f"  {Renkler.YESIL}●{Renkler.RESET} {g}")
        
        print()
        gid = self._gir_int("Kiralanacak Gözlük ID")
        gozluk = self.__depo.gozluk_bul(gid)
        
        if not gozluk:
            print(f"{Renkler.KIRMIZI}  ✖ Gözlük bulunamadı.{Renkler.RESET}")
            self._devam()
            return

        print(f"\n{Renkler.MAVI}  Müşteri Listesi:{Renkler.RESET}\n")
        for m in self.__depo.tum_musteriler():
            print(f"  {Renkler.TURKUAZ}●{Renkler.RESET} {m}")
        
        print()
        mid = self._gir_int("Müşteri ID")
        musteri = self.__depo.musteri_bul(mid)
        
        if not musteri:
            print(f"{Renkler.KIRMIZI}  ✖ Müşteri bulunamadı.{Renkler.RESET}")
            self._devam()
            return

        try:
            k = self.__depo.kiralama_baslat(musteri, gozluk)
            print(f"\n{Renkler.YESIL}  ✔ Kiralama başarıyla oluşturuldu!{Renkler.RESET}")
            print(f"{Renkler.BEYAZ}  {k}{Renkler.RESET}")
        except ValueError as e:
            print(f"{Renkler.KIRMIZI}  ✖ Hata: {e}{Renkler.RESET}")
        
        self._devam()

    def kiralama_iade(self):
        self.ekran_temizle()
        self._baslik("↩️  İADE İŞLEMİ", Renkler.SARI)
        
        aktifler = self.__depo.aktif_kiralamalar()
        if not aktifler:
            print(f"{Renkler.SARI}  ⚠ Aktif kiralama bulunmuyor.{Renkler.RESET}")
            self._devam()
            return
            
        print(f"{Renkler.YESIL}  Aktif kiralamalar:{Renkler.RESET}\n")
        for k in aktifler:
            print(f"  {Renkler.YESIL}●{Renkler.RESET} {k}")
        
        print()
        kid = self._gir_int("İade edilecek Kayıt Numarası")
        
        try:
            k = self.__depo.kiralama_iade(kid)
            print(f"\n{Renkler.YESIL}  ✔ İade işlemi tamamlandı!{Renkler.RESET}")
            print(f"{Renkler.BOLD}{Renkler.BEYAZ}  Toplam Ücret: {k.toplam_ucret():.2f} TL{Renkler.RESET}")
        except ValueError as e:
            print(f"{Renkler.KIRMIZI}  ✖ Hata: {e}{Renkler.RESET}")
        
        self._devam()

    # ── Rapor ekranı ──────────────────────────────────────────────────────────
    def rapor_goster(self):
        self.ekran_temizle()
        self._baslik("📊  KİRALAMA GEÇMİŞİ & RAPOR", Renkler.TURKUAZ)
        
        kayitlar = self.__depo.tum_kayitlar()
        if not kayitlar:
            print(f"{Renkler.SARI}  ⚠ Henüz kiralama kaydı bulunmuyor.{Renkler.RESET}")
            self._devam()
            return
            
        toplam = 0.0
        aktif_sayisi = 0
        tamamlanan_sayisi = 0
        
        print(f"{Renkler.GRI}  Tüm kiralama kayıtları:\n{Renkler.RESET}")
        for k in kayitlar:
            if k.aktif_mi():
                print(f"  {Renkler.YESIL}●{Renkler.RESET} {k}")
                aktif_sayisi += 1
            else:
                print(f"  {Renkler.GRI}●{Renkler.RESET} {k}")
                tamamlanan_sayisi += 1
            toplam += k.toplam_ucret()
        
        print(f"\n{Renkler.BOLD}{'─'*60}{Renkler.RESET}")
        print(f"{Renkler.BOLD}  📈 ÖZET İSTATİSTİKLER{Renkler.RESET}")
        print(f"{Renkler.BOLD}{'─'*60}{Renkler.RESET}")
        print(f"{Renkler.YESIL}  Aktif Kiralama        : {aktif_sayisi} adet{Renkler.RESET}")
        print(f"{Renkler.GRI}  Tamamlanan Kiralama   : {tamamlanan_sayisi} adet{Renkler.RESET}")
        print(f"{Renkler.MAVI}  Toplam Kayıt          : {len(kayitlar)} adet{Renkler.RESET}")
        print(f"{Renkler.BOLD}{Renkler.SARI}  💰 Toplam Kazanç      : {toplam:.2f} TL{Renkler.RESET}")
        print(f"{Renkler.BOLD}{'─'*60}{Renkler.RESET}")
        
        self._devam()
