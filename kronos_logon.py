from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import keyring

usernameStr = 'maggieo'
passwordStr = keyring.get_password('kronos', usernameStr)

browser = webdriver.Chrome()
browser.get(('https://clemson.kronos.net/wfc/logon'))

#fill in username and password""
username = browser.find_element(By.ID, "username")
username.send_keys(usernameStr)

password = browser.find_element(By.ID, "passInput")
password.send_keys(passwordStr)

#press next button
nextButton = browser.find_element(By.ID, "loginSubmit")
nextButton.click()

#waits for next page to open

    #explicit wait not working: issue with presence_of_element?
    #recordTimeStamp = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn jqx-rc-all jqx-button jqx-widget jqx-fill-state-normal")))



#keep page open after preforming actions (to confirm testing)
time.sleep(1000)


