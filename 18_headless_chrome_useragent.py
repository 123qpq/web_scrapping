import requests
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True #여기서 user agent를 사용하면 그 주소에도 headless인 것이 표시되므로 막힐 수 있음
options.add_argument("window-size=1920x1080")
options.add_argument("")
#따라서 원래  chrme으로 들어갈 수 있도록 user agent 수정
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url