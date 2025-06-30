import requests
from bs4 import BeautifulSoup

def googlefinance(birim):
    url = f"https://www.google.com/finance/quote/{birim}-TRY?hl=tr"
    try:
        page = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        htmlPage = BeautifulSoup(page.content, "html.parser")
        
        # Değerin bulunduğu div'in class'ı doğruysa al:
        actualvalue = htmlPage.find("div", class_="YMlKec fxKbKc").getText()
        
        # Simgeleri temizleyip sayıya çevir
        actualvalue = actualvalue.replace("₺", "").replace(",", ".").strip()
        actualduzenle = round(float(actualvalue), 2)
        
        return actualduzenle

    except Exception as e:
        print("Bir hata oluştu:", e)
        return None

# Örnek kullanım:
kur = googlefinance("USD")
if kur:
    print("Güncel USD kuru:", kur)
