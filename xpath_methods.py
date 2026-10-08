from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
wait=WebDriverWait(driver, 10)

driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Chandrapriyadharshini")

driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Chandrabose")

driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[2]/div/textarea").send_keys("123, ABC street, xyz district")

driver.find_element(By.XPATH, "//input[@type='email']").send_keys("priyadharshinibose86@gmail.com")

driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("9876543210")

female=driver.find_element(By.XPATH, "//input[@name='radiooptions']")
if not female.is_selected():
    female.click()

driver.find_element(By.XPATH, "//input[@value='Cricket']").click()
driver.find_element(By.XPATH, "//input[@value='Movies']").click()

skills=driver.find_element(By.XPATH, "//select[@id='Skills']")
dropdown=Select(skills)
dropdown.select_by_value("HTML")

driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[10]/div/span/span[1]/span").click()
country=driver.find_element(By.XPATH, "//input[@class='select2-search__field']")
country.send_keys("India")
country.send_keys(Keys.ENTER)

year=driver.find_element(By.XPATH, "//select[@id='yearbox']")
year=Select(year)
year.select_by_visible_text("2006")

month=driver.find_element(By.XPATH, "//select[@placeholder='Month']")
month=Select(month)
month.select_by_visible_text("July")

day=driver.find_element(By.XPATH, "//select[@id='daybox']")
day=Select(day)
day.select_by_visible_text("17")

driver.find_element(By.XPATH, "//input[@id='firstpassword']").send_keys("sdf@#$123")

driver.find_element(By.XPATH, "//input[@id='secondpassword']").send_keys("sdf@#$123")

driver.find_element(By.XPATH, "//button[text()=' Submit ']").click()

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Refresh']"))).click()

input("Wait to press the enter key....")
driver.quit()