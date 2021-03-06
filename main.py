import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set selenium env
os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")

driver.implicitly_wait(8)
btn = driver.find_element_by_id('downloadButton')
btn.click()

# progress_element = driver.find_element_by_class_name('progress-label')
# print(f"{progress_element.text == 'Completed!'}")

# explicit
WebDriverWait(driver, 30 ).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),  # Element fill
        'Complete!'  # the expected text
    )
)

# sending keys
