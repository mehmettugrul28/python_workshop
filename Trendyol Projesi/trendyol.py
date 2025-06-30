from bs4 import BeautifulSoup
import requests

url = "https://www.trendyol.com/samsung/galaxy-s25-256-gb-buz-mavisi-cep-telefonu-samsung-turkiye-garantili-p-897494158?boutiqueId=61&merchantId=624588"
sayfa = requests.get(url)
html_sayfa = BeautifulSoup(sayfa.content , "html.parser")

isim = html_sayfa.find("h1",class_ = "pr-new-br").getText()
print(isim)
fiyat = html_sayfa.find("span",class_ = "prc-dsc").getText()
print(f"Fiyat -> {fiyat}")