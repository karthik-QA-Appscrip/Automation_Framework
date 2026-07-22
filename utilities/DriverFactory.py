from selenium import webdriver
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

            return webdriver.Chrome(
                service=ChromeService(
                    ChromeDriverManager().install()
                ),
                options=options
            )

        elif browser == "edge":

            options = webdriver.EdgeOptions()

            if headless:
                options.add_argument("--headless=new")

            return webdriver.Edge(
                service=EdgeService(
                    EdgeChromiumDriverManager().install()
                ),
                options=options
            )

        elif browser == "firefox":

            options = webdriver.FirefoxOptions()

            if headless:
                options.add_argument("-headless")

            return webdriver.Firefox(
                service=FirefoxService(
                    GeckoDriverManager().install()
                ),
                options=options
            )

        raise ValueError(f"Unsupported Browser : {browser}")