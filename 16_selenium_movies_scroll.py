import requests
from bs4 import BeautifulSoup
from selenium import webdriver
browser = webdriver.Chrome()
#browser.maximize_window()

#페이지 이동
url = "https://play.google.com/store/movies/top?hl=ko"
browser.get(url)

#지정한 위치로 스크롤 내리기/java
#browser.execute_script("window.scrollTo(0,2080)") #모니터 높이인 1080만큼

#화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

import time
interval = 3
prev_height = browser.execute_script("return document.body.scrollHeight")


while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(interval)
    #현재 문서 높이 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height


soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs={"class" : "Vpfmgd"})



for movie in movies:
 
    original_price = movie.find("span" , attrs={"class" : "SUZt4c djCuy"})

    if original_price:
        original_price = original_price.get_text()
    else:
        continue

    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    dis_price = movie.find("span" , attrs={"class" : "VfPpfd ZdBevf i5DZme"}).get_text()
    link = movie.find("a", attrs={"class" : "JC71ub"})["href"]
    print(f"할인 영화 : {title} \n 할인가 : {original_price} -> {dis_price}")
    print("영화 링크 : ", "https://play.google.com" + link)
    print("-"*80)







