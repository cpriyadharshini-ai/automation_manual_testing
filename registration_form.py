import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains # it is used to perform mouse actions

driver=webdriver.Chrome()
driver.get("https://vinothqaacademy.com/demo-site/")

time.sleep(10)

driver.find_element(By.NAME, "vfb-5").send_keys("Chandrapriyadharshini") #first name
driver.find_element(By.NAME, "vfb-7").send_keys("C") #last name

#gender
female=driver.find_element(By.ID, "vfb-31-2") 
if not female.is_selected():
    female.click()

#Course interested
selenium_webdriver=driver.find_element(By.ID, "vfb-20-0")
if not selenium_webdriver.is_selected():
    selenium_webdriver.click()

java=driver.find_element(By.ID, "vfb-20-1")
if not java.is_selected():
    java.click()

testing=driver.find_element(By.ID, "vfb-20-2")
if not testing.is_selected():
    testing.click()

deveops=driver.find_element(By.ID, "vfb-20-3")
if deveops.is_selected():
    deveops.click()

#Address
driver.find_element(By.NAME, "vfb-13[address]").send_keys("123, ABC street, xyz district")
driver.find_element(By.NAME, "vfb-13[city]").send_keys("Chennai")

driver.find_element(By.NAME, "vfb-14").send_keys("saveetha2023@gmail.com")

driver.find_element(By.NAME, "vfb-19").send_keys("9876543210")

driver.find_element(By.NAME, "vfb-23").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")

driver.find_element(By.NAME, "vfb-3").send_keys("77")

submit=driver.find_element(By.ID, "vfb-4")

time.sleep(4)

ActionChains(driver).move_to_element(submit).click().perform()

input("Entet to close...")

driver.quit()