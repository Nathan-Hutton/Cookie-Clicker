from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:\important\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, 'cookie')
end_time = time.time() + 300

while time.time() < end_time:
    check_time = time.time() + 5
    while time.time() < check_time:
        cookie.click()
    right_rows = driver.find_elements(By.CSS_SELECTOR, "#rightPanel b")
    right_rows.pop()
    for row in reversed(right_rows):
        money = driver.find_element(By.ID, 'money').text
        money = int(money.replace(',', ''))
        price = (row.text.split()[-1])
        price = int(price.replace(",", ''))
        if price < money:
            row.click()
            break

