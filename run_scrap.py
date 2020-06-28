from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

'''
Optional create GUI in which user can choose type of estate,location...

* in version 0.1 only new flats in Warsaw *
'''

# browser settings
chrome_options = Options()
chrome_options.add_argument('start-maximized')

# local path to chrome webdriver (chromedriver.exe)
browser = r'C:\\Users\\Tomek\\.wdm\\drivers\\chromedriver\\83.0.4103.39\\win32\\chromedriver.exe'
driver = webdriver.Chrome(browser, chrome_options=chrome_options)

# go to site
# driver.implicitly_wait(10) # seconds - optional - can turn off
driver.get("https://rynekpierwotny.pl/")
# assertion to confirm that title has "RynekPierwotny" word in it
assert "RynekPierwotny" in driver.title