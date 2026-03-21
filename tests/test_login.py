import os
import time
import json
import pytest
from dotenv import load_dotenv

from pages.login_page import LoginPage
from utils.custom_exception import InvalidUserException
from utils.logger import Logger
from utils.path_resolver import resolve_path

log=Logger().get_logger(__name__)
load_dotenv(".config/.env")

with open(resolve_path("test_data/login_data.json")) as testdatafile:
    data=json.load(testdatafile)

class Test_Login():

    def _login(self,driver,username,password)->bool:
        login_page=LoginPage(driver)
        login_page.enter_username("username",username)
        login_page.enter_username("password",password)
        login_page.click_login("login_button")
        time.sleep(2)
        return login_page.get_current_url() == "https://www.saucedemo.com/inventory.html"

    @pytest.mark.flows
    @pytest.mark.parametrize("credentials",
        [
            data["standard_user"],
        ]
    )
    def test_login_success(self,driver,credentials):
        driver.get(os.getenv("URL"))

        username=credentials["username"]
        password=credentials["password"]

        result=self._login(driver,username,password)

        if not result:
            raise InvalidUserException()


    @pytest.mark.flows
    @pytest.mark.parametrize("credentials",
        [
            data["locked_out_user"],
        ]
    )
    def test_login_failed(self,driver,credentials):
        with pytest.raises(InvalidUserException):
            driver.get(os.getenv("URL"))

            username=credentials["username"]
            password=credentials["password"]

            result=self._login(driver,username,password)

            # if not result:
            #     raise InvalidUserException()
