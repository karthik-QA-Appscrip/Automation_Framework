import allure
import pytest

from pages.loginPage import LoginPage
from utilities.configReader import ConfigReader
from utilities.jsonReader import JsonReader
from constants import messages
from utilities.BaseTest import BaseTest
from utilities.TestDataManager import TestData



@allure.feature("Login")
class TestLogin(BaseTest):

    @allure.description("Verify login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Login Functionality")
    @pytest.mark.smoke
    @allure.title("LOGIN_001 - Verify login with valid credentials")
    def test_login_valid_credentials(self, driver): 

        login = LoginPage(driver)

        self.logger.info(f"Username : {TestData.valid_username}")
        self.logger.info(messages.ENTER_VALID_PASSWORD)
        print(TestData.valid_username)
        print(TestData.valid_password)

        # login.login(valid_username, valid_password)
        login.login(
            TestData.valid_username,
            TestData.valid_password
        )

        self.logger.info(messages.VERIFY_SUCCESSFUL_LOGIN)

        assert login.is_popup_displayed(), \
            messages.POPUP_NOT_DISPLAYED_AFTER_VALID_LOGIN

        self.logger.info(login.get_popup_message())

    @allure.story("Invalid Login")
    @allure.title("LOGIN_002 - Verify login with invalid username")
    def test_login_invalid_credentials(self, driver):

        login = LoginPage(driver)

        # login.login(invalid_username, valid_password)
        login.login(
            TestData.invalid_username,
            TestData.valid_password
        )

        self.logger.info(messages.VERIFY_INVALID_LOGIN)

        assert login.is_popup_displayed(), \
            messages.POPUP_NOT_DISPLAYED_AFTER_INVALID_LOGIN

        assert messages.EMAIL_NOT_FOUND in login.get_popup_message()

        self.logger.info(login.get_popup_message())


    @allure.story("Invalid Login")
    @allure.title("LOGIN_003 - Verify login with invalid password")
    def test_login_invalid_password(self, driver):

        login = LoginPage(driver)

        login.login(TestData.valid_username, TestData.invalid_password)

        self.logger.info(messages.VERIFY_INVALID_PASSWORD)

        assert login.is_popup_displayed(), \
            messages.POPUP_NOT_DISPLAYED_AFTER_INVALID_PASSWORD

        self.logger.info(login.get_popup_message())

    @allure.story("Invalid Login")
    @allure.title("LOGIN_004 - Verify login with blank credentials")
    def test_login_blank_credentials(self, driver):

        login = LoginPage(driver)

        self.logger.info(messages.ENTER_BLANK_USERNAME_PASSWORD)

        login.click_continue_with_password()
        login.enter_username("")
        login.enter_password("")

        assert not login.is_click_login_button_enabled()

    @allure.story("Invalid Login")
    @allure.title("LOGIN_005 - Verify login with valid username and blank password")
    def test_login_blank_password(self, driver):

        login = LoginPage(driver)

        self.logger.info(messages.ENTER_VALID_USERNAME_BLANK_PASSWORD)

        login.click_continue_with_password()
        login.enter_username(TestData.valid_username)
        login.enter_password("")

        assert not login.is_click_login_button_enabled()


    @allure.story("Invalid Login")
    @allure.title("LOGIN_006 - Verify login with blank username and valid password")
    def test_login_blank_username(self, driver):

        login = LoginPage(driver)

        self.logger.info(messages.ENTER_BLANK_USERNAME_VALID_PASSWORD)

        login.click_continue_with_password()
        login.enter_username("")
        login.enter_password(TestData.valid_password)

        assert not login.is_click_login_button_enabled()

    @allure.story("Invalid Login")
    @allure.title("LOGIN_007 - Verify login with invalid username")
    def test_login_invalid_username(self, driver):

        login = LoginPage(driver)

        login.login(
            TestData.invalid_username,
            TestData.valid_password
        )

        self.logger.info(messages.VERIFY_INVALID_USERNAME)
        self.logger.info(f"Username : {TestData.invalid_username}")
        self.logger.info(f"Password : {TestData.valid_password}")
        self.logger.info(messages.CHECKING_POPUP)

        assert login.is_popup_displayed(), \
            messages.POPUP_NOT_DISPLAYED_AFTER_INVALID_USERNAME

        assert messages.EMAIL_NOT_FOUND in login.get_popup_message()

        self.logger.info(login.get_popup_message())


    @allure.story("Email Validation")
    @allure.title("LOGIN_008 - Verify login with invalid email format")
    @pytest.mark.parametrize("test_data", TestData.invalid_email_cases)
    def test_login_invalid_email_format(self, driver, test_data):

        login = LoginPage(driver)

        login.click_continue_with_password()

        login.enter_username(test_data["email"])
        login.enter_password(TestData.valid_password)

        actual_error = login.get_invalid_email_error_message()

        assert actual_error == test_data["expectedError"].strip(), \
            f"Expected error: '{test_data['expectedError']}', but got: '{actual_error}'"

        self.logger.info(f"Verified Email : {test_data['email']}")
        self.logger.info(f"Expected Error : {test_data['expectedError']}")
        self.logger.info(f"Actual Error : {actual_error}")
