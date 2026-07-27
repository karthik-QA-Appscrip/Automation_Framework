import time
from tkinter import S
from xml.dom.minidom import Element
from selenium.webdriver.common.keys import Keys
from pages.basePage import BasePage
from utilities.waitHelper import WaitUtils
from locators.companyLocators import CompanyLocators
from selenium.webdriver.common.by import By


class CompanyPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WaitUtils(driver)

    def click_work_space(self):
            self.wait.wait_for_visibility(CompanyLocators.WORK_SPACE)
            self.click(CompanyLocators.WORK_SPACE)

    def click_view_company(self, company_name):
        locator = (
            By.XPATH,
            f"//tr[.//*[normalize-space()='{company_name}']]//button[@aria-label='View company']"
        )
        self.wait.wait_for_visibility(locator)
        self.click(locator)


    def click_edit_company(self, company_name):
        locator = (
            By.XPATH,
            f"//tr[.//*[normalize-space()='{company_name}']]//button[contains(@aria-label, 'Edit')]"
        )
        self.wait.wait_for_visibility(locator)
        self.click(locator)


    def click_delete_company(self, company_name):
        locator = (
            By.XPATH,
            f"//tr[.//*[normalize-space()='{company_name}']]//button[@aria-label='Delete company']"
        )
        self.wait.wait_for_clickable(locator)
        self.click(locator)

    def get_company_name(self, company_name):
        locator = (
            By.XPATH,
            f"//*[self::td or self::div or self::span or self::a][normalize-space()='{company_name}']"
        )
        self.wait.wait_for_visibility(locator)
        return self.get_text(locator)

    def click_company_tab(self):
         self.wait.wait_for_visibility(CompanyLocators.COMPANY)
         self.click(CompanyLocators.COMPANY)

    def click_add_company_button(self):
         self.wait.wait_for_visibility(CompanyLocators.ADD_COPANY)
         self.click(CompanyLocators.ADD_COPANY)

    def enter_company_name(self, company_name):
         self.wait.wait_for_visibility(CompanyLocators.COMPNAY_NAME)
         self.enter_text(CompanyLocators.COMPNAY_NAME, company_name)

    def enter_company_email(self, email):
         self.wait.wait_for_visibility(CompanyLocators.EMAIL_ID)
         self.enter_text(CompanyLocators.EMAIL_ID, email)

    def click_save_company_button(self):
         self.wait.wait_for_clickable(CompanyLocators.SAVE_BUTTON)
         self.click(CompanyLocators.SAVE_BUTTON)

    def create_company(self, company_name, email):
         self.click_add_company_button()
         self.wait.wait_for_visibility(CompanyLocators.COMPNAY_NAME)
         self.enter_company_name(company_name)
         self.enter_company_email(email)
         self.click_save_company_button()

    def verify_company(self, company_name):
         self.wait.wait_for_visibility(CompanyLocators.BEFROE_COUNT)
         return self.get_company_name(company_name)

    def verify_company_name(self,company_name):
        self.click_view_company(company_name)
        locators = By.XPATH, f"//h2[normalize-space()='{company_name}']"
        self.wait.wait_for_visibility(locators)
        return self.get_text(locators)

    def view_company_and_get_name(self, company_name):
        return self.verify_company_name(company_name)

    def delete_company(self, company_name):
        self.click_delete_company(company_name)
        self.wait.wait_for_visibility(CompanyLocators.CONFIRM_DELETE)
        self.click(CompanyLocators.CONFIRM_DELETE)

    def edit_company(self, company_name, new_name):
        self.click_edit_company(company_name)

        element = self.wait.wait_for_visibility(CompanyLocators.EDIT_COMPANY_NAME)
        time.sleep(3)
        self.clear(CompanyLocators.EDIT_COMPANY_NAME)

        element.send_keys(new_name)

        time.sleep(2)
        self.wait.wait_for_visibility(CompanyLocators.SAVE_BUTTON)
        self.click(CompanyLocators.SAVE_BUTTON)

        time.sleep(5)

        print("Edited to:", new_name)

    def get_popup_text(self):
         self.wait.wait_for_visibility(CompanyLocators.POP_UP)
         return self.get_text(CompanyLocators.POP_UP)

    
    