from selenium import webdriver #pip install selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver-manager
from selenium.webdriver.chrome.options import Options 
import time
import os

scriptDir = os.path.dirname (__file__)
os.chdir (scriptDir)
options = Options ()
options.add_argument("--headless=new")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome (service=service, options = options)
driver.get ("https://python.org")

driver.maximize_window ()

searchInput = driver.find_element (By.XPATH, '//*[@id="id-search-field"]')
searchInput.send_keys ("django")
buttonSubmit = driver.find_element (By.ID, "submit")
buttonSubmit.click ()

# viewport screenshot
#driver.save_screenshot ("python.org1.png")

# body screenshot
#driver.find_element (By.TAG_NAME, "body").screenshot ("python.org2.png")

func = lambda arg: driver.execute_script ("return document.body.parentNode.scroll" + arg)

driver.set_window_size (func ("Width"), func ("Height"))
driver.save_screenshot ("python.org3.png")

time.sleep (2)
driver.quit ()