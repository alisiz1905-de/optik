# 👓 Atasun Gözlük Kiralama Sistemi

Kastamonu Üniversitesi Tosya Meslek Yüksekokulu  
**Programlama II** dersi dönem sonu projesi

---

## 📌 Projenin Amacı

Bir gözlük mağazasının kiralama süreçlerini yönetmek için geliştirilmiş **modern web ve konsol uygulamasıdır**. Müşteri kayıt yönetimi, gözlük stok takibi, kiralama işlemlerinin başlatılması ve iade alınması, günlük ücret hesaplaması ve detaylı raporlama işlevlerini içermektedir.

Programlama II dersinde öğrenilen **Nesne Tabanlı Programlama (OOP)** ilkeleri, **modüler kod yapısı** ve Python'un ileri düzey özelliklerinin uygulamalı bir projede birleştirilmesi hedeflenmiştir.

---

## 👥 Grup Üyeleri ve Görev Dağılımı

| İsim | Okul No | Sorumluluk |
|------|---------|------------|
| Kürşad Oral | 255815014 | `models.py` — Gozluk, Musteri, KiralamaKaydi sınıfları |
| Talha Eser | 255815043 | `depo.py` — Stok ve kayıt yönetimi |
| Ali Altuntaş | 255815016 |  `arayuz.py` — Konsol arayüzü |

---

## 🗂 Dosya Yapısı

```
gozluk_kiralama/
├── web_app.py             # 🌐 Flask web arayüzü (ÖNERİLEN!)
├── main.py                # 💻 Konsol versiyonu giriş noktası
├── models.py              # 📦 Veri sınıfları (Gozluk, Musteri, KiralamaKaydi)
├── depo.py                # 🗄️ Depo sınıfı — stok, müşteri ve kiralama yönetimi
├── arayuz.py              # 🖥️ Terminal arayüzü sınıfı (konsol versiyonu için)
├── requirements.txt       # 📋 Python bağımlılıkları
├── README.md              # 📖 Bu dosya
└── CALISTIRMA_KILAVUZU.md # 🚀 Detaylı çalıştırma talimatları
```

---

## 🏗 OOP Yapısı ve Mimari

### Sınıf Yapısı

| Sınıf | Dosya | Açıklama |
|-------|-------|----------|
| `Gozluk` | models.py | Gözlük bilgilerini ve müsaitlik durumunu tutar. `__private` alanlarla kapsülleme uygulanmıştır. |
| `Musteri` | models.py | Müşteri ad, soyad ve telefon bilgilerini tutar. |
| `KiralamaKaydi` | models.py | Bir kiralama işlemini temsil eder; başlangıç/bitiş tarihi ve ücret hesabı içerir. |
| `Depo` | depo.py | Gözlük, müşteri ve kiralama listelerini yönetir. Repository pattern ile tüm iş mantığı burada toplanmıştır. |
| `Arayuz` | arayuz.py | Konsol arayüzü için terminal etkileşimi. ANSI renk kodları ile modern görünüm. |
| `Renkler` | arayuz.py | ANSI renk kodlarını sabitler olarak tanımlar. Terminal görselleştirmesi için. |

### Kullanılan OOP Kavramları

- **Kapsülleme (Encapsulation):** `Gozluk.__musait` gibi `__private` alanlar doğrudan değiştirilemez, kontrollü erişim sağlanır
- **Property Dekoratörleri:** `@property` ile getter metodları, veri kontrolü ve okunabilirlik
- **`__str__` Metodları:** Her sınıf kendi çıktı formatını tanımlar
- **Bağımlılık Enjeksiyonu:** `Arayuz(depo)` — sınıflar birbirine sıkı bağlı değil, bağımlılık dışarıdan verilir
- **Repository Pattern:** Depo sınıfı, veri yönetimini merkezi bir katmanda toplar
- **Separation of Concerns:** Her modül tek bir sorumluluğa sahip

