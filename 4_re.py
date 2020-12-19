import re

p = re.compile("ca.e") 
# . : 는 하나의 문자를 의미
# ^ : 문자열의 시작 / (^de) -> desk, deco ...
# $ : 문자열의 끝 / ($se) -> case, base ...
lst = p.findall("good care cafe") 
#match : 주어진 문자열이 '처음부터' 일치하는지 확인
#search : 주어진 문자열 중에 일치하는게 있는지 확인
#findall : 일치하는 모든 것을 "리스트" 형태로 반환


#group : 일치하는 문자열 반환
#string : 입력받은 문자열 반환
#start : 일치하는 문자열의 시작 index
#end : 일치하는 문자열의 끝 index
#span : 일치하는 문자열의 시작/끝 index
def print_match(m):
    if m:
        print(m.group())
        print(m.string())
    else:
        print("매칭되지 않음")

print(lst)



