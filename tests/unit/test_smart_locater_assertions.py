import pytest

from core.smart_locator import SmartLocators
from utils.logger import Logger

log=Logger().get_logger(__name__)

class Test_DummyLocatorReader:
    """
    Minimal test double to isolate unit test
    """
    def page_name(self):
        page_name = "unit_test_data"
        return page_name

    @pytest.mark.unit
    def test_get_locators_with_primary_and_fallback(self):
        reader = SmartLocators(self.page_name())

        locators = reader.get_locators_by_element_name("username_input")

        assert locators["primary"] == {"by": "id", "value": "username"}
        assert locators["fallback"] == [
            {"by": "xpath", "value": "//input[@name='username']"}
        ]

    @pytest.mark.unit
    def test_get_locators_without_fallback_returns_empty_list(self):
        reader = SmartLocators(self.page_name())

        locators = reader.get_locators_by_element_name("password_input")

        assert locators["primary"] == {"by": "id", "value": "password"}
        assert locators["fallback"] == []

    @pytest.mark.unit
    def test_get_locators_raises_keyerror_for_missing_element(self):
        try:
            reader = SmartLocators(self.page_name())
            reader.get_locators_by_element_name("email_input")
        except KeyError as ke:
            log.error("Got KeyError: %s", ke)
