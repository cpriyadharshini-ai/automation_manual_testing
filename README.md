# CHANDRAPRIYADHARSHINI C
# 212223240019
<h1>Automation Manual Testing</h1>

# Task-1 (19/09/2026):
Collect the test cases from justdial e-commerce site. 

### Excel sheet:
[View the manual testing XL sheet](https://docs.google.com/spreadsheets/d/1JtfcjQH9tnJ2aiikcJcehL1i27EZg3J2KPaOjPG2OOw/edit?usp=sharing)

# Task-2 (22/09/2026):
Find the test cases and valid and invalid input from given exercises.

### Excel sheet:
[View the test cases from given exercises XL sheet](https://docs.google.com/spreadsheets/d/1JtfcjQH9tnJ2aiikcJcehL1i27EZg3J2KPaOjPG2OOw/edit?usp=sharing)

# Task-3 (23/09/2026):
Python problem: Write the python code within 15 minutes.

### Python file:
[View the python file](python_code.py)

# Task-4 (24/09/2026):
Test metrics & analyze the tests.

### Report file:
[Test metrics & analysis report](https://docs.google.com/spreadsheets/d/1JtfcjQH9tnJ2aiikcJcehL1i27EZg3J2KPaOjPG2OOw/edit?gid=1008736792#gid=1008736792)

# Task-5 (25/09/2026):
Python problem: Write the python code to 10 real world problems.

### Python file:
[View the python file](python_practice_problem.py)

# Task-6 (25\9/09/2026):
Python assignment: Solve python and numpy problems.

### Python file:
[View the python file](python_assignments.py)<br><br><br>
[View the python file (using function)](funtion_assignment.py)

# Task-7 (05/10/2026)
Write the selenium code to login the flipkart login page using python.

### Python file:
[View the selenium Webdriver code](Selenium_webdriver_code.docx)

## Python code
```
SELENIUM WEBDRIVER
CHANDRAPRIYADHARSHINI C
212223240019
```
1.	Automating Google search using Selenium WebDriver with Python code.
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://www.google.com/")

search=driver.find_element(By.ID, "ti6dpd")
search.send_keys("actor surya")
print(search.is_enabled())
search.send_keys(Keys.ENTER)

input("Enter to close the browser...")

driver.quit()
```
2.	Automating search for all products by using .find_elements() keyword.
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://sweetshop.netlify.app/")

products_name=driver.find_elements(By.CLASS_NAME, "card-title")
price_name=driver.find_elements(By.CLASS_NAME, "text-muted")

print("Product details")
for product,price in zip(products_name,price_name):
    print(f"{product.text} -> {price.text}")

'''
USING ARRAY
for i in range(len(products_name)):
    print(f"{products_name[i].text} -> {price[i].text}")
'''
'''
print("Product name")
for product in products_name:
    print(product.text)
print("Price details name")
for price in price_name:
    print(price.text)
'''
input("Enter to close the browser...")

driver.quit()	
```
3.	Automating login and verifying the OTP on the Flipkart website.
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com/")

wait=WebDriverWait(driver, 10)

number_input=wait.until(EC.presence_of_element_located((By.ID, "1")))

number_input.send_keys("9363340535")

button=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))
button.click()

otp=input("Enter OTP: ")

otp_input=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "S1KmoO")))

for i in range(6):
    otp_input[i].send_keys(otp[i])

verify_otp=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Verify']")))

verify_otp.click()

print("Login Successfully")

input("Press Enter to close...")
driver.quit()
```

# Task-8 (06/10/2026)
Write the selenium code to fill out the registration form using python.

### Python file:
[View the selenium registration form code](registration_form.py)

# Task-9
Write the selenium code to order process in amazon application using python.

### Python file:
[View the selenium order process code](amazon_page.py)

# Result
This readme contains only Automation Testing practice exersices.
