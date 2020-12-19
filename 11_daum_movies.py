import requests
from bs4 import BeautifulSoup
url = "https://search.daum.net/search?w=tot&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class" : "thumb_img"})


for idx, image in enumerate(images): # enumerate : ,앞에 있는 변수에 몇번째 image인지 카운트 해줌
    
    image_url = image["src"]
    if image_url.startswith("//"): #startwith 시작문자열이 "//"이면 true 반환
        image_url = "https:" + image_url

    print(image_url)
    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open("movie{}.jpg".format(idx + 1), "wb") as f: #위에서 인덱스 당겨와서 이름에 사용. wb인 이유는 이미지이므로 바이트형태로 날아옴
        f.write(image_res.content) #content는 여기서는 이미지를 의미. 파일에 쓰는작업

    if idx >= 4:
        break

