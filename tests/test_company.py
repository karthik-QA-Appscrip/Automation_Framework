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


class TestCompany(BaseTest):

    company_name = ""
    company_email = ""

    def login_and_navigate(self):
        login = LoginPage()
        company_page = CompanyPage()
        test_data = TestData()
        wait_utils = login.wait

        current_url = login.driver.current_url
        login.login(test_data.valid_username, test_data.valid_password)

        wait_utils.wait_for_url_to_change(current_url)
        time.sleep(3)

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

    