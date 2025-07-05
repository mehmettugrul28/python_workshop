from bs4 import BeautifulSoup
import requests

url = input("Ürünün linkini giriniz: ")
sayfa = requests.get(url)
html_sayfa = BeautifulSoup(sayfa.content , "html.parser")

isim = html_sayfa.find("h1",class_ = "pr-new-br").getText()
print(isim)
fiyat = html_sayfa.find("span",class_ = "prc-dsc").getText()
print(f"Fiyat -> {fiyat}")