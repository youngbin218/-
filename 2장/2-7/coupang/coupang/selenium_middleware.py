from scrapy.http import HtmlResponse
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = FirefoxOptions()
options.add_argument('-headless')
driver = Firefox(options=options)

def selenium_get(url):
    driver.get(url)

def get_dom(query):
    dom = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, query)))
    return dom

def selenium_close():
    driver.close()

class SeleniumMiddleware(object):
    def process_request(self, response, spider):
        driver.get(request.url)
        return HtmlResponse(
            driver.current_url,
            body = driver.page_source,
            encoding = 'utf-8',
            request = request)
