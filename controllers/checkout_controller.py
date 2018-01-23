from selenium.webdriver.common.by import By

from classes.selenium_operations import SeleniumOperations
from classes.helpers import setup_logger

logger = setup_logger(__name__)


class CheckoutController(SeleniumOperations):
    """
    A page object to interact with the search component
    """
    # A reference to the web driver
    driver = None

    # Locators
    LOCATORS = {
        'checkout_view': (By.ID, 'cart-content'),
        'total_price': (By.CLASS_NAME, 'listing-footer__pricing-value'),
        'cart_item_titles': (By.CLASS_NAME, 'item-title')
    }

    def __init__(self, driver):
        super(CheckoutController, self).__init__(driver)
        self.driver = driver

    def is_checkout_page(self):
        """
        Checks if we are in the checkout page
        :return: True if we are, otherwise False
        """
        return bool(self.get_elements(self.LOCATORS['checkout_view']))

    def get_total_price(self):
        """
        Gets the total price of all of the cart items
        :return:
        """
        return self.get_element(self.LOCATORS['total_price']).text

    def item_in_cart(self, item_title):
        """
        Checks if the given item_title is present in the items on the cart
        :param item_title:
        :return:
        """
        return item_title in [items.text for items in self.get_elements(self.LOCATORS['cart_item_titles'])]
