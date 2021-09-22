from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

num = "* ### ***"

driver.get("https://tms.tpf.go.tz/")
print(driver.title)

search = driver.find_element_by_name("vehicle")
search.send_keys(num)
search.send_keys(Keys.RETURN)

# ref = driver.find_element_by_tag_name("th")
# print(ref.text)

# val = driver.find_element_by_tag_name("td")
# print(val.text)

try:
    tbdy = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "tbody"))
    )
except:
    driver.quit()

print(tbdy.text)

# time.sleep(5)

# driver.quit()