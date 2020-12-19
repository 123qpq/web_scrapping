import re
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent" : ""}

for i in range(1, 3): #원하는 페이지 수
    url = "https://www.coupang.com/np/search?q=%ED%9C%B4%EB%8C%80%ED%8F%B0&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)
    print("페이지 : ", i)
    print("-"*100)
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class" : re.compile("search-product")})

    for item in items:
        
        ad = item.find("span", attrs={"class" : "ad-badge-text"}) #광고 제외
        if ad: 
            continue

        name = item.find("div", attrs={"class" : "name"}).get_text() #제품
        price = item.find("strong", attrs={"class" : "price-value"}).get_text() #가격
        rate = item.find("em", attrs={"class" : "rating"}) #평점
        if rate: #평점 없을 경우 패스
            rate = rate.get_text() 
        else:
            continue

        link = "https://www.coupang.com" + item.a["href"] #링크 첨부
        

        if float(rate) >= 4.5:
            print(f"제품 명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}")
            print(f"링크 : {link}")
            print("-"*100)


