from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com/login?signup=true&ret=/")

wait = WebDriverWait(driver, 10)

number = "9363340535"

number_input = wait.until(EC.presence_of_element_located((By.ID, "1")))

number_input.send_keys(number)

button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))

button.click()

otp = input("Enter OTP: ")

otp_input=driver.find_elements(By.CLASS_NAME, "S1KmoO")
for i in range(6):
    otp_input[i].send_keys(otp[i])

verify_otp = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Verify']")))
verify_otp.click()

print("Login Sucessfully")

input("Wait until i press the enter....")
driver.quit()