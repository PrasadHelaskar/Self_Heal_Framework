from utils.base_methods import BaseMethods
from core.self_healing_engine import Self_Healing_Engine
from core.smart_locator import SmartLocators

class LoginPage(BaseMethods):

    def __init__(self, driver):
        page_name = "login_page"      
        smart_locators=SmartLocators(page_name)
        healing = Self_Healing_Engine(driver, smart_locators)
        super().__init__(driver, healing)

    def enter_username(self, element_name, username):
        self.send_keys(element_name,username)

    def enter_password(self, element_name, password):
        self.send_keys(element_name,password)

    def click_login(self, element_name):
        self.click(element_name)