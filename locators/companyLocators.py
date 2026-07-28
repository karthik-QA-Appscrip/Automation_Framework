from selenium.webdriver.common.by import By

class CompanyLocators:

    WORK_SPACE = (
        By.XPATH, "//button[@aria-label='Toggle Workspace menu']//div[@class='flex items-center space-x-3']"
    )

    COMPANY = (
        By.XPATH, "//a//span[.='Companies']"
    )

    ADD_COPANY = (
        By.XPATH, "//button[normalize-space()='Add Company']"
    )

    COMPNAY_NAME = (
        By.XPATH, "//label[contains(., 'Name')]//following::input[1]"
    )

    EMAIL_ID = (
        By.XPATH, "//input[@type='email']"
    )

    SAVE_BUTTON = (
        By.XPATH, "//button[normalize-space()='Save company']"
    )

    BEFROE_COUNT = (
        By.XPATH, "//tbody/tr"
    )

    AFTER_COUNT = (
        By.XPATH, "//tbody/tr"
    )

    COMPANY_NAME_VIEW = (
        By.XPATH, "//h2[contains(@class, 'font-bold')]"
    )

    CONFIRM_DELETE = (
        By.XPATH, "//button[normalize-space()='Delete']"
    )

    EDIT_COMPANY_NAME = (
        By.XPATH, "//input[@name='name']"
    )

    POP_UP = (
        By.XPATH, "//section[@aria-label='Notifications alt+T']"
    )

    REFRESH_BUTTON = (
        By.XPATH, "//button[normalize-space()='Refresh']"
    )

    CONTACT_TABLE_ROWS = (
            By.XPATH, "//tbody[@class='[&_tr:last-child]:border-0']"
        )
    

    