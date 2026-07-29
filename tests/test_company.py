import time
import allure
import pytest
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait

from fixtures.browser_fixture import driver
from pages.companyPage import CompanyPage
from pages.loginPage import LoginPage
from constants import messages
from utilities.BaseTest import BaseTest
from utilities.TestDataManager import TestData
from utilities.assertionHelper import AssertionHelper
from utilities.waitHelper import WaitUtils
from locators.companyLocators import CompanyLocators


class TestCompany(BaseTest):

    company_name = ""
    company_email = ""

    def login_and_navigate(self):
        login = LoginPage()
        company_page = CompanyPage()
        test_data = TestData()
        wait_utils = login.wait

        login.login(
            test_data.valid_username,
            test_data.valid_password
        )

        # Wait until Workspace button appears after login
        company_page.wait.wait_for_visibility(
            CompanyLocators.WORK_SPACE
        )

        company_page.click_work_space()
        company_page.click_company_tab()

        return company_page

    @allure.description("Create a new company")
    @allure.title("COMPANY_001 - Create Company")
    @pytest.mark.smoke
    def test_01_create_company(self):
        self.logger.info("--- Starting Test 1: Create Company ---")

        fake = Faker()
        TestCompany.company_name = fake.company()
        TestCompany.company_email = fake.email()
        self.logger.info(
            f"Generated Data -> Name: {TestCompany.company_name} | Email: {TestCompany.company_email}"
        )

        company_page = self.login_and_navigate()
        company_page.create_company(TestCompany.company_name, TestCompany.company_email)
        time.sleep(5)

        self.logger.info("Successfully created company.")

    @allure.description("Verify the created company")
    @allure.title("COMPANY_002 - Verify Company")
    @pytest.mark.smoke
    def test_02_verify_company(self):
        self.logger.info("--- Starting Test 2: Verify Company ---")

        if not TestCompany.company_name:
            pytest.skip("Skipping: No company was created in Test 1.")

        company_page = self.login_and_navigate()

        company_page.click_view_company(TestCompany.company_name)
        actual_name = company_page.view_company_and_get_name(TestCompany.company_name)

        self.logger.info(f"Viewed company name -> {actual_name}")
        self.logger.info(f"Expected company name -> {TestCompany.company_name}")

        assert actual_name == TestCompany.company_name, (
            f"Company name mismatch. Expected '{TestCompany.company_name}', got '{actual_name}'."
        )

        self.logger.info("Successfully verified company details.")

    @allure.description("Delete the created company")
    @allure.title("COMPANY_003 - Delete Company")
    @pytest.mark.smoke
    def test_03_delete_company(self):
        self.logger.info("--- Starting Test 3: Delete Company ---")

        if not TestCompany.company_name:
            pytest.skip("Skipping: No company exists to delete.")

        company_page = self.login_and_navigate()

        company_page.delete_company(TestCompany.company_name)

        result = company_page.get_popup_text()
        expected_word = "Company deleted"

        AssertionHelper.verify_equal(expected_word, result, "Checking if success message contains 'Delete'")

        self.logger.info(f"Deleted company -> {TestCompany.company_name}")
        self.logger.info("Successfully deleted company.")

    @allure.description("Create and verify a second company")
    @allure.title("COMPANY_004 - Create and Verify Another Company")
    @pytest.mark.smoke
    def test_04_create_and_verify_another_company(self):
        self.logger.info("--- Starting Test 4: Create and Verify Another Company ---")

        fake = Faker()
        TestCompany.company_name = fake.company()
        TestCompany.company_email = fake.email()
        self.logger.info(
            f"Generated Data -> Name: {TestCompany.company_name} | Email: {TestCompany.company_email}"
        )

        company_page = self.login_and_navigate()
        company_page.create_company(TestCompany.company_name, TestCompany.company_email)
        time.sleep(5)

        actual_name = company_page.view_company_and_get_name(TestCompany.company_name)

        self.logger.info(f"Viewed company name -> {actual_name}")
        self.logger.info(f"Expected company name -> {TestCompany.company_name}")

        assert actual_name == TestCompany.company_name, (
            f"Company name mismatch. Expected '{TestCompany.company_name}', got '{actual_name}'."
        )

        self.logger.info("Successfully created and verified another company.")

    @allure.description("Edit the created company")
    @allure.title("COMPANY_005 - Edit Company")
    @pytest.mark.smoke
    def test_05_edit_company(self):
        self.logger.info("--- Starting Test 5: Edit Company ---")


        company_page = self.login_and_navigate()

        fake = Faker()
        TestCompany.company_name = fake.company()
        TestCompany.company_email = fake.email()

        company_page.create_company(TestCompany.company_name,TestCompany.company_email)
        

        updated_name = f"{TestCompany.company_name}_Edited"
        company_page.edit_company(TestCompany.company_name, updated_name)
        time.sleep(5)

        actual_name = company_page.view_company_and_get_name(updated_name)

        self.logger.info(f"Edited company name -> {actual_name}")
        self.logger.info(f"Expected company name -> {updated_name}")

        assert actual_name == updated_name, (
            f"Company name mismatch after edit. Expected '{updated_name}', got '{actual_name}'."
        )

        self.logger.info("Successfully edited company.")

    @allure.description("Verify the refresh button functionality reloads the company grid")
    @allure.title("COMPANY_006 - Refresh functionality testing")
    @pytest.mark.smoke
    def test_06_refresh_functionality(self):
        self.logger.info("--- Starting Test 6: Refresh Functionality ---")

        company_page = self.login_and_navigate()

        value = company_page.refresh_functionality()

        AssertionHelper.verify_true(value, "Verify company grid successfully refreshed")
        self.logger.info("Successfully verified refresh functionality.")


    @allure.description("Search and verify a company using their name")
    @allure.title("COMPANY_007 - Search company by name")
    @pytest.mark.smoke
    def test_07_search_by_name(self):

        self.logger.info("========== COMPANY_007 STARTED ==========")
        self.logger.info("Test Objective : Search and verify a company using company name.")

        company_page = self.login_and_navigate()

        fake = Faker()

        TestCompany.company_name = fake.company()
        TestCompany.company_email = fake.email()

        self.logger.info(f"Generated Company Name : {TestCompany.company_name}")
        self.logger.info(f"Generated Company Email : {TestCompany.company_email}")

        self.logger.info("Creating a new company.")

        company_page.create_company(
            TestCompany.company_name,
            TestCompany.company_email
        )

        self.logger.info("Company created successfully.")

        self.logger.info(
            f"Searching and verifying company : {TestCompany.company_name}"
        )

        actual_result = company_page.verify_company_details(
            TestCompany.company_name
        )

        expected_result = TestCompany.company_name

        self.logger.info(f"Expected Company Name : {expected_result}")
        self.logger.info(f"Actual Company Name   : {actual_result}")

        AssertionHelper.verify_equal(
            expected_result,
            actual_result,
            "Verify created company is displayed correctly."
        )

        self.logger.info("Company verification completed successfully.")
        self.logger.info("========== COMPANY_007 PASSED ==========")


    @allure.description("Verify company count increases after creating a new company")
    @allure.title("COMPANY_008 - Verify Company Count After Creation")
    @pytest.mark.smoke
    def test_08_count_company_after_creation(self):

        self.logger.info("========== COMPANY_008 STARTED ==========")

        fake = Faker()

        company_name = fake.company()
        company_email = fake.email()

        company_page = self.login_and_navigate()

        # Count before creation
        before_count = company_page.get_company_count()

        self.logger.info(f"Company Count Before Creation : {before_count}")

        # Create company
        company_page.create_company(
            company_name,
            company_email
        )

        self.logger.info("Company created successfully.")

        # Verify company
        actual_name = company_page.verify_company_details(company_name)

        AssertionHelper.verify_equal(
            company_name,
            actual_name,
            "Verify company created successfully."
        )

        # Count after creation
        after_count = company_page.get_company_count()

        self.logger.info(f"Company Count After Creation : {after_count}")

        AssertionHelper.verify_equal(
            before_count + 1,
            after_count,
            "Verify company count incremented."
        )

        self.logger.info("Company count increment verified.")
        self.logger.info("========== COMPANY_008 PASSED ==========")


    @allure.description("Verify company count decrements after deleting a company")
    @allure.title("COMPANY_009 - Verify Company Count After Deletion")
    @pytest.mark.smoke
    def test_09_count_company_after_deletion(self):

        self.logger.info("========== COMPANY_009 STARTED ==========")

        fake = Faker()

        company_name = fake.company()
        company_email = fake.email()

        company_page = self.login_and_navigate()

        # Count before creation
        before_count = company_page.get_company_count()

        self.logger.info(f"Company Count Before Creation : {before_count}")

        # Create company
        company_page.create_company(
            company_name,
            company_email
        )

        self.logger.info("Company created successfully.")

        # Verify company
        actual_name = company_page.verify_company_details(company_name)

        AssertionHelper.verify_equal(
            company_name,
            actual_name,
            "Verify company created successfully."
        )

        # Count after creation
        count_after_creation = company_page.get_company_count()

        self.logger.info(
            f"Company Count After Creation : {count_after_creation}"
        )

        AssertionHelper.verify_equal(
            before_count + 1,
            count_after_creation
        )

        # Delete company
        self.logger.info(f"Deleting Company : {company_name}")

        company_page.delete_company(company_name)

        popup = company_page.get_popup_text()

        AssertionHelper.verify_contains(
            "Company deleted",
            popup
        )

        company_page.wait_for_popup_to_clear()

        self.logger.info("Company deleted successfully.")

        # Count after deletion
        after_count = company_page.get_company_count()

        self.logger.info(
            f"Company Count After Deletion : {after_count}"
        )

        AssertionHelper.verify_equal(
            count_after_creation - 1,
            after_count,
            "Verify company count decremented."
        )

        self.logger.info("Company count decrement verified.")
        self.logger.info("========== COMPANY_009 PASSED ==========")


    @allure.description("Verify company's email field is blocked/read-only")
    @allure.title("COMPANY_010 - Verify company's email field is blocked/read-only")
    @pytest.mark.smoke
    def test_10_verify_company_email_readonly(self):

        self.logger.info("========== COMPANY_010 STARTED ==========")

        fake = Faker()

        company_name = fake.company()
        company_email = fake.email()

        company_page = self.login_and_navigate()

        self.logger.info(
            f"Generated Company -> Name: {company_name}, Email: {company_email}"
        )

        # Create Company
        company_page.create_company(
            company_name,
            company_email
        )

        self.logger.info("Company created successfully.")

        # Open Edit Company
        company_page.click_edit_company(company_name)

        self.logger.info("Edit Company page opened.")

        # Verify Email field is not editable
        editable = company_page.is_field_editable(
            CompanyLocators.EMAIL_ID
        )

        self.logger.info(f"Email Field Editable: {editable}")

        AssertionHelper.verify_false(
            editable,
            "Verify company email field is blocked/read-only."
        )

        self.logger.info("Verified company email field is read-only.")
        self.logger.info("========== COMPANY_010 PASSED ==========")