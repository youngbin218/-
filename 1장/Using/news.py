import urllib.request
from bs4 import BeautifulSoup
import time

num = 1
url = "https://finance.naver.com/sise/lastsearch2.nhn"
res = urllib.request.urlopen(url)

soup = BeautifulSoup(res, "html.parser")
results = soup.select("td > a")

print("검색상위 종목\n")
for result in results:
    print (num, end='')
    print("순위")
    print(result.string)
    detail_url = "https://finance.naver.com" + result.attrs["href"]
    detail_res = urllib.request.urlopen(detail_url)
    detail = BeautifulSoup(detail_res, "html.parser")
    prices = detail.select_one("p.no_today span")
    print(prices.string)
    print('''''')
    num += 1
    time.sleep(1)
