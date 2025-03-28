import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# variable declaration
URL = "https://www.saucedemo.com/"
Time = 2

#initializing browser
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()

# Fill the login details
driver.find_element(By.ID, "user-name").send_keys("visual_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(Time)

# Add products to carts
Backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
BikeLight = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
BoltTShirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
FleeceJacket = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
labsOniese = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
RedTshirt = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
CartContainer = driver.find_element(By.ID, "shopping_cart_container").click()
time.sleep(Time)

# Proceed to checkout
driver.find_element(By.ID, "checkout").click()

# Fill customer information
FirstName = driver.find_element(By.ID, "first-name").send_keys("oluwaseun")
LastName = driver.find_element(By.ID, "last-name").send_keys("Adio")
PostalCode = driver.find_element(By.ID, "postal-code").send_keys("234")
Continuing = driver.find_element(By.ID, "continue").click()
time.sleep(Time)

# Complete order
driver.find_element(By.ID, "finish").click()
time.sleep(Time)

driver.find_element(By.ID, "back-to-products").click()
time.sleep(Time)


