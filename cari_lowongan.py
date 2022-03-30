from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://kasirpintar.co.id/careers/")
driver.maximize_window()
driver.implicitly_wait(0.5)
driver.find_element_by_id("posisi").send_keys("QA Automation Engineer")
driver.find_element_by_id("cari").click()
driver.quit()
