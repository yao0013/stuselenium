from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
import threading

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print("这是设置的高度800*800")
driver.set_window_size(800,800)
driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()
driver.refresh()
driver.back()
driver.find_element_by_id("kw").send_keys("xiaozemaliya")
driver.find_element_by_id("su").submit()
driver.find_element_by_id("kw").clear()
right_click = driver.find_element_by_id("su")
ActionChains(driver).context_click(right_click).perform()
cookie = driver.get_cookies()
print(cookie)
js = "window.scrollTo(100,450);"
driver.execute_script(js)
sleep(3)
Keys.F5