from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from core.smart_locator import SmartLocators
from utils.logger import Logger


log=Logger().get_logger(__name__)

class Self_Healing_Engine():

    def __init__(self,driver,smart_locators:SmartLocators):
        self.driver=driver
        self.smart_locator=smart_locators

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

        except NoSuchElementException as e:
            log.exception("No Such Element Exception :%s",e)
            return False

    def _check_locator_presence(self, locator, timeout=5):
        try:
            WebDriverWait(driver=self.driver,timeout=timeout).until(
                EC.presence_of_element_located(locator=locator)
            )

            return True

        except NoSuchElementException as e:
            log.exception("No Such Element Exception :%s",e)
            return False

    def check_locator_validity(self, element_nmae, visibility_required:bool=True):
        locators=self.smart_locator.convert_locator_to_list(element_nmae)

        for locator_dict in locators:
            locator_tuple=self._maping_tuple(locator_dict)

            if visibility_required:
                is_valid=self._check_locator_visibility(locator_tuple)
            else:
                is_valid=self._check_locator_presence(locator_tuple)

            if is_valid:
                log.info(f"Working Locator found {locator_tuple}")
                return locator_tuple
            
        raise NoSuchElementException(f"Self healing failed for : {element_nmae}")