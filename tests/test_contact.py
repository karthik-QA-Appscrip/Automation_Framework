import time
import allure
import pytest
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait

from fixtures.browser_fixture import driver
from pages.contactPage import ContactPage
from pages.loginPage import LoginPage
from constants import messages
from utilities.BaseTest import BaseTest
from utilities.TestDataManager import TestData
from utilities.assertionHelper import AssertionHelper


class TestContact(BaseTest):

    # 1. Class-level variables to share the generated data across all 3 tests
    contact_first_name = ""
    contact_email = ""

    def login_and_navigate(self, driver):
        """Helper method to log in and open contacts page so we don't repeat this code 3 times."""
        login = LoginPage(driver)
        contact_page = ContactPage(driver)
        test_data = TestData()

        # Login
        login.login(test_data.valid_username, test_data.valid_password)
        WebDriverWait(driver, 30).until(lambda d: "/login" not in d.current_url)
        time.sleep(3) 

        # Navigate
        contact_page.click_work_space()
        contact_page.click_contacts_tab()
        
        return contact_page


    @allure.description("Create a new contact")
    @allure.title("CONTACT_001 - Create Contact")
    @pytest.mark.smoke
    def test_01_create_contact(self, driver):
        self.logger.info("--- Starting Test 1: Create Contact ---")
        
        # Generate the unique data and save it to the Class variables
        fake = Faker()
        TestContact.contact_first_name = fake.first_name()  
        TestContact.contact_email = fake.email()
        self.logger.info(f"Generated Data -> Name: {TestContact.contact_first_name} | Email: {TestContact.contact_email}")

        # Use our helper to get to the right page
        contact_page = self.login_and_navigate(driver)

        # Execute creation
        contact_page.create_contact(TestContact.contact_first_name, TestContact.contact_email)
        time.sleep(5) # Allow database to process
        
        self.logger.info("Successfully created contact.")


    @allure.description("Search and verify the previously created contact")
    @allure.title("CONTACT_002 - Verify Contact")
    @pytest.mark.smoke
    def test_02_verify_contact(self, driver):
        self.logger.info("--- Starting Test 2: Verify Contact ---")
        
        # Safety check: If Test 1 failed, we can't run this test.
        if not TestContact.contact_first_name:
            pytest.skip("Skipping: No contact was created in Test 1.")

        contact_page = self.login_and_navigate(driver)

        # The verify_contact method handles the search and the extraction
        actual_name, actual_email = contact_page.verify_contact(
            TestContact.contact_first_name,
            TestContact.contact_email
        )

        self.logger.info(
            f"Verified contact values -> Name: {actual_name} | Email: {actual_email}"
        )
        self.logger.info(
            f"Expected contact values -> Name: {TestContact.contact_first_name} | Email: {TestContact.contact_email}"
        )

        assert actual_name == TestContact.contact_first_name, (
            f"Name mismatch. Expected '{TestContact.contact_first_name}', got '{actual_name}'."
        )
        assert actual_email == TestContact.contact_email, (
            f"Email mismatch. Expected '{TestContact.contact_email}', got '{actual_email}'."
        )

        self.logger.info("Successfully verified contact details.")


    @allure.description("Delete the contact to clean up the database")
    @allure.title("CONTACT_003 - Delete Contact")
    @pytest.mark.smoke
    def test_03_delete_contact(self, driver):
        self.logger.info("--- Starting Test 3: Delete Contact ---")
        
        if not TestContact.contact_first_name:
            pytest.skip("Skipping: No contact exists to delete.")

        contact_page = self.login_and_navigate(driver)

        # 1. We must search for the specific contact first so we delete the right one
        contact_page.search_field(TestContact.contact_first_name)
        time.sleep(3) # Wait for search grid to filter
        
        # 2. Execute deletion
        result = contact_page.delete_contact_in_search_field()
        expected_word = "Contact deleted"
        AssertionHelper.verify_contains(expected_word, result, "Checking if success message contains 'Delete'")
        
        self.logger.info("Successfully deleted contact. Cleanup complete.")