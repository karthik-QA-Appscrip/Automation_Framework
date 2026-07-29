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
from utilities.waitHelper import WaitUtils


class TestContact(BaseTest):

    # 1. Class-level variables to share the generated data across all 3 tests
    contact_first_name = ""
    contact_email = ""

    def login_and_navigate(self):
        login = LoginPage()
        contact_page = ContactPage()
        test_data = TestData()
        wait_utils = login.wait

        current_url = login.driver.current_url
        login.login(test_data.valid_username, test_data.valid_password)
        
        # Use your custom utility instead of a raw lambda!
        wait_utils.wait_for_url_to_change(current_url)
        time.sleep(3) 

        contact_page.click_work_space()
        contact_page.click_contacts_tab()
        
        return contact_page


    @allure.description("Create a new contact")
    @allure.title("CONTACT_001 - Create Contact")
    @pytest.mark.smoke
    def test_01_create_contact(self):
        self.logger.info("--- Starting Test 1: Create Contact ---")
        
        # Generate the unique data and save it to the Class variables
        fake = Faker()
        TestContact.contact_first_name = fake.first_name()  
        TestContact.contact_email = fake.email()
        self.logger.info(f"Generated Data -> Name: {TestContact.contact_first_name} | Email: {TestContact.contact_email}")

        # Use our helper to get to the right page
        contact_page = self.login_and_navigate()

        # Execute creation
        contact_page.create_contact(TestContact.contact_first_name, TestContact.contact_email)
        time.sleep(5) # Allow database to process
        
        self.logger.info("Successfully created contact.")


    @allure.description("Search and verify the previously created contact")
    @allure.title("CONTACT_002 - Verify Contact")
    @pytest.mark.smoke
    def test_02_verify_contact(self):
        self.logger.info("--- Starting Test 2: Verify Contact ---")
        
        # Safety check: If Test 1 failed, we can't run this test.
        if not TestContact.contact_first_name:
            pytest.skip("Skipping: No contact was created in Test 1.")

        contact_page = self.login_and_navigate()

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
    def test_03_delete_contact(self):
        self.logger.info("--- Starting Test 3: Delete Contact ---")
        
        if not TestContact.contact_first_name:
            pytest.skip("Skipping: No contact exists to delete.")

        contact_page = self.login_and_navigate()

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
    def test_04_edit_contact(self):
        self.logger.info("--- Starting Test 4: Edit Contact ---")
        
        fake = Faker()
        initial_name = fake.first_name()
        contact_email = fake.email()
        updated_name = f"{initial_name}_Edited"
        
        contact_page = self.login_and_navigate()
        
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
    def test_05_search_by_email(self):
        self.logger.info("--- Starting Test 5: Search By email ---")

        # 1. Generate local test data
        fake = Faker()
        contact_name = fake.first_name()
        contact_email = fake.email()

        contact_page = self.login_and_navigate()

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

    @allure.description("Verify the refresh button functionality reloads the grid")
    @allure.title("CONTACT_006 - Refresh functionality testing")
    @pytest.mark.smoke
    def test_06_refresh_functionality(self):
        self.logger.info("--- Starting Test 6: Refresh Functionality ---")

        contact_page = self.login_and_navigate()

        value = contact_page.refresh_page()

        AssertionHelper.verify_true(value, "Verify page/grid successfully refreshed")
        self.logger.info("Successfully verified refresh functionality.")



    @allure.description("Create contact with blank First Name")
    @allure.title("CONTACT_007 - Create Contact with Blank First Name")
    @pytest.mark.smoke
    def test_07_create_contact_with_blank_first_name(self):
        self.logger.info("--- Starting Test 7: Create contact with blank First Name ---")

        fake = Faker()
        contact_name = ""
        contact_email = fake.email()

        self.logger.info(f"Test Data -> First Name: '{contact_name}', Email: {contact_email}")

        contact_page = self.login_and_navigate()

        self.logger.info("Attempting to create contact with blank First Name.")

        actual_result = contact_page.create_invalid_contact(contact_name, contact_email)

        self.logger.info(f"Actual Validation Message : {actual_result}")

        expected_result = "First name is required"

        self.logger.info(f"Expected Validation Message : {expected_result}")

        AssertionHelper.verify_contains(expected_result, actual_result)

        self.logger.info("Successfully verified validation message for blank First Name.")



    @allure.description("Create contact with blank Email")
    @allure.title("CONTACT_008 - Create Contact with Blank Email")
    @pytest.mark.smoke
    def test_08_create_contact_with_blank_email(self):
        self.logger.info("--- Starting Test 8: Create contact with blank Email ---")

        fake = Faker()
        contact_name = fake.first_name()
        contact_email = ""

        self.logger.info(f"Test Data -> First Name: {contact_name}, Email: '{contact_email}'")

        contact_page = self.login_and_navigate()

        self.logger.info("Attempting to create contact with blank Email.")

        actual_result = contact_page.create_invalid_contact(contact_name, contact_email)

        self.logger.info(f"Actual Validation Message : {actual_result}")

        expected_result = "Email is required"

        self.logger.info(f"Expected Validation Message : {expected_result}")

        AssertionHelper.verify_contains(expected_result, actual_result)

        self.logger.info("Successfully verified validation message for blank Email.")


    @allure.description("Create contact with invalid Email")
    @allure.title("CONTACT_009 - Create Contact with Invalid Email")
    @pytest.mark.smoke
    def test_09_create_contact_with_invalid_email(self):
        self.logger.info("--- Starting Test 9: Create contact with invalid Email ---")

        fake = Faker()
        contact_name = fake.first_name()
        contact_email = "invalidemail"   # Invalid email format

        self.logger.info(f"Test Data -> First Name: {contact_name}, Email: {contact_email}")

        contact_page = self.login_and_navigate()

        self.logger.info("Attempting to create contact with an invalid Email.")

        actual_result = contact_page.create_invalid_contact(contact_name, contact_email)

        self.logger.info(f"Actual Validation Message : {actual_result}")

        expected_result = "Please enter a valid email address"

        self.logger.info(f"Expected Validation Message : {expected_result}")

        AssertionHelper.verify_contains(expected_result, actual_result)

        self.logger.info("Successfully verified validation message for invalid Email.")



    @allure.description("Create contact with duplicate Email")
    @allure.title("CONTACT_010 - Create Contact with Duplicate Email")
    @pytest.mark.smoke
    def test_10_create_contact_with_duplicate_email(self):

        self.logger.info("--- Starting Test 10: Create Contact with Duplicate Email ---")

        fake = Faker()
        contact_name = fake.first_name()
        contact_email = fake.email()

        self.logger.info(
            f"Generated Test Data -> Name: {contact_name}, Email: {contact_email}"
        )

        contact_page = self.login_and_navigate()

        # Create contact
        self.logger.info("Creating contact for the first time.")
        contact_page.create_contact(contact_name, contact_email)

        # Verify contact was created
        actual_name, actual_email = contact_page.verify_contact(contact_name)


        self.logger.info(f"Expected Name  : {contact_name}")
        self.logger.info(f"Actual Name    : {actual_name}")
        self.logger.info(f"Expected Email : {contact_email}")
        self.logger.info(f"Actual Email   : {actual_email}")

        AssertionHelper.verify_equal(contact_name, actual_name)
        AssertionHelper.verify_equal(contact_email, actual_email)

        self.logger.info("Contact created successfully.")

        # Try creating another contact with same email
        self.logger.info("Creating another contact with the same email.")

        contact_page.create_contact(fake.first_name(), contact_email)

        actual_popup = contact_page.get_pop_up_text()
        expected_popup = "A user with this email already exists in our system"

        self.logger.info(f"Expected Popup : {expected_popup}")
        self.logger.info(f"Actual Popup   : {actual_popup}")

        AssertionHelper.verify_contains(expected_popup, actual_popup)

        self.logger.info("Duplicate email validation verified successfully.")


    @allure.description("Search contact by partial name")
    @allure.title("CONTACT_011 - Search Contact by Partial Name")
    @pytest.mark.smoke
    def test_11_search_contact_by_partial_name(self):

        self.logger.info("--- Starting Test 11: Search Contact by Partial Name ---")

        fake = Faker()
        contact_name = fake.first_name()      # Example: Matthew
        contact_email = fake.email()

        self.logger.info(
            f"Generated Test Data -> Name: {contact_name}, Email: {contact_email}"
        )

        contact_page = self.login_and_navigate()

        # Create Contact
        self.logger.info("Creating contact.")
        contact_page.create_contact(contact_name, contact_email)

        # Verify contact creation
        actual_name, actual_email = contact_page.verify_contact(contact_name)

        AssertionHelper.verify_equal(contact_name, actual_name)
        AssertionHelper.verify_equal(contact_email, actual_email)

        self.logger.info("Contact created successfully.")

        # Search using partial name
        partial_name = contact_name[:4]   # Example: "Matt"

        self.logger.info(f"Searching with partial name: {partial_name}")

        actual_name, actual_email = contact_page.verify_contact(partial_name)

        self.logger.info(f"Expected Name  : {contact_name}")
        self.logger.info(f"Actual Name    : {actual_name}")

        AssertionHelper.verify_contains(contact_name, actual_name)

        self.logger.info("Partial name search verified successfully.")


    @allure.description("Verify contact count increases after creating a new contact")
    @allure.title("CONTACT_012 - Verify Contact Count After Creation")
    @pytest.mark.smoke
    def test_12_count_contacts_after_creation(self):

        self.logger.info("--- Starting Test 12: Verify Contact Count After Creation ---")

        fake = Faker()
        contact_name = fake.first_name()
        contact_email = fake.email()

        self.logger.info(
            f"Generated Test Data -> Name: {contact_name}, Email: {contact_email}"
        )

        contact_page = self.login_and_navigate()

        # Get count before creation
        before_count = contact_page.get_contact_count()

        self.logger.info(f"Before Count : {before_count}")

        # Create contact
        contact_page.create_contact(contact_name, contact_email)

        # Verify contact
        actual_name, actual_email = contact_page.verify_contact(contact_name)

        AssertionHelper.verify_equal(contact_name, actual_name)
        AssertionHelper.verify_equal(contact_email, actual_email)

        # Go to Dashboard again
        after_count = contact_page.get_contact_count()

        self.logger.info(f"After Count : {before_count}")

        AssertionHelper.verify_equal(before_count + 1, after_count)


    @allure.description("Verify contact count decrements after deleting a contact")
    @allure.title("CONTACT_013 - Verify Contact Count After Deletion")
    @pytest.mark.smoke
    def test_13_count_contacts_after_deletion(self):

        self.logger.info("--- Starting Test 13 ---")

        fake = Faker()
        contact_name = fake.first_name()
        contact_email = fake.email()

        contact_page = self.login_and_navigate()

        # Count before creation
        before_count = contact_page.get_contact_count()
        self.logger.info(f"Before Count : {before_count}")

        # Create contact
        contact_page.create_contact(contact_name, contact_email)

        # Verify contact
        actual_name, actual_email = contact_page.verify_contact(contact_name)

        AssertionHelper.verify_equal(contact_name, actual_name)
        AssertionHelper.verify_equal(contact_email, actual_email)

        # Count after creation
        count_after_creation = contact_page.get_contact_count()
        self.logger.info(f"Count After Creation : {count_after_creation}")

        AssertionHelper.verify_equal(before_count + 1, count_after_creation)

        # Search contact
        contact_page.search_field(contact_name)

        # Delete contact
        popup = contact_page.delete_contact_in_search_field()

        AssertionHelper.verify_contains("Contact deleted", popup)

        contact_page.wait_for_popup_to_clear()

        # Count after deletion
        after_count = contact_page.get_contact_count()
        self.logger.info(f"After Count : {after_count}")

        AssertionHelper.verify_equal(count_after_creation - 1, after_count)

        self.logger.info("Contact count decremented successfully.")