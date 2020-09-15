import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/month/index.htm"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

musics = soup.find_all("div", attrs = {"class": "ellipsis rank01"})
title = musics[1].a.get_text()

artists = soup.find_all("div", attrs = {"class": "ellipsis rank02"})
#name = artists.a.get_text()

# print(name)

# for music in musics:
#     title = music.a.get_text()
#     print(title)

for artist in artists:
    name = artist.a.get_text()
    print(name)