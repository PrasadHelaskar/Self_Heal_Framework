import time
import os
import pytest
from dotenv import load_dotenv

from utils.logger import Logger
from pages.login_page import LoginPage

log=Logger().get_logger(__name__)

class Test_Login():
    @pytest.mark.order(1)
    def test_login(self,driver):
        load_dotenv(".config/.env")
        login_page=LoginPage(driver)
        driver.get(os.getenv("URL"))
        login_page.enter_username("username","locked_out_user")
        login_page.enter_username("password","secret_sauce")
        login_page.click_login("login_button")


