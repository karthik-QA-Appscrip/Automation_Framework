from re import A, X

from selenium.webdriver.common.by import By

class ContactsLocators:

    WORK_SPACE = (
        By.XPATH, "//button[@aria-label='Toggle Workspace menu']//div[@class='flex items-center space-x-3']"
    )

    CONTACTS_TAB = (
        By.XPATH, "//a//span[.='Contacts']"
    )

    ADD_CONTACT_BUTTON = (
        By.XPATH, "//button[normalize-space()='Add Contact']"
    )

    FIRST_NAME = (
        By.XPATH, "//label[contains(.,'First name')]//following::input[@name='firstName']"
    )

    EMAIL = (
        By.XPATH, "//h3[contains(normalize-space(),'Email')]//following::input[@type='email']"
    )

    ADMINISTRATION = (
        By.XPATH, "//button[@aria-label='Toggle Administration menu']"
    )

    AUDIT_LOGS = (
        By.XPATH, "//li//span[.='Audit Logs']"
    )

    POP_UP = (
        By.XPATH, "//section[@aria-label='Notifications alt+T']"
    )
    
    VIEW_BUTTON = (
        By.XPATH, "//tbody/tr[1]//button[contains(@aria-label, 'View') or contains(@title, 'View')]"
    )

    SEARCH_FIELD = (
        By.XPATH, "//input[contains(@placeholder,'Search contacts...')]"
    )

    VERIFY_NAME = (
        By.XPATH, "//h2[@class='font-bold text-lg leading-tight break-words']"
    )

    VERIFY_EMAIL = (
        By.XPATH, "//div[@class='space-y-1 min-w-0 flex-1']//a"
    )

    SAVE_BUTTON = (
        By.XPATH, "//button[contains(normalize-space(),'Save contact')]"
    )

    DELETE_CONTACT_BUTTON = (By.XPATH, "//button[contains(., 'Delete')]") 

    CONFIRM_DELETE = (By.XPATH, "//button[contains(., 'Delete')]")

    SEARCH_FIELD_DELETE_BUTTON = (
        By.XPATH, "//tbody/tr[1]//button[contains(@aria-label, 'Delete') or contains(@title, 'Delete')]"
    )

    EDIT_CONTACT = (
        By.XPATH, "//tbody/tr[1]//button[contains(@aria-label, 'Edit') or contains(@title, 'Edit')]"
    )

    REFRESH_BUTTON = (
        By.XPATH, "//button[normalize-space()='Refresh']"
    )

    CONTACT_TABLE_ROWS = (
        By.XPATH, "//tbody[@class='[&_tr:last-child]:border-0']"
    )

        