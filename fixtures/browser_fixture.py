import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utilities.DriverFactory import DriverFactory

from utilities.configReader import ConfigReader


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser Name"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run Browser in Headless Mode"
    )


@pytest.fixture(scope="function")
def driver(request):
    config = ConfigReader()

    browser = request.config.getoption("--browser")

    if browser is None:
        browser = config.get_browser()

    headless = request.config.getoption("--headless")

    driver = DriverFactory.get_driver(
        browser=browser,
        headless=headless
    )

    driver.maximize_window()
    driver.implicitly_wait(config.get_timeout())
    driver.get(config.get_url())

    yield driver

    driver.quit()