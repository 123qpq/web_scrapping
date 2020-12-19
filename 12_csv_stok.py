import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)          #엑셀파일로 열 때 utf-8-sig로 입력해야 오류가 안남

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	".split("\t")

writer.writerow(title) #split : 문자열을 공백 혹은 어떠한 기준으로 나눌 때 사용하는 함수, 리스트에 요소로 저장됨

for page in range(1,2):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class" : "type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        colums = row.find_all("td")
        if len(colums) <= 1:
            continue
        data = [colum.get_text().strip() for colum in colums] #strip : 양끝에 공백과 기호들을 삭제시킴
                                                                #만약 안에 있는 기호들을 날릴려면 replace 함수 사용
        #print(data)
        writer.writerow(data)
        