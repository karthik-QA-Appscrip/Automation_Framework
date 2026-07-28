import time
from xml.dom.minidom import Element
from selenium.webdriver.common.keys import Keys
from pages.basePage import BasePage
from utilities.waitHelper import WaitUtils
from locators.contactsLocators import ContactsLocators
from selenium.common.exceptions import StaleElementReferenceException


class ContactPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WaitUtils(driver)

    def click_work_space(self):
        self.wait.wait_for_visibility(ContactsLocators.WORK_SPACE)
        self.click(ContactsLocators.WORK_SPACE)

    def click_contacts_tab(self):
        self.wait.wait_for_visibility(ContactsLocators.CONTACTS_TAB)
        self.click(ContactsLocators.CONTACTS_TAB)

    def click_add_contact_button(self):
        self.wait.wait_for_visibility(ContactsLocators.ADD_CONTACT_BUTTON)
        self.click(ContactsLocators.ADD_CONTACT_BUTTON)

    def first_name(self, first_name):
        self.wait.wait_for_visibility(ContactsLocators.FIRST_NAME)
        self.enter_text(ContactsLocators.FIRST_NAME, first_name)

    def email(self, email):
        self.wait.wait_for_visibility(ContactsLocators.EMAIL)
        self.enter_text(ContactsLocators.EMAIL, email)

    def click_administration(self):
        self.wait.wait_for_visibility(ContactsLocators.ADMINISTRATION)
        self.click(ContactsLocators.ADMINISTRATION)

    def click_audit_logs(self):
        self.wait.wait_for_visibility(ContactsLocators.AUDIT_LOGS)
        self.click(ContactsLocators.AUDIT_LOGS)

    def click_view_button(self):
        self.wait.wait_for_visibility(ContactsLocators.VIEW_BUTTON)
        self.click(ContactsLocators.VIEW_BUTTON)

    def search_field(self, search_text):
        self.wait.wait_for_visibility(ContactsLocators.SEARCH_FIELD)
        self.clear(ContactsLocators.SEARCH_FIELD)
        self.enter_text(ContactsLocators.SEARCH_FIELD, search_text)
        # Press ENTER to trigger the search query
        self.driver.find_element(*ContactsLocators.SEARCH_FIELD).send_keys(Keys.ENTER)

    def get_verify_name(self):
        self.wait.wait_for_visibility(ContactsLocators.VERIFY_NAME)
        return self.get_text(ContactsLocators.VERIFY_NAME)

    def get_verify_email(self):
        self.wait.wait_for_visibility(ContactsLocators.VERIFY_EMAIL)
        return self.get_text(ContactsLocators.VERIFY_EMAIL)

    def click_save_button(self):
        self.wait.wait_for_visibility(ContactsLocators.SAVE_BUTTON)
        self.click(ContactsLocators.SAVE_BUTTON)

    def get_and_verify__popup(self):
        self.wait.wait_for_visibility(ContactsLocators.POP_UP)
        return self.get_text(ContactsLocators.POP_UP)

    def wait_for_popup_to_clear(self):
        """Dynamically waits for the success toast to appear, then fade away."""
        self.wait.wait_for_visibility(ContactsLocators.POP_UP)
        self.wait.wait_for_invisibility(ContactsLocators.POP_UP)

    def create_contact(self, first_name, email):
        self.click_add_contact_button()
        self.first_name(first_name)
        self.email(email)
        self.click_save_button()


    def edit_contact(self, edit_name):
        self.wait.wait_for_visibility(ContactsLocators.EDIT_CONTACT)
        self.click(ContactsLocators.EDIT_CONTACT)
        self.clear(ContactsLocators.FIRST_NAME)
        self.enter_text(ContactsLocators.FIRST_NAME, edit_name) # BasePage handles clearing
        self.click_save_button()
       

    def verify_contact(self, value):
        self.click_contacts_tab()
        self.wait.wait_for_visibility(ContactsLocators.SEARCH_FIELD)
        
        self.search_field(value)
        
        # Wait dynamically for the grid to filter instead of time.sleep(3)
        from selenium.webdriver.common.by import By
        self.wait.wait_for_text_in_element((By.XPATH, "//tbody/tr[1]"), value)
        
        self.click_view_button()
        self.wait.wait_for_visibility(ContactsLocators.VERIFY_NAME) # Wait for profile to open
        
        name = self.get_verify_name()
        email = self.get_verify_email()

        self.click(ContactsLocators.CONTACTS_TAB)
        return name, email

    def delete_contact_in_search_field(self):
        self.click_contacts_tab()
        
        # No overlay! Just wait for the delete button to be ready to click
        self.wait.wait_for_visibility(ContactsLocators.SEARCH_FIELD_DELETE_BUTTON)
        self.click(ContactsLocators.SEARCH_FIELD_DELETE_BUTTON)

        self.wait.wait_for_visibility(ContactsLocators.CONFIRM_DELETE)
        self.click(ContactsLocators.CONFIRM_DELETE)

        return self.get_and_verify__popup()

    def refresh_page(self):

        for i in range(3):
            try:
                self.click(ContactsLocators.REFRESH_BUTTON)
                break
            except StaleElementReferenceException:
                if i == 2:
                    raise

        self.wait.wait_for_visibility(
            ContactsLocators.CONTACT_TABLE_ROWS
        )

        return True

    def get_pop_up_text(self):
        self.wait.wait_for_visibility(ContactsLocators.POP_UP)
        self.find_element(ContactsLocators.POP_UP)
        
        return self.get_text(ContactsLocators.POP_UP)

    

    def create_invalid_contact(self,first_name,email):
        self.click_add_contact_button()
        self.first_name(first_name)
        self.email(email)
        self.click_save_button()

        return self.get_pop_up_text()

    def before_count_contact(self):
        self.wait.wait_for_visibility(ContactsLocators.BEFROE_COUNT)
        rows = self.find_all(ContactsLocators.BEFROE_COUNT)
        # count_no = len(rows)

        # return count_no  
        print("Total Rows:", len(rows))

        for i, row in enumerate(rows):
            print(i, row.text)

        return len(rows)

    def after_count_contact(self):
        self.wait.wait_for_visibility(ContactsLocators.BEFROE_COUNT)

        rows = self.find_all(ContactsLocators.BEFROE_COUNT)

        print("After count:", len(rows))

        for i, row in enumerate(rows):
            print(i, row.is_displayed())

        return len(rows)

    def get_contact_count(self):
        self.click(ContactsLocators.DASHBOARD)
        self.click(ContactsLocators.REFRESH_BUTTON)
        time.sleep(2)
        self.wait.wait_for_visibility(ContactsLocators.CONTACT_COUNT)

        count = self.get_text(ContactsLocators.CONTACT_COUNT)

        self.click(ContactsLocators.CONTACT_COUNT)

        return int(count)
