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

    COMPANY_TABLE_ROWS = (
            By.XPATH, "//tbody[@class='[&_tr:last-child]:border-0']"
        )

    SEARCH_FIELD = (
        By.XPATH, "//input[@placeholder='Search companies...']"
    )

    GET_COMPANY_NAME = (
        By.XPATH, "//div[@class='min-w-0 flex-1']//h2"
    )

    COMPANIES_COUNT = (
        By.XPATH, "//p[normalize-space()='Companies']/ancestor::div[@data-slot='card-content']//p[contains(@class,'text-3xl')]"
    )

    DASHBOARD = (
        By.XPATH , "//span[normalize-space()='Dashboard']"
    )

    REFRESH_BUTTON = (
        By.XPATH, "//button[normalize-space()='Refresh']"
    )

    AUDIT_LOGS_ACTION = (
        By.XPATH, "//tbody/tr[1]/td[3]//span"
    )

    AUDIT_LOGS_CATEGORY = (
        By.XPATH, "//tbody/tr[1]/td[4]//span"
    )

    ADMINISTRATION = (
            By.XPATH, "//button[@aria-label='Toggle Administration menu']"
        )
    
    AUDIT_LOGS = (
            By.XPATH, "//li//span[.='Audit Logs']"
        )

