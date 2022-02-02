from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# driver_path = "/Users/hakansen/Documents/Development/chromedriver"
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie= driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time()+5

while True:
    cookie.click()

    if time.time() > timeout:
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#store b")

        list_upgrades = [upgrade.text.split("-")[1].strip().replace(",", "") for upgrade in upgrades if upgrade.text != "" ]
        print(list_upgrades)
