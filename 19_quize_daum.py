import requests
from bs4 import BeautifulSoup
from selenium import webdriver
browser = webdriver.Chrome()
import time

url = "https://www.daum.net/"
browser.get(url)


search = "송파 헬리오시티"

browser.find_element_by_xpath("//*[@id='q']").send_keys(search)
browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]").click()

soup = BeautifulSoup(browser.page_source, "lxml")
data_row = soup.find("div", attrs={"class" : "wrap_tbl tbl_trade"}).find("tbody").find_all("tr")


for idx, row in enumerate(data_row):
    colums = row.find_all("td")
    data = [colum.get_text().strip() for colum in colums]
    print("="*10, "매물", idx+1, "="*10)
    print(f" 거래 : {data[0]} \n 공급/전용면적 : {data[1]} \n 매물가 : {data[2]} (만원) \n 동 : {data[3]} \n 층 : {data[4]}")




