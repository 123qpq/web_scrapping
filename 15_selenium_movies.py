import re
import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top?hl=ko"
headers = {"User-Agent" : ""}
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class" : "ImZGtf mpg5gc"})

for movie in movies:

    name = movie.find("div", attrs={"class" : "WsMG1c nnK0zc"}).get_text()
    print(f"영화 제목 : {name}")