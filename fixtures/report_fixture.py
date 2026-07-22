import allure
import pytest
from pytest_html import extras

from utilities.logger import Logger
from utilities.screenshot import Screenshot

logger = Logger.get_logger()


# ------------------------------
# Log Test Start
# ------------------------------
def pytest_runtest_logstart(nodeid, location):
    logger.info(f"STARTED : {nodeid}")


# ------------------------------
# Log Test Finish
# ------------------------------
def pytest_runtest_logfinish(nodeid, location):
    logger.info(f"FINISHED : {nodeid}")


# ------------------------------
# Screenshot on Failure
# ------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    logger.info("=" * 60)
    logger.info(f"TEST   : {item.name}")
    logger.info(f"STATUS : {report.outcome.upper()}")
    logger.info("=" * 60)

    if report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            path = Screenshot.capture(driver, item.name)

            logger.error(f"Failure Screenshot Saved : {path}")

            if not hasattr(report, "extras"):
                report.extras = []

            report.extras.append(extras.image(path))

            allure.attach.file(
                path,
                name=item.name,
                attachment_type=allure.attachment_type.PNG
            )