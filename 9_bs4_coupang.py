import re
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent" : ""}
url = "https://www.coupang.com/np/search?component=&q=%ED%9C%B4%EB%8C%80%ED%8F%B0&channel=user"

res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class" : re.compile("search-product")})

for item in items:
    ad = item.find("span", attrs={"class" : "ad-badge-text"})
    if ad:
        print("광고입니다!!")
        continue

    name = item.find("div", attrs={"class" : "name"}).get_text() #제품
    price = item.find("strong", attrs={"class" : "price-value"}).get_text() #가격
    rate = item.find("em", attrs={"class" : "rating"}) #평점
    if rate:
        rate = rate.get_text() 
    else:
        rate = "평점없음"

    print(name, price, rate)


