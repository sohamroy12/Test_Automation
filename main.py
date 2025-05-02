from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager
from selenium.webdriver.common.by import By
import time


# Custom path to install ChromeDriver (adjust this as needed)
custom_driver_path = r"D:\Udemy Courses\Pyhton\Udemy\Python Mega Course\2025\Test_Automation\Drivers\chromedriver"
print(custom_driver_path)
cache_manager=DriverCacheManager(custom_driver_path)

# Use webdriver-manager to download and install to custom path
# service = Service(ChromeDriverManager(path=custom_driver_path).install())
# chrome_browser = webdriver.Chrome(service=service)
chrome_browser = webdriver.Chrome(service=Service(ChromeDriverManager(cache_manager=cache_manager).install()))
print(chrome_browser)
chrome_browser.get('https://omayo.blogspot.com/')
# chrome_browser.maximize_window()
# sleep(30)
assert 'Button X' in chrome_browser.page_source
drop1 = chrome_browser.find_element(By.ID, 'drop1')
# drop1.clear()
drop1.send_keys('doc 1')

chrome_browser.quit()

