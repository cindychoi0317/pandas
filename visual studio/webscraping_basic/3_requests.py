import requests
res = requests.get("http://google.com") #200 나오면 정상
#res = requests.get("http://nadocoading.tistory.com") #404 나오면 비정상
res.raise_for_status()
#print("응답코드 : ", res.status_code)

if res.status_code == requests.codes.ok: #requests.codes.ok는 200이랑 같다?
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")



#print("웹 스크래핑을 진행합니다")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)