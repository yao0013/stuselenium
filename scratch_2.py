from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


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
