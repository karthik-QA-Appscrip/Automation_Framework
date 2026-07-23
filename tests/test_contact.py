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
            TestContact.contact_first_name
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
    @allure.title("CONTACT_004 - Delete Contact")
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


    @allure.description("Create a contact, edit its name, and verify the changes")
    @allure.title("CONTACT_004 - Edit Contact")
    @pytest.mark.smoke
    def test_04_edit_contact(self, driver):
        self.logger.info("--- Starting Test 4: Edit Contact ---")
        
        fake = Faker()
        initial_name = fake.first_name()
        contact_email = fake.email()
        updated_name = f"{initial_name}_Edited"
        
        contact_page = self.login_and_navigate(driver)
        
        # 1. Create (Allow DB time to process because there is no success popup)
        self.logger.info(f"Creating initial contact: {initial_name}")
        contact_page.create_contact(initial_name, contact_email)
        time.sleep(5) 
        
        # 2. Search & Verify Original
        contact_page.search_field(initial_name)
        
        # 3. Edit (Allow DB time to process the updated name)
        self.logger.info(f"Editing contact name to: {updated_name}")
        contact_page.edit_contact(updated_name)
        time.sleep(5) 
        
        # 4. Verify Updated Data (Method automatically waits for grid to filter)
        actual_name, actual_email = contact_page.verify_contact(updated_name)
        
        AssertionHelper.verify_equal(updated_name, actual_name, "Verify updated name matches")
        AssertionHelper.verify_equal(contact_email, actual_email, "Verify email remained the same")
        self.logger.info("Successfully verified edited contact details.")
        
        # 5. Clean up
        contact_page.delete_contact_in_search_field()
        self.logger.info("Cleanup complete.")

    @allure.description("Search and verify a contact using their email address")
    @allure.title("CONTACT_005 - Search By Email")
    @pytest.mark.smoke
    def test_05_search_by_email(self, driver):
        self.logger.info("--- Starting Test 5: Search By email ---")

        # 1. Generate local test data
        fake = Faker()
        contact_name = fake.first_name()
        contact_email = fake.email()

        contact_page = self.login_and_navigate(driver)

        # 2. Create the contact
        self.logger.info(f"Creating contact -> Name: {contact_name} | Email: {contact_email}")
        contact_page.create_contact(contact_name, contact_email)

        # 3. Verify Contact (Searching by Email)
        # FIX: Only pass the email once to match your Page Object!
        actual_name, actual_email = contact_page.verify_contact(contact_email)
        
        # 4. Assert against the LOCAL variable
        AssertionHelper.verify_equal(contact_email, actual_email, "Email mismatch")
        AssertionHelper.verify_equal(contact_name, actual_name, "Name mismatch")
        
        self.logger.info("Successfully verified contact details by searching with email.")

        # 5. Clean up the database
        contact_page.delete_contact_in_search_field()
        self.logger.info("Cleanup complete.")