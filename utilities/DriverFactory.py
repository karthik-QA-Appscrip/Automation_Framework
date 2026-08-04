from selenium import webdriver
from utilities.driver_manager import DriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser, headless=False):

        browser = browser.lower()

        if browser == "chrome":

            options = webdriver.ChromeOptions()

            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")

            driver = webdriver.Chrome(
                service=ChromeService(
                    ChromeDriverManager().install()
                ),
                options=options
            )

            DriverManager.set_driver(driver)

            return DriverManager.get_driver()

        elif browser == "edge":

            options = webdriver.EdgeOptions()

            if headless:
                options.add_argument("--headless=new")

            driver = webdriver.Edge(
                service=EdgeService(
                    EdgeChromiumDriverManager().install()
                ),
                options=options
            )

            DriverManager.set_driver(driver)

            return DriverManager.get_driver()

        elif browser == "firefox":

            options = webdriver.FirefoxOptions()

            if headless:
                options.add_argument("-headless")

            driver = webdriver.Firefox(
                service=FirefoxService(
                    GeckoDriverManager().install()
                ),
                options=options
            )

            DriverManager.set_driver(driver)

            return DriverManager.get_driver()

        raise ValueError(f"Unsupported Browser : {browser}")