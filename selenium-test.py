from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument('--no-sandbox')
driver = webdriver.Chrome('./chromedriver', options=options)
driver.get('http://dev04.avlino.bw')
try:
    print('Page Title: ' + driver.title)
except AssertionError:
    print('TEST FAILED')
else:
    print(driver.title)
    print(driver.current_url)
    el = driver.find_element_by_css_selector('h3')
    print(el.text)

driver.close()