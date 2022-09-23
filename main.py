

from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service

chrome_options=webdriver.ChromeOptions()
chrome_options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver=webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

driver.get("https://www.webmd.com/drugs/2/search?type=conditions&query=cough")
print(driver.title)


