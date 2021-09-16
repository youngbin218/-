import urllib.request as req
from bs4 import BeautifulSoup
import time

# 네이버 금융 정보 분석
url = "https://finance.naver.com/sise/"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

# 제목 가져오기
results_title = soup.select_one("h3.hpop > span.blind")
print(results_title.string, "\n")

# 인기 검색 종목 가져오기
results = soup.select("#popularItemList > li")

# 순위, 이름, 가격 가져오기
for result in results:
    print(result.select_one("em").string, end='')
    print(result.select_one("a").string)
    print(result.select_one("span").string)

    # 각 종목별 상세 정보 가져오기
    detail_url = "https://finance.naver.com" + result.select_one("a")["href"]
    detail_res = req.urlopen(detail_url)
    detail_soup = BeautifulSoup(detail_res, "html.parser")
    p = detail_soup.select_one("p.no_exday")
    em = p.find_all("em")

    # 전일대비 가격 변화
    change_text = em[0].find("span", "ico")
    price = em[0].find("span", "blind")
    
    # 가격 변화 % 표기
    change_mark = em[1].find("span", "ico")
    percent = em[1].find("span", "blind")

    # 출력
    print(change_text.string, price.string)
    if change_mark != None:
        print(change_mark.string, end='')
    print(percent.string, end='')
    print("%")
    print('''''')
    time.sleep(1)

