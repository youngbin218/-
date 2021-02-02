import requests
r = requests.get("http://wikibook.co.kr/logo.png")

with open("test.png", "wb") as f:
    f.write(r.content)

print("saved")
