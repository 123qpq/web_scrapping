import requests
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions() #크롬을 직접 띄우지 않고 백그라운드에서 작업을 실행시킴
options.headless = True
options.add_argument("window-size=1920x1080") #내 모니터 크기 지정
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies/top?hl=ko"
browser.get(url)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")


import time
interval = 3
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height


browser.get_screenshot_as_file("google_movie.png") #프로그램 동작상태 확인을 위한 스크린샷
    

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







