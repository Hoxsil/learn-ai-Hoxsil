from selenium import webdriver
from selenium.webdriver.common.by import By
import time

wd = webdriver.Firefox()
time.sleep(3)
wd.implicitly_wait(10)

wd.get('https://www.byhy.net/cdn2/files/selenium/stock1.html')

elements = wd.find_elements(By.CLASS_NAME, 'name')
for element in elements:
    print(element.text)

input('按回车键退出')