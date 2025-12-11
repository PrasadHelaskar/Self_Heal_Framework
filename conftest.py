import pytest

from selenium import webdriver
from utils.logger import Logger

log=Logger().get_logger(__name__)

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
    chrome_options.add_argument("--force-device-scale-factor=0.7")
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_cdp_cmd("Page.enable", {})
    driver.execute_cdp_cmd('Network.enable', {})
    driver.execute_cdp_cmd("Debugger.setSkipAllPauses", {"skip": True})
    driver.execute_cdp_cmd("Page.setLifecycleEventsEnabled",{"enabled": True})
    # driver.execute_cdp_cmd("Emulation.setPageScaleFactor", {"pageScaleFactor": 0.8})
    driver.maximize_window()

    log.info("Webdriver is Initited with the Browser Window")

    yield driver

    log.info("The Execution is Completed and returned to conftest fixture clearing the instances\n")
    driver.quit()