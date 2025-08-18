from flask import Flask, render_template, request, render_template_string
import csv
from datetime import datetime
import os

app = Flask(__name__)
csv_dosya = "/Users/mehmettugruldurmus/Documents/Github/workshops/Randevu Sistemi/randevu.csv"

@app.route("/")
def index():
    return render_template("randevu.html")

@app.route("/randevu", methods=["POST"])
def randevu_al():
    isim = request.form["isim"]
    saat = request.form["saat"]

    try:
        
        zaman = datetime.strptime(saat, "%H:%M")
        if zaman.minute not in [0, 30]:
            return render_template_string("""
                <h3>Geçersiz saat formatı. Lütfen sadece 30 dakikalık aralıklarla saat girin. (örn. 10:00, 10:30)</h3>
                <a href="/" style="display:inline-block; margin-top:10px; padding:8px 16px; background:#007BFF; color:white; text-decoration:none; border-radius:5px;">Ana Sayfa'ya Dön</a>
            """)

        
        dolu_saatler = set()
        if os.path.exists(csv_dosya):
            with open(csv_dosya, mode="r", newline="", encoding="utf-8") as dosya:
                okuyucu = csv.reader(dosya)
                for satir in okuyucu:
                    if len(satir) >= 2:
                        dolu_saatler.add(satir[1])

        if saat in dolu_saatler:
            return render_template_string(f"""
                <h3>{saat} saati zaten alınmış. Lütfen başka bir saat seçin.</h3>
                <a href="/" style="display:inline-block; margin-top:10px; padding:8px 16px; background:#007BFF; color:white; text-decoration:none; border-radius:5px;">Ana Sayfa'ya Dön</a>
            """)

        
        with open(csv_dosya, mode="a", newline="", encoding="utf-8") as dosya:
            yazici = csv.writer(dosya)
            yazici.writerow([isim, saat])

      
        randevular = []
        with open(csv_dosya, mode="r", newline="", encoding="utf-8") as dosya:
            okuyucu = csv.reader(dosya)
            for satir in okuyucu:
                if len(satir) >= 2:
                    randevular.append((satir[0], satir[1]))

       
        html_cevap = """
            <h3>Randevunuz başarıyla oluşturuldu: {{isim}} - {{saat}}</h3>
            <h4>Güncel Randevu Listesi:</h4>
            <table border="1" cellpadding="5" cellspacing="0">
                <tr><th>İsim</th><th>Saat</th></tr>
                {% for ad, zaman in randevular %}
                <tr><td>{{ad}}</td><td>{{zaman}}</td></tr>
                {% endfor %}
            </table>
            <a href="/" style="display:inline-block; margin-top:10px; padding:8px 16px; background:green; color:white; text-decoration:none; border-radius:5px;">Ana Sayfa'ya Dön</a>
        """
        return render_template_string(html_cevap, isim=isim, saat=saat, randevular=randevular)

    except ValueError:
        return render_template_string("""
            <h3>Geçersiz saat formatı.</h3>
            <a href="/" style="display:inline-block; margin-top:10px; padding:8px 16px; background:#007BFF; color:white; text-decoration:none; border-radius:5px;">Ana Sayfa'ya Dön</a>
        """)

if __name__ == "__main__":
    app.run(debug=True)
