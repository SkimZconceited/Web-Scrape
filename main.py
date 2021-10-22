from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)



def automatic(nums):
    driver.get("https://tms.tpf.go.tz/")
    print(driver.title)

    search = driver.find_element_by_name("vehicle")
    search.send_keys(nums)
    search.send_keys(Keys.RETURN)


    try:
        # tbdy = WebDriverWait(driver, 15).until(
        #     EC.presence_of_element_located((By.TAG_NAME, "tbody"))   
        # )
        #This was the wait progress of 
        
        tbdy = driver.find_element_by_tag_name("tbody")

        trows = tbdy.find_elements_by_tag_name("tr")
        
        for trow in trows:
            print(trow.text)

    finally:
        driver.quit()

# I just have to add a list that enters automatically after finishing one object
# Create a word document after the results
# stalled for a long time now I have to keep going.
#