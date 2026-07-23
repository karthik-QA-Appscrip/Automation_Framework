from utilities.DriverFactory import DriverFactory
from utilities.TestDataManager import TestData
from pages.loginPage import LoginPage
from selenium.webdriver.common.by import By
import time


driver = DriverFactory.get_driver(browser='chrome', headless=True)
driver.maximize_window()
driver.get('https://sandbox.houseofapps.ai/login')
login = LoginPage(driver)
login.login(TestData.valid_username, TestData.valid_password)
print('login done')
time.sleep(8)
print('url=', driver.current_url)
print('title=', driver.title)

xpaths = [
    "//div[@id='work-space']",
    "//a//span[.='Contacts']",
    "//button[normalize-space()='Add Contact']",
    "//input[contains(@placeholder,'Search contacts...')]",
    "//button[@aria-label='Toggle Administration menu']",
]
for xpath in xpaths:
    els = driver.find_elements(By.XPATH, xpath)
    print(xpath, 'count=', len(els))
    if els:
        print('text=', els[0].text[:200])
        print('html=', els[0].get_attribute('outerHTML')[:600])

print('--- page source snippet ---')
print(driver.page_source[:6000])

driver.quit()
