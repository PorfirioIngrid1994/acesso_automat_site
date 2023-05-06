from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.linguee.com.br/")

search_bar = driver.find_element_by_name("query")
search_bar.send_keys("chuva")
search_bar.send_keys(Keys.RETURN)

first_block = driver.find_element_by_class_name("dictLink")
print(first_block.text)

driver.quit()
