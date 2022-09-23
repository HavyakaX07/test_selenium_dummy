

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
var =driver.title()

from flask import Flask

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'+str(var)


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

