from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
from selenium.common.exceptions import StaleElementReferenceException

import settings
from classes.helpers import setup_logger

logger = setup_logger(__name__)


class SeleniumOperations:
    """
    Helper class that uses built in conditionals to facilitate common operations with page elements
    """

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, timeout=settings.SELENIUM['SELENIUM_TIMEOUT']):
        """
        Retrieves an element by the given locator
        Checks if the element is present in the DOM and later if the element is visible (in the viewport)
        :param locator:
        :param timeout:
        :return:
        """
        element = WebDriverWait(self.driver, timeout).until(
            conditions.presence_of_element_located(locator))
        WebDriverWait(self.driver, timeout).until(
            conditions.visibility_of(element))
        return element

    def get_elements(self, locator):
        """
        Retrieves a collection of web elements that match the given locator
        :param locator:
        :return:
        """
        return WebDriverWait(self.driver, settings.SELENIUM['SELENIUM_TIMEOUT']).until(
            conditions.presence_of_all_elements_located(locator))
