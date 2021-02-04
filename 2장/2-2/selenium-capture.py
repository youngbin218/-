from selenium.webdriver import Firefox, FirefoxOptions

url = "http://www.naver.com"

options = FirefoxOptions()
options.add_argument('-headless')

browser = Firefox(options=options)

browser.get(url)

browser.save_screenshot("Website.png")

browser.quit()
