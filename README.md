# 👓 Atasun Gözlük Kiralama Sistemi

Kastamonu Üniversitesi Tosya Meslek Yüksekokulu  
**Programlama II** dersi dönem sonu projesi

---

## 📌 Projenin Amacı

Bir gözlük mağazasının kiralama süreçlerini yönetmek için geliştirilmiş konsol tabanlı bir uygulamadır. Müşteri ve gözlük ekleme, kiralama başlatma/iade alma ve kazanç raporlama işlemlerini destekler.

---

## 👥 Grup Üyeleri ve Görev Dağılımı

| İsim | Okul No | Sorumluluk |
|------|---------|------------|
| [kürşad oral] | [255815014] | `models.py` — Gozluk, Musteri, KiralamaKaydi sınıfları |
| [talha eser2] | [255815043] | `depo.py` — Stok ve kayıt yönetimi |
| [Ali altuntaş 3] | [255815016] | `arayuz.py` — Konsol menüsü ve kullanıcı etkileşimi |

---

## 🗂 Dosya Yapısı

```
gozluk_kiralama/
├── main.py        # Programın giriş noktası, menü döngüsü
├── models.py      # Veri sınıfları (Gozluk, Musteri, KiralamaKaydi)
├── depo.py        # Depo sınıfı — stok, müşteri ve kiralama yönetimi
├── arayuz.py      # Arayuz sınıfı — konsol ekranları
├── requirements.txt
└── README.md
```

---

## 🏗 OOP Yapısı

| Sınıf | Dosya | Açıklama |
|-------|-------|----------|
| `Gozluk` | models.py | Gözlük bilgilerini ve müsaitlik durumunu tutar. `__private` alanlarla kapsülleme uygulanmıştır. |
| `Musteri` | models.py | Müşteri adı ve telefon bilgilerini tutar. |
| `KiralamaKaydi` | models.py | Bir kiralama işlemini temsil eder; başlangıç/bitiş tarihi ve ücret hesabı içerir. |
| `Depo` | depo.py | Gözlük, müşteri ve kiralama listelerini yönetir. Tüm iş mantığı burada toplanmıştır. |
| `Arayuz` | arayuz.py | Kullanıcıdan veri alır, menüleri gösterir. `Depo` nesnesini kullanır. |

**Kullanılan OOP kavramları:**
- **Kapsülleme:** `Gozluk.__musait` gibi `__private` alanlar doğrudan değiştirilemez
- **Property:** `@property` dekoratörü ile getter metodları
- **`__str__`:** Her sınıf kendi çıktı formatını tanımlar
- **Bağımlılık enjeksiyonu:** `Arayuz(depo)` — sınıflar birbirine bağımlı değil, bağımlılık dışarıdan verilir

---

## ▶ Kurulum ve Çalıştırma

**Gereksinim:** Python 3.10 veya üzeri

```bash
# Depoyu klonla
git clone https://github.com/KULLANICI_ADI/gozluk-kiralama.git
cd gozluk-kiralama

# Bağımlılık yok, doğrudan çalıştır
python main.py
```

---

## 🖥 Örnek Ekran Çıktısı

```
╔══════════════════════════════════╗
║   ATASUN GÖZLÜK KİRALAMA SİSTEMİ  ║
╠══════════════════════════════════╣
║  1. Gözlük Ekle                  ║
║  2. Gözlükleri Listele           ║
║  3. Müşteri Ekle                 ║
║  4. Müşterileri Listele          ║
║  5. Gözlük Kirala                ║
║  6. İade Al                      ║
║  7. Kiralama Geçmişi & Rapor     ║
║  0. Çıkış                        ║
╚══════════════════════════════════╝
```

---

## 🛠 Kullanılan Teknolojiler

- **Python 3.10+**
- Yalnızca standart kütüphane (`datetime`) — harici paket yok
