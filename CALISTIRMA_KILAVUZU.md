# 🚀 ATASUN GÖZLÜK KİRALAMA SİSTEMİ - ÇALIŞTIRMA KILAVUZU

## 🌐 WEB ARAYÜZÜ (ÖNERİLEN - FLASK)

### 📦 Kurulum
```bash
pip install Flask
```

### ▶️ Çalıştırma
```bash
python web_app.py
```

### 🌍 Tarayıcıda Açma
Otomatik açılmazsa şu adresi tarayıcıya yazın:
```
http://127.0.0.1:5000
```

veya

```
http://localhost:5000
```

---

## 💻 KONSOL ARAYÜZÜ (ALTERNATİF)

### ▶️ Çalıştırma
```bash
python main.py
```

Kurulum gerektirmez, hemen çalışır!

---

## 📱 ÖZELLİKLER

### Web Arayüzü (Flask)
✅ Modern, renkli tasarım
✅ Mobil ve masaüstü uyumlu
✅ Kolay form girişleri
✅ Gerçek zamanlı tablolar
✅ Anlık istatistikler

### Konsol Arayüzü
✅ ANSI renk kodları
✅ İkonlu menüler
✅ Hızlı terminal erişimi

---

## 🆘 SORUN GİDERME

### Flask kurulmazsa:
```bash
python -m pip install Flask
```

### Port 5000 kullanılıyorsa:
`web_app.py` dosyasında son satırı şöyle değiştir:
```python
app.run(debug=True, host='0.0.0.0', port=8080)
```
Sonra tarayıcıda: `http://127.0.0.1:8080`

### Admin yetkisi gerekiyorsa:
PowerShell'i "Yönetici Olarak Çalıştır"

---

## 📚 DOSYA YAPISI

```
gozluk_kiralama/
├── web_app.py          # 🌐 Flask web arayüzü (YENİ!)
├── main.py             # 💻 Konsol versiyonu
├── models.py           # 📦 Veri sınıfları
├── depo.py             # 🗄️ Veri yönetimi
├── arayuz.py           # 🖥️ Terminal arayüzü
└── requirements.txt    # 📋 Bağımlılıklar
```

---

## 🎯 HIZLI BAŞLANGIÇ

1. **Flask'ı kur:**
   ```bash
   pip install Flask
   ```

2. **Uygulamayı başlat:**
   ```bash
   python web_app.py
   ```

3. **Tarayıcıda aç:**
   ```
   http://127.0.0.1:5000
   ```

4. **Kullan!** 🎉

---

## 💡 İPUCU

Web arayüzü sunumda çok daha etkileyici görünür!
- Renkli grafikler
- Modern tasarım
- Kolay kullanım
- Profesyonel görünüm

Başarılar! 🚀👓
