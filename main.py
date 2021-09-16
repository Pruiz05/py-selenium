import os
from selenium import webdriver

# set selenium env
os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
btn = driver.find_element_by_id('downloadButton')
btn.click()