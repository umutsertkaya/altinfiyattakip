import requests
from bs4 import BeautifulSoup
Url = "https://uzmanpara.milliyet.com.tr/gram-altin-fiyati/"
headers = {"useragent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

def sorgula():
    bag = requests.get(Url)
    veri = bag.content
    ayr = BeautifulSoup(veri,"html.parser")
    alt = ayr.find(id= "gld_header_son_data")
    print(f"Gram Altın son fiyat {alt.text} TL")
    
sorgula()