from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains

from utils.logger import Logger
from core.self_healing_engine import Self_Healing_Engine

log=Logger().get_logger(__name__)

class BaseMethods:

    def __init__(self,driver,self_healing_engine:Self_Healing_Engine=None):
        """
            :param driver: Selenium WebDriver instance
            :param healing_engine: SelfHealingEngine instance
        """
        self.driver=driver
        self.wait=WebDriverWait(driver, timeout=10)
        self.healing=self_healing_engine

# Element Finders

    def find_element_wait(self, element_name):
        '''
        Waits until the element located by the given locator is visible and returns it.
        
        :param element_name: Element name matching with josn file 
        
        Returns:
            WebElement: The visible web element found
        '''
        try:
            locator=self.healing.check_locator_validity(element_name)
            element=self.wait.until(EC.visibility_of_element_located(locator))
            return element

        except NoSuchElementException as e:
            log.exception("No Element found: %s",e)

    def find_elements_wait(self, element_name):
        """
        Waits until all elements located by the given locator are visible and returns them.
        
        param element_name: Element name matching with josn file
        
        Returns:
            list[WebElement]: A list of visible web elements found.
        """
        try:
            locator=self.healing.check_locator_validity(element_name)
            elements=self.wait.until(EC.visibility_of_all_elements_located(locator))
            return elements

        except NoSuchElementException as e:
            log.exception("No Element found: %s",e)

    def find_element_wait_presence(self, element_name):
        """
        Waits until all elements located by the given locator are visible and returns them.

        param element_name: Element name matching with josn file

        Returns:
            list[WebElement]: A list of visible web elements found.
        """
        try:
            locator=self.healing.check_locator_validity(element_name, require_visibility=False)
            element=self.wait.until(EC.presence_of_element_located(locator))
            return element

        except NoSuchElementException as e:
            log.exception("No Element found: %s",e)

    def find_elements_wait_presence(self, element_name):
        """
        Waits until all elements located by the given locator are visible and returns them.

        param element_name: Element name matching with josn file

        Returns:
            list[WebElement]: A list of visible web elements found.
        """
        try:
            locator=self.healing.check_locator_validity(element_name, require_visibility=False)
            element=self.wait.until(EC.presence_of_all_elements_located(locator))
            return element

        except NoSuchElementException as e:
            log.exception("No Element found: %s",e)


# Action Methods (Click)
    def click(self, element_name):
        """
        Waits for visibility of the element and clicks on it.

        Parameters:
            locator (tuple): Locator strategy and locator value.
        """
        try:
            element = self.find_element_wait(element_name)
            element.click()

        except ElementClickInterceptedException as e:
            log.error("Failed to interact with the elemet in the view port")
            log.info(e)


    def click_presence(self, element_name):
        """
        Waits for presence of the element and clicks on it.

        Parameters:
            locator (tuple): Locator strategy and locator value.
        """
        try:
            element = self.find_element_wait_presence(element_name)
            element.click()

        except ElementClickInterceptedException as e:
            log.error("Failed to interact with the elemet in the view port")
            log.info(e)

# Action Methods (Send keys)
    def send_keys(self, element_name, text):
        """
        Waits for the element, clears it, and sends the specified text.

        Parameters:
            locator (tuple): Locator strategy and locator value.
            text (str): Text to input into the element.
        """
        try:
            element = self.find_element_wait(element_name)
            element.clear()
            element.send_keys(text)

        except ElementClickInterceptedException as e:
            log.error("Failed to interact with the elemet in the view port")
            log.info(e)

# Action Methods (get text)
    def get_text(self, element_name):
        """
        Retrieves the visible text of the located element.

        Parameters:
            locator (tuple): Locator strategy and locator value.

        Returns:
            str: Text content of the element.
        """
        try:
            element = self.find_element_wait(element_name)
            element_text = element.text
            return  element_text if element_text else None

        except NoSuchElementException as e:
            log.error("Failed to Locate the elemet in the view port")
            log.info(e)

# Action Methods (check visibility)
    def is_visible(self, element_name):
        """
        Checks whether the element located by the given locator is visible.

        Parameters:
            locator (tuple): Locator strategy and locator value.

        Returns:
            str or bool: "True"/"False" string if found, otherwise False if an exception occurs.
        """
        try:
            element = self.find_element_wait(element_name)
            op = element.is_displayed()
            return str(op) if op else False
        except ElementNotVisibleException as e :
            log.error("Failed to Locate the elemet in the view port")
            log.info(e)

# Action Methods (clear the text boxes)
    def clear_element(self, element_name):
        """
        Waits for the element and clears its content.

        Parameters:
            locator (tuple): Locator strategy and locator value.
        """
        try:
            element = self.find_element_wait(element_name)
            element.clear()
        except NoSuchElementException as e :
            log.error("Failed to Locate the elemet in the view port")
            log.info(e)

# Action Methods (get current url)
    def get_url(self):
        """
        Retrieves the current URL of the active browser window.

        Returns:
            str: The current URL loaded in the browser.
        """
        url = self.driver.current_url
        return url if url else None

# Action Methods (get required attributes of element)
    def get_attribute(self,element_name,attribute):
        """
        Retrieve the value of a specified attribute from a web element.

        Args:
            locator (tuple): A tuple containing the Selenium By strategy and the locator string.
                            Example: (By.XPATH, "//input[@name='email']")
            attribute (str): The name of the attribute whose value needs to be fetched.
                            Example: "type", "name", "value"

        Returns:
            str: The value of the specified attribute, or None if the attribute is not present.

        Raises:
            TimeoutException: If the element is not found within the wait time defined in `find_element_wait`.
        """
        try:
            element = self.find_element_wait(element_name)
            value=element.get_attribute(attribute)
            return value if value else None

        except NoSuchElementException as e :
            log.error("Failed to Locate the elemet in the view port")
            log.info(e)

# Action Methods (action class: hover)
    def hover_on_elemet(self,element_name):
        """
        Hover the mouse pointer over a web element.

        This method uses Selenium's ActionChains to move the mouse cursor
        to the specified web element located by the given locator.
        It is typically used to trigger hover effects such as dropdowns
        or tooltips.

        Args:
            locator (tuple): A locator tuple (By, value) used to identify the element.

        Returns:
            None
        """
        try:
            actions=ActionChains(self.driver)
            actions.move_to_element(self.find_element_wait(element_name)).perform()

        except (NoSuchElementException,ElementClickInterceptedException) as e :
            log.error("Failed to Locate the elemet in the view port")
            log.info(e)

# additional waits for special conditions
    def page_wait(self):
        """
        Waits until the page's document.readyState is 'complete'.

        This ensures that the entire page, including all dependent resources,
        has finished loading before proceeding.
        """
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

# Action Methods (scrolling)
    def scroll_till_element(self, element_name):
        """
        Scrolls the web page until the specified element is visible in the viewport.

        Args:
            locator (tuple): A tuple containing the locator strategy and locator value
                            (e.g., (By.ID, "element_id")) used to identify the element.

        Returns:
            None: This method performs a scroll action and does not return a value.

        Raises:
            TimeoutException: If the element is not found within the wait period.
            NoSuchElementException: If the element cannot be located on the page.

        Example:
            self.scrollTillElemet((By.XPATH, "//div[@id='target']"))
        """
        element = self.find_element_wait_presence(element_name)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)