### Katmanlı Mimari

1. **Veri Katmanı** (`models.py`) — Sınıf tanımları, veri modelleri
2. **İş Mantığı Katmanı** (`depo.py`) — Repository pattern, iş kuralları
3. **Sunum Katmanı** (`web_app.py` / `arayuz.py`) — Kullanıcı arayüzü

---

## ▶ Kurulum ve Çalıştırma

**Gereksinim:** Python 3.10 veya üzeri

### 🌐 Web Arayüzü (Flask) — ÖNERİLEN

```bash
# Bağımlılıkları yükle
pip install Flask

# Uygulamayı başlat
python web_app.py
```

Tarayıcınızda otomatik olarak `http://127.0.0.1:5000` açılacaktır.

### 💻 Konsol Arayüzü (Alternatif)

```bash
# Bağımlılık yok, doğrudan çalıştır
python main.py
```

Renkli ve modern terminal arayüzü ile çalışır.

---

## 🎨 Arayüz Özellikleri

### 🌐 Web Arayüzü (Flask)

#### Ana Sayfa
- **İstatistik Kartları:** Toplam gözlük, müsait gözlük, kayıtlı müşteri, aktif kiralama sayıları
- **Gradient renkli kartlar** (mor-mavi geçişli)
- **Müsait gözlükler listesi** — anlık durum
- **Aktif kiralamalar özeti**

#### Gözlük İşlemleri
- ➕ **Gözlük Ekle:** Form ile marka, model ve günlük ücret girişi
- 📋 **Gözlük Listesi:** Tablo formatında, müsaitlik durumu rozetleri ile (✅ Müsait / ❌ Kirada)

#### Müşteri İşlemleri
- ➕ **Müşteri Ekle:** Ad, soyad ve telefon girişi formu
- 📋 **Müşteri Listesi:** Tüm kayıtlı müşteriler tablosu

#### Kiralama İşlemleri
- 🔑 **Gözlük Kirala:** Dropdown menülerden kolay seçim, anlık kiralama başlatma
- ↩️ **İade Al:** Aktif kiralamaları iade etme, otomatik ücret hesaplama ve gösterim

#### Raporlar
- 📊 **İstatistik Kartları:** Aktif/tamamlanan kiralama sayıları, toplam kazanç
- 📋 **Detaylı Tablo:** Tüm kiralama kayıtları, tarih ve durum bilgileri
- 💰 **Toplam Kazanç Özeti**

#### Tasarım Özellikleri
- 🎨 Gradient renkler (mor-mavi)
- 📱 Responsive tasarım (mobil ve masaüstü uyumlu)
- ⚡ Animasyonlar ve hover efektleri
- 🎯 Modern UI (rounded corners, shadow effects)
- 🔔 Flash mesajları (başarı, hata, bilgi)

### 💻 Konsol Arayüzü

#### Özellikler
- **ANSI Renk Kodları:** Mavi, yeşil, kırmızı, turkuaz, sarı, mor renkler
- **Durum İkonları:** ● sembolleri ile görsel ayrım (yeşil=müsait, kırmızı=kirada)
- **Modern Menü Tasarımı:** Çerçeveli, renkli, profesyonel
- **Ekran Temizleme:** Her işlem öncesi temiz ekran
- **Başarı/Hata Mesajları:** ✔ ve ✖ işaretleri ile net geri bildirim
- **İstatistik Raporu:** Aktif/tamamlanan kiralama özeti, toplam kazanç
- **Bekleme Mekanizması:** [Enter] ile devam, kullanıcıya okuma fırsatı

#### Menü Yapısı
1. Gözlük Ekle
2. Gözlükleri Listele
3. Müşteri Ekle
4. Müşterileri Listele
5. Gözlük Kirala
6. İade Al
7. Kiralama Geçmişi & Rapor
0. Çıkış

---

## 🖼 Örnek Ekran Çıktıları

