from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()
driver.get("https://assertqa.com/practice/webtables/")

table_heading=driver.find_element(By.XPATH, "//*[@id='employees-table']/thead")
print("------ Table Heading ------")
print(table_heading.text)

first_data=driver.find_element(By.XPATH, "//*[@id='employees-table']/tbody/tr[1]")
print("------ First Data row ------")
print(first_data.text)

no_of_row=driver.find_element(By.XPATH, "//select[@aria-label='Rows per page']")
dropdown=Select(no_of_row)
row_value=input("Enter the rows value (5,10,15,25): ")
dropdown.select_by_value(row_value)

last_data=driver.find_element(By.XPATH, f"//*[@id='employees-table']/tbody/tr[{row_value}]")
print("------ Last Data row ------")
print(last_data.text)

search=driver.find_element(By.XPATH, "//input[@placeholder='Search by name, email...']")
last_name=input("Enter the last name: ")
search.send_keys(last_name)

searched_name=driver.find_element(By.XPATH, "//*[@id='employees-table']/tbody/tr")
print("------ Searched name ------")
print(searched_name.text)

time.sleep(3)

driver.refresh()

no_of_row=driver.find_element(By.XPATH, "//select[@aria-label='Rows per page']")
dropdown=Select(no_of_row)
row_value=input("Enter the rows value (5,10,15,25): ")
dropdown.select_by_value(row_value)

emails=driver.find_elements(By.XPATH, "//*[@id='employees-table']/tbody/tr/td[4]")
print("------ Email row ------")
for email in emails:
    print(email.text)

print("Website links exist : ")
links=driver.find_elements(By.TAG_NAME, "a")
if len(links)>0:
    print("Pass")
else:
    print("Failed")

total_row=driver.find_elements(By.XPATH, "//table[@id='employees-table']/tbody/tr")
print("Total row without header row: ",len(total_row))

input("Press enter to close...")
driver.quit()