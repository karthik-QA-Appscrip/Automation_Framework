from pages.basePage import BasePage
from locators.loginLocators import LoginLocators


class LoginPage(BasePage):

    def click_continue_with_password(self):
        self.click(LoginLocators.CONTINUE_WITH_PASSWORD)

    def enter_username(self, username):
        self.enter_text(LoginLocators.USERNAME, username)

    def enter_password(self, password):
        self.enter_text(LoginLocators.PASSWORD, password)

    def click_login(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    def login(self, username, password):
        self.click_continue_with_password()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_invalid_credentials_message_displayed(self):
        return self.is_displayed(LoginLocators.INVALID_CREDENTIALS_MESSAGE)

    def get_error_message(self):
        return self.get_text(LoginLocators.INVALID_CREDENTIALS_MESSAGE)

    def is_click_login_button_enabled(self):
        return self.is_enabled(LoginLocators.LOGIN_BUTTON)

    def is_popup_displayed(self):
        return self.is_displayed(LoginLocators.POPUP)

    def is_error_displayed(self):
        return self.is_displayed(LoginLocators.ERROR_MESSAGE)

    def get_popup_message(self):
        return self.get_text(LoginLocators.POPUP)

    def click_close_button(self):
        self.click(LoginLocators.CLOSE_BUTTON)

    def get_error_popup_message(self):
        return self.get_text(LoginLocators.ERROR_POPUP)

    def get_invalid_email_error_message(self):
        return self.get_text(LoginLocators.INVALID_EMAIL_ERROR_MESSAGE)