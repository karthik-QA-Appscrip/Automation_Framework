from selenium.webdriver.support.ui import Select
from utilities.waitHelper import WaitUtils
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class BasePage:

        def __init__(self, driver):
            self.driver = driver
            self.wait = WaitUtils(driver)

        def find_element(self, locator):
            return self.wait.wait_for_visibility(locator)

        def click(self, locator):
            self.wait.wait_for_clickable(locator).click()

        def enter_text(self, locator, text):
            if text is None:
                text = ""

            element = self.wait.wait_for_visibility(locator)
            element.clear()
            element.send_keys(text)

        def get_text(self, locator):
            return self.wait.wait_for_visibility(locator).text

        def is_displayed(self, locator):
            return self.wait.wait_for_visibility(locator).is_displayed()

        def is_enabled(self, locator):
            return self.wait.wait_for_visibility(locator).is_enabled()

        def clear(self, locator):
            element = self.find_element(locator)
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(Keys.BACKSPACE)

        def scroll_to_element(self, locator):
            element = self.find_element(locator)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                element
            )

        def js_click(self, locator):
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)

        def is_element_present(self, locator):
            try:
                self.find_element(locator)
                return True
            except TimeoutException:
                return False

        def find_all(self, locator):
            return self.driver.find_elements(*locator)

        def select_by_text(self, locator, text):
            Select(self.find_element(locator)).select_by_visible_text(text)

        def get_title(self):
            return self.driver.title

        def get_url(self):
            return self.driver.current_url