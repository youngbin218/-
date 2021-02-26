import scrapy
from ..selenium_middleware import *

# 네이버 아이디, 비밀번호 지정
ID = "rldudqls02"
PW = "dufrhdgkwk!"

class GetMyStockSpider(scrapy.Spider):
    name = 'get_my_stock'

    # 미들웨어 등록
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES" : {
            "naver_stock.selenium_middleware.SeleniumMiddleware" : 0
        }
    }

    # 네이버 로그인
    def login(self):
        selenium_get("https://nid.naver.com/nidlogin.login")
        naver_ID = get_dom('.int [type=text]')
        naver_ID.send_keys(ID)
        naver_PW = get_dom('.int [type=password]')
        naver_PW.send_keys(PW)
        login_button = get_dom(".btn_global [type=submit]")
        login_button.click()

        # 마이 페이지 이동
        a = get_dom('li.m8 > a')
        mypage = a.get_atrribute('href')
        yield scrapy.Request(mypage, self,parse)

    def parse(self, response):
        my_stocks = response.css('.bx > table > tbody')
        for my_stock in my_stocks:
            stock_name = my_stock.css("frst _rt_cd_068270 _rt_an_SERVICE_ITEM point_dn a::text").extract_first()
            stock_price = my_stock.css("frst _rt_cd_068270 _rt_an_SERVICE_ITEM point_dn span.blind::text").extract_first()
            yield {
                "종목명" : stock_name,
                "현재가" : stock_price
            }
