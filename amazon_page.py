import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")

time.sleep(3)

account = driver.find_element(By.ID, "nav-link-accountList")
account.click()
# wait=WebDriverWait(driver, 10)

number=driver.find_element(By.ID, "ap_email_login")

number.send_keys("9363340535")

button=driver.find_element(By.CLASS_NAME, "a-button-input")
button.click()

time.sleep(10)

otp = input("Enter OTP: ")

otp_input = driver.find_element(By.XPATH, '//input[@id="cvf-input-code"]')

otp_input.send_keys(otp)

verify_otp = driver.find_element(By.CLASS_NAME, "a-button-input")

verify_otp.click()

print("Login Successfully")

search_item=input("Enter searching item: ")

search=driver.find_element(By.NAME, "field-keywords")

search.send_keys(search_item)
search.send_keys(Keys.ENTER)

products = driver.find_elements(By.CSS_SELECTOR, "[data-component-type='s-search-result']")

print("Products found:", len(products))

# Select first product
first_product = products[0]

first_product.click()

time.sleep(3)
cart=driver.find_element(By.XPATH, "//*[@id='ewc-cart-button-loaded-retail']/span/span/a")

cart.click()
time.sleep(3)
order=driver.find_element(By.NAME, "proceedToRetailCheckout")

order.click()
'''
deliver=driver.find_element(By.XPATH, "//*[@id='add-new-address-desktop-sasp-tango-link']/span/a")

deliver.click()

driver.find_element(By.XPATH, "//*[@id='address-ui-widgets-enterAddressFullName']").send_keys("Priyadharshini")

driver.find_element(By.XPATH, "//*[@id='address-ui-widgets-enterAddressPhoneNumber']").send_keys("9876543210")

driver.find_element(By.XPATH, "//*[@id='address-ui-widgets-enterAddressLine1']").send_keys("123,ABC street, xyz district")
'''

input("Enter to close...")

driver.quit()