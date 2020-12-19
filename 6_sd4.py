import requests
from bs4 import BeautifulSoup #beautifulsoup 관련 정보 :https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") #res.text 파일을 lxml 로 파서 시켜서 BeautifulSoup객체로 만든 것

#print(soup.a) : soup 객체에서 처음 발견되는 a element 반환
#print(soup.a.attrs) : a element 의 속성 정보를 출력
#print(soup.a["href"]) : a element 의 herf  속성 값 정보를 출력
#print(soup.find("a", attrs={"class" : "Nbtn_uplkoad"})) : class="Nbtn_uplkoad" 인 a element 를 검색
rank1 = soup.find("li", attrs={"class" : "rank01"})
print(rank1.a.get_text()) # rank1의 a테그의 글자를 가져옴
#next_sibling : 다음 형제객체 / previous_sibling : 이전 형제객체
#parent : 부모객체
rank2 = rank1.find_next_sibling("li") #rank1의 다음 형제객체를 끌어옴
print(rank2.a.get_text())
print(rank1.find_next_siblings("li")) #rank1의 형제객체들 싹다 끌어옴


#원하는 회차의 html 정보 가져오기
# webtoon = soup.find("a", text = "전지적 독자 시점-017. Ep.04 위선도 선이다 (2)")
# print(webtoon)