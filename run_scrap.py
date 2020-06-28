from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

'''
Optional create GUI in which user can choose type of estate,location...

* in version 0.1 only new flats in one city *
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

'''
*** XPath ***
type of estates:

new_flats_menu = """//*[@id="guest-navigation-wrapper"]/ul/li[1]/ul/li[1]/div[1]/div/span"""
new_houses_menu = """//*[@id="guest-navigation-wrapper"]/ul/li[1]/ul/li[2]/div[1]/div/span"""
new_business_premises = """//*[@id="guest-navigation-wrapper"]/ul/li[1]/ul/li[3]/div[1]/div/span"""
'''

# find dropdown toggle with type of estates
xpath_estate_menu = """//*[@id="guest-navigation-wrapper"]/ul/li[1]"""
estates_menu = driver.find_element_by_xpath(xpath_estate_menu)
ActionChains(driver).move_to_element(estates_menu).perform()

# find new flats
xpath_new_flats_menu = """//*[@id="guest-navigation-wrapper"]/ul/li[1]/ul/li[1]/div[1]/div/span"""
new_flats_menu = driver.find_element_by_xpath(xpath_new_flats_menu)
ActionChains(driver).move_to_element(new_flats_menu).perform()

# find new flats in region
xpath_new_flats_in_region = """//*[@id="guest-navigation-wrapper"]/ul/li[1]/ul/li[1]/div[2]/ul/li[6]/a/span"""
new_flats_in_region = driver.find_element_by_xpath(xpath_new_flats_in_region)
ActionChains(driver).move_to_element(new_flats_in_region).perform()

# find new flats in city
xpath_new_flats_in_city = """//*[@id="guest-navigation-wrapper"]/ul/li[1]/ul/li[1]/div[2]/ul/li[6]/ul/li[1]/a"""
new_flats_in_city = driver.find_element_by_xpath(xpath_new_flats_in_city)
new_flats_in_city.click()

# click on background in due to hide any addition information
xpath_background = '''//*[@id="root"]/div[1]/main/article'''
background = driver.find_element_by_xpath(xpath_background)
background.click()