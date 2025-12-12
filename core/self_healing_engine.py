from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from core.smart_locator import SmartLocators
from utils.logger import Logger


log=Logger().get_logger(__name__)

class Self_Healing_Engine():

    def __init__(self,driver,smart_locators:SmartLocators, auto_update=True):
        self.driver=driver
        self.smart_locator=smart_locators
        self.auto_update=auto_update

    def _maping_tuple(self, locator_dict):
        mapping={
            "id":By.ID,
            "name":By.NAME,
            "xpath":By.XPATH,
            "css":By.CSS_SELECTOR
        }

        locator_strategy=mapping[locator_dict["type"].lower()]

        return (locator_strategy,locator_dict["value"])

    def _check_locator_visibility(self, locator, timeout=5):
        try:
            WebDriverWait(driver=self.driver,timeout=timeout).until(
                EC.visibility_of_element_located(locator=locator)
            )

            return True

        except TimeoutException as e:
            log.exception("Time out Exception :%s",e)
            return False

    def _check_locator_presence(self, locator, timeout=5):
        try:
            WebDriverWait(driver=self.driver,timeout=timeout).until(
                EC.presence_of_element_located(locator=locator)
            )

            return True

        except TimeoutException as e:
            log.exception("Time out Exception :%s",e)
            return False

    def check_locator_validity(self, element_name, visibility_required:bool=True):
        locators=self.smart_locator.convert_locator_to_list(element_name)

        primary_block = self.smart_locator.get_locators_by_element_name(element_name)
        primary = primary_block["primary"]

        for locator_dict in locators:
            locator_tuple=self._maping_tuple(locator_dict)

            if visibility_required:
                is_valid=self._check_locator_visibility(locator_tuple)
            
            else:
                is_valid=self._check_locator_presence(locator_tuple)
            
            if is_valid:
                log.info(f"Working locator → {locator_tuple}")

                if self.auto_update and locator_dict != primary:
                    log.info(f"Updating primary for '{element_name}' to {locator_dict}")
                    self.smart_locator.update_primary_locator(element_name, locator_dict)

                return locator_tuple
                    
            
        raise TimeoutException(f"Self healing failed for : {element_name}")