### Web Arayüzü
```
┌─────────────────────────────────────────────┐
│  👓 ATASUN GÖZLÜK KİRALAMA SİSTEMİ         │
│     Modern Web Arayüzü ile Kolay Yönetim   │
└─────────────────────────────────────────────┘

[🏠 Ana Sayfa] [👓 Gözlükler] [👤 Müşteriler] [🔑 Kiralama] [📊 Raporlar]

📈 Sistem Özeti
┌─────────────┬─────────────┬─────────────┬─────────────┐
│ 📦 Toplam   │ ✅ Müsait   │ 👥 Kayıtlı  │ 🔄 Aktif    │
│ Gözlük: 3   │ Gözlük: 2   │ Müşteri: 2  │ Kiralama: 1 │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

### Konsol Arayüzü
```
╔══════════════════════════════════════════════════════════╗
║           👓 ATASUN GÖZLÜK KİRALAMA SİSTEMİ              ║
╠══════════════════════════════════════════════════════════╣
║  1. Gözlük Ekle                                          ║
║  2. Gözlükleri Listele                                   ║
║  3. Müşteri Ekle                                         ║
║  4. Müşterileri Listele                                  ║
║  5. Gözlük Kirala                                        ║
║  6. İade Al                                              ║
║  7. Kiralama Geçmişi & Rapor                             ║
║  0. Çıkış                                                ║
╚══════════════════════════════════════════════════════════╝

  ▸ Seçiminiz: 
```

---

## 🛠 Kullanılan Teknolojiler

### Backend & Core
- **Python 3.10+** — Programlama dili
- **Flask 3.0+** — Web framework (hafif, hızlı, güçlü)

### Standart Kütüphaneler
- **datetime** — Tarih ve zaman işlemleri
- **os** — Ekran temizleme (konsol versiyonu)
- **sys** — Sistem işlemleri

### Özellikler
- Veritabanı yok — Hafif, dosya bazlı
- Harici API yok — Bağımsız çalışma
- Minimal bağımlılık — Sadece Flask

---

## 📚 Proje Yapısı Detayları

### models.py
```python
# Veri sınıfları
- Gozluk: id, marka, model, gunluk_ucret, musait
- Musteri: id, ad, soyad, telefon
- KiralamaKaydi: kayit_id, musteri, gozluk, baslangic, bitis
```

### depo.py
```python
# Repository sınıfı
- Gözlük yönetimi: ekle, listele, bul, musait olanları getir
- Müşteri yönetimi: ekle, listele, bul
- Kiralama yönetimi: başlat, iade al, aktif/tümünü getir
- Otomatik ID üretimi
```

### web_app.py
```python
# Flask web uygulaması
- 5 route (ana sayfa, gözlükler, müşteriler, kiralama, raporlar)
- HTML template (embedded CSS)
- Flash mesaj sistemi
- Form handling
```

### arayuz.py
```python
# Konsol arayüz sınıfı
- Renkler sınıfı (ANSI kodları)
- Menü gösterimi
- Kullanıcı giriş fonksiyonları
- Ekran temizleme
```

---

## 🆚 Arayüz Karşılaştırması

| Özellik | Web Arayüzü | Konsol Arayüzü |
|---------|-------------|----------------|
| Kurulum | Flask gerekli | Hiçbir şey gereksiz |
| Görünüm | Modern, renkli, gradient | Terminal renkleri, ASCII |
| Kullanım | Mouse + Keyboard | Sadece Keyboard |
| Mobil | ✅ Uyumlu | ❌ Desktop only |
| Hız | Orta (web render) | ⚡ Çok hızlı |
| Sunum | 🌟 Etkileyici | 💪 Profesyonel |
| Erişim | Tarayıcı | Terminal |

**Öneri:** Sunum için web arayüzü, hızlı test için konsol arayüzü kullanın.

---

## 🎯 Kullanım Senaryoları

### Senaryo 1: Yeni Gözlük Ekleme
1. Web: "Gözlükler" sekmesi → Form doldur → "Gözlük Ekle"
2. Konsol: Ana menüden "1" → Bilgileri gir

### Senaryo 2: Gözlük Kiralama
1. Web: "Kiralama" sekmesi → Gözlük seç → Müşteri seç → "Kiralamayı Başlat"
2. Konsol: Ana menüden "5" → Müsait listeden ID seç → Müşteri ID gir

### Senaryo 3: İade İşlemi
1. Web: "Kiralama" sekmesi → "İade Al" → Kayıt numarası gir → "İade İşlemini Tamamla"
2. Konsol: Ana menüden "6" → Aktif listeden kayıt numarası gir

### Senaryo 4: Rapor Görüntüleme
1. Web: "Raporlar" sekmesi → İstatistikler ve detaylı tablo
2. Konsol: Ana menüden "7" → Tüm kayıtlar ve özet

---

## 🚀 Geliştirme Potansiyeli

### Veritabanı Entegrasyonu
- SQLite / PostgreSQL / MySQL
- Kalıcı veri saklama
- Büyük ölçekli kullanım

### Kullanıcı Sistemi
- Admin / Çalışan rolleri
- Giriş / Çıkış sistemi
- Yetki yönetimi

### Gelişmiş Özellikler
- PDF fatura oluşturma
- E-posta bildirimleri (kiralama hatırlatıcıları)
- SMS entegrasyonu
- QR kod ile hızlı teslim/iade
- Ödeme sistemi entegrasyonu (iyzico, PayTR)

### Raporlama
- Tarih aralığına göre filtreleme
- Grafik ve chart'lar (Chart.js, Plotly)
- Excel export
- PDF rapor oluşturma

### Mobil Uygulama
- React Native
- Flutter
- Ionic

### API
- RESTful API
- JSON response
- Token authentication
- Mobil/web entegrasyonu

---

## 🆘 Sorun Giderme

### Flask kurulumu başarısız
```bash
python -m pip install Flask
# veya
pip install Flask --user
```

### Port 5000 kullanılıyor
`web_app.py` dosyasında son satırı değiştir:
```python
app.run(debug=True, host='0.0.0.0', port=8080)
```
Sonra: `http://127.0.0.1:8080`

