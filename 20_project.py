import re
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("오늘의 날씨")
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=날씨"
    soup = create_soup(url)


    cast = soup.find("p", attrs={"class" : "cast_txt"}).get_text()

    temp = soup.find("span", attrs={"class" : "todaytemp"}).get_text()
    temp_mm = soup.find("span", attrs={"class" : "merge"}).get_text()
    sensible = soup.find("span", attrs={"class" : "sensible"}).get_text()

    indicator = soup.find("dl", attrs={"class" : "indicator"})
    pm10 = indicator.find_all("dd")[0].get_text()
    pm25 = indicator.find_all("dd")[1].get_text()


    rain_mor = soup.find("span", attrs={"class" : "point_time morning"}).get_text().strip()
    rain_aft = soup.find("span", attrs={"class" : "point_time afternoon"}).get_text().strip()

    print(f"기온 : {temp}℃ ({temp_mm}) {sensible} \n {cast}")
    print(f"미세먼지 : {pm10}, 초미세먼지 : {pm25}")
    print(f"{rain_mor}/{rain_aft}")
    
    



def news():
    print("<<오늘의 헤드라인>>")
    url = "https://news.naver.com/"
    soup = create_soup(url)
    heads = soup.find("ul", attrs={"class" : "hdline_article_list"}).find_all("li", limit=3)#all 찾는 것에 limit 을 사용해 갯수를 한정시킬 수 있다.
    
    for idx, head in enumerate(heads):
        hdline = head.find("div", attrs={"class" : "hdline_article_tit"}).get_text().strip()
        hdlink = "https://news.naver.com" + head.a["href"]

        print(idx+1, hdline)
        print(f"링크 : {hdlink}")

def themenews():
    print("<<오늘의 경제뉴스>>")
    url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=101"
    soup = create_soup(url)
    heads = soup.find("ul", attrs={"class" : "type06_headline"}).find_all("li", limit=5)#all 찾는 것에 limit 을 사용해 갯수를 한정시킬 수 있다.

    for idx, head in enumerate(heads):

        a_idx = 0 #이미지가 있으면 li의 첫번째 a태그 사용, 아니면 두번째[1] 태그 사용
        img = head.find("img")
        if img:
            a_idx = 1

        a_tag = head.find_all("a")[a_idx]
        hdline = a_tag.get_text().strip()
        hdlink = a_tag["href"]

        print(idx+1, hdline)
        print(f"링크 : {hdlink}")

def english():
    print("<<오늘의 영어회화>>")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    contexts = soup.find_all("div", attrs={"id" : re.compile("^conv_kor_t")})#비교문 쓸 때 re.compile 써주기!, import re 도 필요

    lengths = len(contexts)

    print("<<영어지문>>")
    for context in contexts[lengths//2:]: #리스트형태로 반환시켜 원하는 만큼만 가져온다!
        print(context.get_text().strip())
    print("<<한글지문>>")
    for context in contexts[:lengths//2]:
        print(context.get_text().strip())




if __name__ == "__main__":
    scrape_weather()
    news()
    themenews()
    english()