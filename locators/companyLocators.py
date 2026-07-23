from selenium.webdriver.common.by import By

class CompanyLocators:

    WORK_SPACE = (
        By.XPATH, "//button[@aria-label='Toggle Workspace menu']//div[@class='flex items-center space-x-3']"
    )

    COMPANY = (
        By.XPATH, "//a//span[.='Companies']"
    )

    