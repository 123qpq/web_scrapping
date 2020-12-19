import requests
url = "https://comic.naver.com/index.nhn"
headers = {"User-Agent" : ""}
res = requests.get(url, headers = headers)
res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf8") as f: 
    f.write(res.text)
    