import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.ID, "user-name").send_keys("visual_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
driver.find_element(By.ID, "shopping_cart_container").click()
time.sleep(2)

driver.find_element(By.ID, "checkout").click()

driver.find_element(By.ID, "first-name").send_keys("oluwaseun")
driver.find_element(By.ID, "last-name").send_keys("Adio")
driver.find_element(By.ID, "postal-code").send_keys("234")
driver.find_element(By.ID, "continue").click()
time.sleep(2)

driver.find_element(By.ID, "finish").click()
time.sleep(2)

driver.find_element(By.ID, "back-to-products").click()
time.sleep(2)


