"""
ATASUN GÖZLÜK KİRALAMA SİSTEMİ - WEB ARAYÜZÜ
Flask ile Modern Web Uygulaması
"""

from flask import Flask, render_template_string, request, redirect, url_for, flash
from depo import Depo
from datetime import date

app = Flask(__name__)
app.secret_key = 'atasun-gozluk-2024-secret-key'

# Global depo
depo = Depo()

# Demo verisi
depo.gozluk_ekle("Ray-Ban", "Aviator", 50.0)
depo.gozluk_ekle("Oakley", "Holbrook", 40.0)
depo.gozluk_ekle("Atasun", "Klasik Çerçeve", 30.0)
depo.musteri_ekle("Ahmet", "Yılmaz", "0555-111-2233")
depo.musteri_ekle("Ayşe", "Kaya", "0544-987-6543")

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>👓 Atasun Gözlük Kiralama Sistemi</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        
        .header p {
            font-size: 1.1rem;
            opacity: 0.9;
        }
        
        .nav {
            display: flex;
            background: #f8f9fa;
            border-bottom: 2px solid #e0e0e0;
            flex-wrap: wrap;
        }
        
        .nav a {
            flex: 1;
            padding: 15px 20px;
            text-decoration: none;
            color: #333;
            text-align: center;
            font-weight: 600;
            transition: all 0.3s;
            min-width: 150px;
        }
        
        .nav a:hover {
            background: #667eea;
            color: white;
        }
        
        .nav a.active {
            background: #667eea;
            color: white;
        }
        
        .content {
            padding: 30px;
        }
        
        .metrics {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .metric-card h3 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        
        .metric-card p {
            font-size: 1rem;
            opacity: 0.9;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #333;
        }
        
        .form-group input,
        .form-group select {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 1rem;
            transition: border 0.3s;
        }
        
        .form-group input:focus,
        .form-group select:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .table thead {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        
        .table th,
        .table td {
            padding: 15px;
            text-align: left;
        }
        
        .table tbody tr:nth-child(even) {
            background: #f8f9fa;
        }
        
        .table tbody tr:hover {
            background: #e9ecef;
        }
        
        .badge {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }
        
        .badge-success {
            background: #28a745;
            color: white;
        }
        
        .badge-danger {
            background: #dc3545;
            color: white;
        }
        
        .badge-info {
            background: #17a2b8;
            color: white;
        }
        
        .alert {
            padding: 15px 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        
        .alert-success {
            background: #d4edda;
            border-left: 4px solid #28a745;
            color: #155724;
        }
        
        .alert-danger {
            background: #f8d7da;
            border-left: 4px solid #dc3545;
            color: #721c24;
        }
        
        .alert-info {
            background: #d1ecf1;
            border-left: 4px solid #17a2b8;
            color: #0c5460;
        }
        
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        
        .card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .card h3 {
            margin-bottom: 15px;
            color: #667eea;
        }
        
        .footer {
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 2px solid #e0e0e0;
        }
        
        @media (max-width: 768px) {
            .nav {
                flex-direction: column;
            }
            
            .nav a {
                border-bottom: 1px solid #e0e0e0;
            }
            
            .header h1 {
                font-size: 1.8rem;
            }
            
            .metrics {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>👓 ATASUN GÖZLÜK KİRALAMA SİSTEMİ</h1>
            <p>Modern Web Arayüzü ile Kolay Yönetim</p>
        </div>
        
        <div class="nav">
            <a href="/" class="{{ 'active' if page == 'home' else '' }}">🏠 Ana Sayfa</a>
            <a href="/gozlukler" class="{{ 'active' if page == 'gozlukler' else '' }}">👓 Gözlükler</a>
            <a href="/musteriler" class="{{ 'active' if page == 'musteriler' else '' }}">👤 Müşteriler</a>
            <a href="/kiralama" class="{{ 'active' if page == 'kiralama' else '' }}">🔑 Kiralama</a>
            <a href="/raporlar" class="{{ 'active' if page == 'raporlar' else '' }}">📊 Raporlar</a>
        </div>
        
        <div class="content">
            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    {% for category, message in messages %}
                        <div class="alert alert-{{ category }}">{{ message }}</div>
                    {% endfor %}
                {% endif %}
            {% endwith %}
            
            {% block content %}{% endblock %}
        </div>
        
        <div class="footer">
            <p>💻 Kastamonu Üniversitesi Tosya MYO - Programlama II Projesi</p>
            <p>👓 Atasun Gözlük Kiralama Sistemi © 2024</p>
        </div>
    </div>
</body>
</html>
"""

# Ana Sayfa
@app.route('/')
def index():
    html = HTML_TEMPLATE.replace('{% block content %}', f'''
    <h2>📈 Sistem Özeti</h2>
    <div class="metrics">
        <div class="metric-card">
            <h3>{len(depo.tum_gozlukler())}</h3>
            <p>📦 Toplam Gözlük</p>
        </div>
        <div class="metric-card">
            <h3>{len(depo.musait_gozlukler())}</h3>
            <p>✅ Müsait Gözlük</p>
        </div>
        <div class="metric-card">
            <h3>{len(depo.tum_musteriler())}</h3>
            <p>👥 Kayıtlı Müşteri</p>
        </div>
        <div class="metric-card">
            <h3>{len(depo.aktif_kiralamalar())}</h3>
            <p>🔄 Aktif Kiralama</p>
        </div>
    </div>
    
    <div class="grid">
        <div class="card">
            <h3>👓 Müsait Gözlükler</h3>
            {''.join([f'<p><span class="badge badge-success">✓</span> [{g.id}] {g.marka} {g.model} - {g.gunluk_ucret:.2f} TL/gün</p>' for g in depo.musait_gozlukler()[:5]]) or '<p>Müsait gözlük yok</p>'}
        </div>
        <div class="card">
            <h3>🔄 Aktif Kiralamalar</h3>
            {''.join([f'<p><span class="badge badge-info">●</span> Kayıt #{k._kayit_id} - {k._musteri.ad_soyad}</p>' for k in depo.aktif_kiralamalar()[:5]]) or '<p>Aktif kiralama yok</p>'}
        </div>
    </div>
    ''').replace('{% endblock %}', '').replace("{{ 'active' if page == 'home' else '' }}", 'active')
    return render_template_string(html, page='home')

# Gözlükler
@app.route('/gozlukler', methods=['GET', 'POST'])
def gozlukler():
    if request.method == 'POST':
        marka = request.form.get('marka')
        model = request.form.get('model')
        ucret = float(request.form.get('ucret'))
        g = depo.gozluk_ekle(marka, model, ucret)
        flash(f'✅ Başarıyla eklendi! ID: {g.id} | {g.marka} {g.model}', 'success')
        return redirect(url_for('gozlukler'))
    
    liste = depo.tum_gozlukler()
    tablo = ''.join([
        f'<tr><td>{g.id}</td><td>{g.marka}</td><td>{g.model}</td><td>{g.gunluk_ucret:.2f} TL</td><td><span class="badge badge-{"success" if g.musait else "danger"}">{"✅ Müsait" if g.musait else "❌ Kirada"}</span></td></tr>'
        for g in liste
    ])
    
    html = HTML_TEMPLATE.replace('{% block content %}', f'''
    <h2>👓 Gözlük İşlemleri</h2>
    
    <div class="card" style="margin-bottom: 30px;">
        <h3>➕ Yeni Gözlük Ekle</h3>
        <form method="POST">
            <div class="grid">
                <div class="form-group">
                    <label>🏷️ Marka</label>
                    <input type="text" name="marka" placeholder="örn: Ray-Ban" required>
                </div>
                <div class="form-group">
                    <label>📦 Model</label>
                    <input type="text" name="model" placeholder="örn: Aviator" required>
                </div>
                <div class="form-group">
                    <label>💰 Günlük Ücret (TL)</label>
                    <input type="number" step="0.01" name="ucret" placeholder="30.00" required>
                </div>
            </div>
            <button type="submit" class="btn">✅ Gözlük Ekle</button>
        </form>
    </div>
    
    <h3>📋 Tüm Gözlükler ({len(liste)} adet)</h3>
    <table class="table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Marka</th>
                <th>Model</th>
                <th>Günlük Ücret</th>
                <th>Durum</th>
            </tr>
        </thead>
        <tbody>
            {tablo or '<tr><td colspan="5" style="text-align:center;">Henüz gözlük eklenmedi</td></tr>'}
        </tbody>
    </table>
    ''').replace('{% endblock %}', '').replace("{{ 'active' if page == 'gozlukler' else '' }}", 'active')
    return render_template_string(html, page='gozlukler')

# Müşteriler
@app.route('/musteriler', methods=['GET', 'POST'])
def musteriler():
    if request.method == 'POST':
        ad = request.form.get('ad')
        soyad = request.form.get('soyad')
        telefon = request.form.get('telefon')
        m = depo.musteri_ekle(ad, soyad, telefon)
        flash(f'✅ Başarıyla eklendi! ID: {m.id} | {m.ad_soyad}', 'success')
        return redirect(url_for('musteriler'))
    
    liste = depo.tum_musteriler()
    tablo = ''.join([
        f'<tr><td>{m.id}</td><td>{m.ad_soyad}</td><td>{m.telefon}</td></tr>'
        for m in liste
    ])
    
    html = HTML_TEMPLATE.replace('{% block content %}', f'''
    <h2>👤 Müşteri İşlemleri</h2>
    
    <div class="card" style="margin-bottom: 30px;">
        <h3>➕ Yeni Müşteri Ekle</h3>
        <form method="POST">
            <div class="grid">
                <div class="form-group">
                    <label>👤 Ad</label>
                    <input type="text" name="ad" placeholder="örn: Ahmet" required>
                </div>
                <div class="form-group">
                    <label>👤 Soyad</label>
                    <input type="text" name="soyad" placeholder="örn: Yılmaz" required>
                </div>
                <div class="form-group">
                    <label>📱 Telefon</label>
                    <input type="text" name="telefon" placeholder="örn: 0555-123-4567" required>
                </div>
            </div>
            <button type="submit" class="btn">✅ Müşteri Ekle</button>
        </form>
    </div>
    
    <h3>📋 Tüm Müşteriler ({len(liste)} kişi)</h3>
    <table class="table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Ad Soyad</th>
                <th>Telefon</th>
            </tr>
        </thead>
        <tbody>
            {tablo or '<tr><td colspan="3" style="text-align:center;">Henüz müşteri eklenmedi</td></tr>'}
        </tbody>
    </table>
    ''').replace('{% endblock %}', '').replace("{{ 'active' if page == 'musteriler' else '' }}", 'active')
    return render_template_string(html, page='musteriler')

# Kiralama
@app.route('/kiralama', methods=['GET', 'POST'])
def kiralama():
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'kirala':
            gid = int(request.form.get('gozluk_id'))
            mid = int(request.form.get('musteri_id'))
            gozluk = depo.gozluk_bul(gid)
            musteri = depo.musteri_bul(mid)
            
            try:
                k = depo.kiralama_baslat(musteri, gozluk)
                flash(f'✅ Kiralama başarıyla oluşturuldu! Kayıt #{k._kayit_id}', 'success')
            except ValueError as e:
                flash(f'❌ Hata: {e}', 'danger')
        
        elif action == 'iade':
            kid = int(request.form.get('kayit_id'))
            try:
                k = depo.kiralama_iade(kid)
                flash(f'✅ İade tamamlandı! Toplam ücret: {k.toplam_ucret():.2f} TL', 'success')
            except ValueError as e:
                flash(f'❌ Hata: {e}', 'danger')
        
        return redirect(url_for('kiralama'))
    
    musaitler = depo.musait_gozlukler()
    musteriler = depo.tum_musteriler()
    aktifler = depo.aktif_kiralamalar()
    
    gozluk_options = ''.join([f'<option value="{g.id}">[{g.id}] {g.marka} {g.model} ({g.gunluk_ucret:.2f} TL/gün)</option>' for g in musaitler])
    musteri_options = ''.join([f'<option value="{m.id}">[{m.id}] {m.ad_soyad} ({m.telefon})</option>' for m in musteriler])
    aktif_liste = ''.join([f'<p><span class="badge badge-info">●</span> Kayıt #{k._kayit_id} | {k._musteri.ad_soyad} → {k._gozluk.marka} {k._gozluk.model}</p>' for k in aktifler])
    
    html = HTML_TEMPLATE.replace('{% block content %}', f'''
    <h2>🔑 Kiralama İşlemleri</h2>
    
    <div class="grid">
        <div class="card">
            <h3>🔑 Gözlük Kirala</h3>
            {f'''
            <form method="POST">
                <input type="hidden" name="action" value="kirala">
                <div class="form-group">
                    <label>👓 Gözlük Seçin</label>
                    <select name="gozluk_id" required>
                        <option value="">Seçiniz...</option>
                        {gozluk_options}
                    </select>
                </div>
                <div class="form-group">
                    <label>👤 Müşteri Seçin</label>
                    <select name="musteri_id" required>
                        <option value="">Seçiniz...</option>
                        {musteri_options}
                    </select>
                </div>
                <button type="submit" class="btn">✅ Kiralamayı Başlat</button>
            </form>
            ''' if musaitler and musteriler else '<div class="alert alert-danger">❌ Müsait gözlük veya müşteri yok!</div>'}
        </div>
        
        <div class="card">
            <h3>↩️ İade Al</h3>
            {f'''
            <div style="margin-bottom: 20px;">
                <h4 style="font-size: 1rem; margin-bottom: 10px;">Aktif Kiralamalar:</h4>
                {aktif_liste}
            </div>
            <form method="POST">
                <input type="hidden" name="action" value="iade">
                <div class="form-group">
                    <label>📝 Kayıt Numarası</label>
                    <input type="number" name="kayit_id" placeholder="örn: 1" required>
                </div>
                <button type="submit" class="btn">✅ İade İşlemini Tamamla</button>
            </form>
            ''' if aktifler else '<div class="alert alert-info">⚠️ Aktif kiralama bulunmuyor</div>'}
        </div>
    </div>
    ''').replace('{% endblock %}', '').replace("{{ 'active' if page == 'kiralama' else '' }}", 'active')
    return render_template_string(html, page='kiralama')

# Raporlar
@app.route('/raporlar')
def raporlar():
    kayitlar = depo.tum_kayitlar()
    toplam_kazanc = sum(k.toplam_ucret() for k in kayitlar)
    aktif_sayisi = len(depo.aktif_kiralamalar())
    tamamlanan = len(kayitlar) - aktif_sayisi
    
    tablo = ''.join([
        f'<tr><td>{k._kayit_id}</td><td>{k._musteri.ad_soyad}</td><td>{k._gozluk.marka} {k._gozluk.model}</td>'
        f'<td>{k._baslangic}</td><td>{k._bitis or "Devam ediyor"}</td><td>{k.toplam_ucret():.2f} TL</td>'
        f'<td><span class="badge badge-{"info" if k.aktif_mi() else "success"}">{"🔄 Aktif" if k.aktif_mi() else "✅ Tamamlandı"}</span></td></tr>'
        for k in kayitlar
    ])
    
    html = HTML_TEMPLATE.replace('{% block content %}', f'''
    <h2>📊 Kiralama Geçmişi & Raporlar</h2>
    
    <div class="metrics">
        <div class="metric-card">
            <h3>{aktif_sayisi}</h3>
            <p>🔄 Aktif Kiralama</p>
        </div>
        <div class="metric-card">
            <h3>{tamamlanan}</h3>
            <p>✅ Tamamlanan</p>
        </div>
        <div class="metric-card">
            <h3>{len(kayitlar)}</h3>
            <p>📦 Toplam Kayıt</p>
        </div>
        <div class="metric-card">
            <h3>{toplam_kazanc:.2f} TL</h3>
            <p>💰 Toplam Kazanç</p>
        </div>
    </div>
    
    <h3>📋 Tüm Kiralama Kayıtları</h3>
    <table class="table">
        <thead>
            <tr>
                <th>Kayıt #</th>
                <th>Müşteri</th>
                <th>Gözlük</th>
                <th>Başlangıç</th>
                <th>Bitiş</th>
                <th>Ücret</th>
                <th>Durum</th>
            </tr>
        </thead>
        <tbody>
            {tablo or '<tr><td colspan="7" style="text-align:center;">Henüz kiralama kaydı yok</td></tr>'}
        </tbody>
    </table>
    ''').replace('{% endblock %}', '').replace("{{ 'active' if page == 'raporlar' else '' }}", 'active')
    return render_template_string(html, page='raporlar')

if __name__ == '__main__':
    print("=" * 60)
    print("   👓 ATASUN GÖZLÜK KİRALAMA SİSTEMİ")
    print("=" * 60)
    print("\n🌐 Web arayüzü başlatılıyor...")
    print("📱 Tarayıcınızda açın: http://127.0.0.1:5000")
    print("⏹️  Durdurmak için: CTRL+C")
    print("=" * 60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
