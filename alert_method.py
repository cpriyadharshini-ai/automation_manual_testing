import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/alerts.html")

wait=WebDriverWait(driver, 10)

time.sleep(3)
#simple alert
alert=driver.find_element(By.ID, "alert")
alert.click()
message=wait.until(EC.alert_is_present())
print(message.text)
message.accept()
time.sleep(3)

#empty alert
alert=driver.find_element(By.ID, "empty-alert")
alert.click()
message=wait.until(EC.alert_is_present())
print(message.text)
message.accept()
time.sleep(3)

#prompt
driver.find_element(By.ID, "prompt").click()
alert=wait.until(EC.alert_is_present())
print("\nPrompt text: ")
print(alert.text)
alert.send_keys("Chandra")
alert.accept()
time.sleep(3)

#slow alert
driver.find_element(By.ID, "slow-alert").click()
text=wait.until(EC.alert_is_present())
print(text.text)
text.accept()
time.sleep(3)

#confirmation alert
driver.find_element(By.ID, "confirm").click()
message=wait.until(EC.alert_is_present())
print(message.text)
message.accept()
driver.back()
time.sleep(3)

#iframe dialog box
iframe = driver.find_element(By.NAME, "iframeWithAlert")
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH, "//*[@id='alertInFrame']").click()
iframe_message=wait.until(EC.alert_is_present())
print(iframe_message.text)
iframe_message.accept()
driver.switch_to.default_content()
time.sleep(3)

#nested iframe dialog box
nest = driver.find_element(By.NAME, "iframeWithIframe")
driver.switch_to.frame(nest)
nested = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(nested)
driver.find_element(By.XPATH, "//*[@id='alertInFrame']").click()
nested_iframe_message=wait.until(EC.alert_is_present())
print(nested_iframe_message.text)
nested_iframe_message.accept()
driver.switch_to.default_content()
time.sleep(3)

#Open new page
driver.find_element(By.ID, "open-page-with-onload-alert").click()
new_page=wait.until(EC.alert_is_present())
print(new_page.text)
new_page.accept()
driver.back()
wait.until(EC.presence_of_element_located((By.ID, "open-window-with-onload-alert")))

'''
# Open new window
original_window = driver.current_window_handle
driver.find_element(By.ID, "open-window-with-onload-alert").click()
wait.until(EC.number_of_windows_to_be(2))
for window in driver.window_handles:
    if window != original_window:
        driver.switch_to.window(window)
        break
# Wait for onload alert
new_page = wait.until(EC.alert_is_present())
print(new_page.text)
# Click OK
new_page.accept()
# Return to original window
driver.switch_to.window(original_window)
'''

input("Enter to close......................")
driver.quit()