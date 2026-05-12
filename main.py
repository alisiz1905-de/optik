# main.py — Programın giriş noktası

from depo import Depo
from arayuz import Arayuz


def menu_goster():
    print("\n╔══════════════════════════════════╗")
    print("║   ATASUN GÖZLÜK KİRALAMA SİSTEMİ  ║")
    print("╠══════════════════════════════════╣")
    print("║  1. Gözlük Ekle                  ║")
    print("║  2. Gözlükleri Listele           ║")
    print("║  3. Müşteri Ekle                 ║")
    print("║  4. Müşterileri Listele          ║")
    print("║  5. Gözlük Kirala                ║")
    print("║  6. İade Al                      ║")
    print("║  7. Kiralama Geçmişi & Rapor     ║")
    print("║  0. Çıkış                        ║")
    print("╚══════════════════════════════════╝")


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

    while True:
        menu_goster()
        secim = input("\n  Seçiminiz: ").strip()
        if secim == "0":
            print("\n  Güle güle! 👓\n")
            break
        elif secim in islemler:
            islemler[secim]()
        else:
            print("  ⚠ Geçersiz seçim, tekrar deneyin.")


if __name__ == "__main__":
    main()
