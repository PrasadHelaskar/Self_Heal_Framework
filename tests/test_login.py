import time
import json
import os
import pytest
from dotenv import load_dotenv

from utils.logger import Logger
from pages.login_page import LoginPage

log=Logger().get_logger(__name__)

with open("/mnt/k/self_heal_framework/code/test_data/login_data.json") as  testdatafile:
    data=json.load(testdatafile)

class Test_Login():
    @pytest.mark.order(1)
    @pytest.mark.parametrize("credentials",[
        data["valid_data"],
        data["locked_out_user_invalid_data"]
    ]
)
    def test_login(self,driver,credentials):
        load_dotenv(".config/.env")
        login_page=LoginPage(driver)
        driver.get(os.getenv("URL"))
        
        username=credentials["username"]
        password=credentials["password"]
        
        def login(username,password)->bool:

            login_page.enter_username("username",username)
            login_page.enter_username("password",password)
            login_page.click_login("login_button")
            time.sleep(2)
            
            return login_page.get_current_url() == "https://www.saucedemo.com/inventory.html"
        
        result=login(username,password)

        log.info("Login Results : %s",result)