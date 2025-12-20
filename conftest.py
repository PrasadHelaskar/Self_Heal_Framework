import time
import pytest

from selenium import webdriver
from utils.logger import Logger

log=Logger().get_logger(__name__)

# def pytest_configure(config):
#     config._metadata["Project"] = "Self Healing Automation Framework"
#     config._metadata["Author"] = "Prasad Helaskar"

@pytest.fixture(scope="session")
def driver():

    """
    Provides a Selenium WebDriver instance configured for test execution.

    Returns:
        WebDriver: A configured Selenium WebDriver instance.

    The driver is pre-configured to handle common settings for test automation and should be properly
    closed after use to prevent resource leaks.
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/usr/bin/google-chrome"
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--window-size=1920,1080")
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    time.sleep(1)
    driver.execute_cdp_cmd("Page.enable", {})
    driver.execute_cdp_cmd('Network.enable', {})
    driver.execute_cdp_cmd("Page.setLifecycleEventsEnabled",{"enabled": True})
    driver.maximize_window()

    log.info("Webdriver is Initited with the Browser Window")

    yield driver

    log.info("The Execution is Completed and returned to conftest fixture clearing the instances\n")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Attach a browser screenshot to the pytest-html report when a test fails
        during execution and a WebDriver fixture is available.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            screenshot = driver.get_screenshot_as_base64()
            pytest_html = item.config.pluginmanager.getplugin("html")
            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.png(screenshot))
            report.extras = extra