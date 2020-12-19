import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

filename = "네이버항공권 검색결과.csv" #내가추가 : 검색결과를 엑셀파일로 만듦
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

browser = webdriver.Chrome()
browser.maximize_window()#창 최대화
browser.get("https://flight.naver.com/flights/") 

browser.find_element_by_link_text("가는날 선택").click()
browser.find_elements_by_link_text("27")[0].click() # [0} -> 이번달
browser.find_elements_by_link_text("28")[1].click() 

#제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()
#항공권 검색
browser.find_element_by_link_text("항공권 검색").click()

#browser.implicitly_wait(10) : html 페이지 전체가 뜨는 동안 기다림. 마지노선 10초
try:
    for i in range(1,11):
        elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[{}]".format(i)))).text.split("\n")
        # 위 코드는 html 전체가 뜨는 시간을 기다리는 것이 아니라 내가 필요한 정보(xpath)만 뜨면 바로 접속함. 마지노선이 10라는 것

        #print(elem)
        writer.writerow(elem)
    f.close()


finally:
    browser.quit()

