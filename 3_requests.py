import requests
res = requests.get("http://google.com")
res.raise_for_status()

print(len(res.text))
print(res.text)

with open("google.html", "w", encoding="utf8") as f: 
    # with as 구문 : with 블록 내 프로그래밍 종료 후 파일과 연결된 부분들을
    #자동으로 해제해줌. 예외처리를 해주지 않아도 되는 장점을 가지고 있음.
    #프로그램 종료 후 리소스 낭비 또는 손실의 문제점 해소
    f.write(res.text)
    