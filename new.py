from selenium import webdriver

url = "https://tms.tpf.go.tz"

web = webdriver.Chrome
web.get(url)

num = "T658DDA"

inp = driver.find_element_by_class_name("vehicle")
inp.send_keys(1)