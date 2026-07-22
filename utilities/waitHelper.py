from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.configReader import ConfigReader


class WaitUtils:

    def __init__(self, driver):
        self.driver = driver

        config = ConfigReader()
        timeout = config.get_timeout()

        self.wait = WebDriverWait(driver, timeout)

    def wait_for_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_presence(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )