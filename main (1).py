# main.py — Programın giriş noktası

from depo import Depo
from arayuz import Arayuz, Renkler


def menu_goster():
    print(f"\n{Renkler.BOLD}{Renkler.MAVI}╔{'═'*58}╗{Renkler.RESET}")
    print(f"{Renkler.BOLD}{Renkler.MAVI}║{' '*15}👓 ATASUN GÖZLÜK KİRALAMA SİSTEMİ{' '*10}║{Renkler.RESET}")
    print(f"{Renkler.BOLD}{Renkler.MAVI}╠{'═'*58}╣{Renkler.RESET}")
    print(f"{Renkler.MAVI}║{Renkler.RESET}  {Renkler.YESIL}1.{Renkler.RESET} Gözlük Ekle{' '*43}║")
    print(f"{Renkler.MAVI}║{Renkler.RESET}  {Renkler.MAVI}2.{Renkler.RESET} Gözlükleri Listele{' '*36}║")
    print(f"{Renkler.MAVI}║{Renkler.RESET}  {Renkler.YESIL}3.{Renkler.RESET} Müşteri Ekle{' '*42}║")
    print(f"{Renkler.MAVI}║{Renkler.RESET}  {Renkler.MAVI}4.{Renkler.RESET} Müşterileri Listele{' '*35}║")
    print(f"{Renkler.MAVI}║{Renkler.RESET}  {Renkler.MOR}5.{Renkler.RESET} Gözlük Kirala{' '*41}║")
    print(f"{Renkler.MAVI}║{Renkler.RESET}  {Renkler.SARI}6.{Renkler.RESET} İade Al{' '*47}║")
    print(f"{Renkler.MAVI}║{Renkler.RESET}  {Renkler.TURKUAZ}7.{Renkler.RESET} Kiralama Geçmişi & Rapor{' '*30}║")
    print(f"{Renkler.MAVI}║{Renkler.RESET}  {Renkler.KIRMIZI}0.{Renkler.RESET} Çıkış{' '*49}║")
    print(f"{Renkler.BOLD}{Renkler.MAVI}╚{'═'*58}╝{Renkler.RESET}")


def main():
    depo = Depo()
    arayuz = Arayuz(depo)

    # Demo verisi — sunumda hazır çalışması için
    depo.gozluk_ekle("Ray-Ban", "Aviator", 50.0)
    depo.gozluk_ekle("Oakley", "Holbrook", 40.0)
    depo.gozluk_ekle("Atasun", "Klasik Çerçeve", 30.0)
    depo.musteri_ekle("Ahmet", "Yılmaz", "0555-111-2233")
    depo.musteri_ekle("Ayşe", "Kaya", "0544-987-6543")

    islemler = {
        "1": arayuz.gozluk_ekle,
        "2": arayuz.gozluk_listele,
        "3": arayuz.musteri_ekle,
        "4": arayuz.musteri_listele,
        "5": arayuz.kiralama_baslat,
        "6": arayuz.kiralama_iade,
        "7": arayuz.rapor_goster,
    }

    arayuz.ekran_temizle()
    while True:
        menu_goster()
        secim = input(f"\n{Renkler.TURKUAZ}  ▸ Seçiminiz: {Renkler.RESET}").strip()
        
        if secim == "0":
            arayuz.ekran_temizle()
            print(f"\n{Renkler.YESIL}  ✔ Programdan çıkılıyor...{Renkler.RESET}")
            print(f"{Renkler.BOLD}  Güle güle! 👓{Renkler.RESET}\n")
            break
        elif secim in islemler:
            islemler[secim]()
        else:
            print(f"{Renkler.KIRMIZI}  ✖ Geçersiz seçim, lütfen tekrar deneyin.{Renkler.RESET}")
            input(f"{Renkler.GRI}  [Enter] tuşuna basın...{Renkler.RESET}")
            arayuz.ekran_temizle()


if __name__ == "__main__":
    main()