### Konsol renkleri görünmüyor (Windows)
PowerShell veya Windows Terminal kullanın, CMD yerine.

### Import hatası
Tüm dosyaların aynı klasörde olduğundan emin olun.

---

## 📖 Öğrenme Kaynakları

### Python OOP
- [Python Docs - Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - OOP](https://realpython.com/python3-object-oriented-programming/)

### Flask
- [Flask Quickstart](https://flask.palletsprojects.com/quickstart/)
- [Flask Tutorial](https://flask.palletsprojects.com/tutorial/)

### Tasarım Desenleri
- Repository Pattern
- Dependency Injection
- MVC Architecture

---

## 📝 Notlar

- Proje eğitim amaçlıdır, production kullanımı için güvenlik önlemleri eklenmelidir
- Veritabanı kullanılmadığı için veriler uygulama yeniden başlatıldığında sıfırlanır
- Demo verileri `web_app.py` ve `main.py` dosyalarında tanımlıdır

---

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.  
Kastamonu Üniversitesi Tosya MYO - Programlama II Dersi © 2024

---

## 👨‍💻 Geliştiriciler

**Kürşad Oral** - Veri Modelleri  
**Talha Eser** - İş Mantığı  
**Ali Altuntaş** - Kullanıcı Arayüzü

---

## 🎓 Teşekkürler

Programlama II dersi kapsamında bu projeyi geliştirme fırsatı verdiği için öğretim görevlilerimize teşekkür ederiz.

---

**📌 Son Güncelleme:** Mayıs 2024  
**📧 İletişim:** [Okul e-posta adresleri]  
**🔗 GitHub:** [Repository linki buraya eklenebilir]
