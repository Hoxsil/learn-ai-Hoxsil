from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--start-maximized")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# 这两个保留，删掉 execute_cdp_cmd那一段（很多电脑会启动失败）
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# 先注释掉 options.add_argument("--disable-blink-features=AutomationControlled")
# wd.execute_cdp_cmd(...) 这整段注释！！

wd = webdriver.Chrome(options=options)

input("输入回车以退出")