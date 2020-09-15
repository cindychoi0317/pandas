import re
# abcd, book, desk
#ca?e
#care, cafe, case, cave

p = re.compile("ca.e") 
#. (ca.e): 하나의 문자를 의미 > care, cafe, case는 됨 | caffe는 안 됨
#^ (^de): 문자열의 시작을 의미 > desk, destination은 됨 | fade는 안 됨
#$ (se$): 문자열의 끝을 의미 > case, base은 됨 | face는 안 됨

def print_match(m):
    #print(m.group()) #매치되지 않으면 에러 발생
    if m:
        print("m.group()", m.group()) #group은 일치하는 문자열 반환
        print("m.string", m.string) #string은 입력받은 문자열 그대로 반환
        print("m.start()", m.start()) #start는 일치하는 문자열의 시작 index
        print("m.end()", m.end()) #end는 일치하는 문자열의 끝 index
        print("m.span()", m.span()) #span은 일치하는 문자열의 시작과 끝 index
    else:
        print("매칭되지 않았습니다")

#m = p.match("careless") #주어진 문자열의 처음부터 일치하는지 확인
#print_match(m) 

#m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
#print_match(m) 

#list = p.findall("good care cafe") #findall 일치하는 모든 것을 리스트 형태로 반환
#print(list)


#1. p = re.compile("원하는 형태")
#2. m = p.match("비교할 문자열")
#3. m = p.search("비교할 문자열")
#4. list = p.findall("비교할 문자열")

#원하는 형태 : 정규식
#. (ca.e): 하나의 문자를 의미 > care, cafe, case는 됨 | caffe는 안 됨
#^ (^de): 문자열의 시작을 의미 > desk, destination은 됨 | fade는 안 됨
#$ (se$): 문자열의 끝을 의미 > case, base은 됨 | face는 안 됨