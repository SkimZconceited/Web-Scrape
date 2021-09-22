from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

num = "T 583 DEB"

driver.get("https://tms.tpf.go.tz/")
print(driver.title)

search = driver.find_element_by_name("vehicle")
search.send_keys(num)
search.send_keys(Keys.RETURN)


try:
    tbdy = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "tbody"))   
    )

    trows = tbdy.find_elements_by_tag_name("tr")
    
    for trow in trows:
        print(trow.text)


    #     theads = trow.find_elements_by_tag_name("th")
    #     for thead in theads:
    #         print(thead.text)

    # for trow in trows:
    #     tdets = trow.find_elements_by_tag_name("td")
    #     for tdet in tdets:
    #         print(tdets.text)
               
        

        # n = 0
        # while n < 12:
        #     # m = n
        #     # print(m)

        #     print(thead[n].text)
        #     print(tdets[n].text)

        #     n = n+1

finally:
    driver.quit()



# ref = driver.find_element_by_tag_name("th")
# print(ref.text)

# val = driver.find_element_by_tag_name("td")
# print(val.text)

# time.sleep(5)
# driver.quit()