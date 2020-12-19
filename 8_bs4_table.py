import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=748105"
res = requests.get(url)
res.raise_for_status()

#만화 제목, 링크, 평점 가져오기
soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class" : "title"})

for cartoon in cartoons:
   title = cartoon.a.get_text()
   link = "https://comic.naver.com" + cartoon.a["href"]
   rate = cartoon.find_next_sibling("td").strong.get_text()
   print(title, link, rate)
