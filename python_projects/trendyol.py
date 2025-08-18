from bs4 import BeautifulSoup
import requests

url = input("Ürünün linkini giriniz: ")
sayfa = requests.get(url)
html_sayfa = BeautifulSoup(sayfa.content, "html.parser")

isim_etiket = html_sayfa.find("h1", class_="pr-new-br")
if isim_etiket:
    print("Ürün İsmi:", isim_etiket.getText())
else:
    print("Ürün ismi bulunamadı. Sayfa yapısı değişmiş olabilir.")

fiyat_etiket = html_sayfa.find("span", class_="prc-dsc")
if fiyat_etiket:
    print(f"Fiyat -> {fiyat_etiket.getText()}")
else:
    print("Fiyat bilgisi bulunamadı.")
