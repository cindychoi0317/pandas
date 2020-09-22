import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

url ="https://search.tmon.co.kr/search/?keyword=%ED%8B%B0%ED%8C%8C%EB%8B%88%EC%95%A4%EC%BD%94&sortType=POPULAR"

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs ={"class": "item"})
title = items[0].a.get_text()

# for item in items:

#     name = item.find("strong", attrs={"class":"tx"}).get_text() #제품명
#     price = item.find("i", attrs={"class":"num"}).get_text() #가격
#     rate = item.find("span", attrs={"class":"grade_average_score"}).get_text() #평점
#     buy = item.find("span", attrs={"class":"buy_count"}).get_text() #구매 개수
#     freeshiping = item.find("span", attrs={"class":"text"}).get_text() #무료 배송
#     link = item.find("a",attrs={"class":"anchor"})["href"] #링크