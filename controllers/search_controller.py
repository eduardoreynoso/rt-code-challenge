from selenium.webdriver.common.by import By

from classes.selenium_operations import SeleniumOperations
import settings
from classes.helpers import setup_logger

logger = setup_logger(__name__)


class SearchController(SeleniumOperations):
    """
    A page object to interact with the search component
    """
    # A reference to the web driver
    driver = None

    # Locators
    LOCATORS = {
        'dismiss_subscribe_modal': (By.XPATH, '//*[@data-track="Close"]'),
        'search_term_textfield': (By.ID, 'gh-search-input'),
        'search_button': (By.CLASS_NAME, 'header-search-button'),
        'search_results': (By.CLASS_NAME, 'list-item'),
        'search_result_item_price': (By.CLASS_NAME, 'pb-purchase-price'),
        'search_result_item_rating': (By.CLASS_NAME, 'c-review-average'),
        'search_result_item_add_to_cart': (By.CLASS_NAME, 'add-to-cart-button'),
        'go_to_cart_modal_button': (By.CLASS_NAME, 'go-to-cart')
    }

    def __init__(self, driver):
        super(SearchController, self).__init__(driver)
        self.driver = driver

    def open_search_page(self):
        """
        Opens the base url for search
        :return:
        """
        self.driver.get(settings.ENV_BASE_URL)

    def dismiss_subscribe_modal(self):
        """
        Dismisses the subscribe modal
        :return:
        """
        self.get_element(self.LOCATORS['dismiss_subscribe_modal']).click()

    def search(self, search_term):
        """
        Inputs the given search term in the search box and searches
        :param search_term: A string
        :return:
        """
        self.get_element(self.LOCATORS['search_term_textfield']).send_keys(search_term)
        self.get_element(self.LOCATORS['search_button']).click()

    def get_search_results(self):
        """
        Gets all the available search results
        :return:
        """
        results = self.get_elements(self.LOCATORS['search_results'])
        if len(results) < 1:
            logger.info('There are no search results available')
        return results

    def get_item_from_results(self, item_title):
        """
        Gets a specific item from the search results
        :param item_title: The name of the item to retrieve
        :return: A web element that can be further queried for data
        """
        results = self.get_search_results()
        for item in results:
            title = item.find_element_by_class_name('sku-title').text
            if title == item_title:
                return item
        logger.error('Item named: {} was not found in the search results'.format(item_title))
        return None

    def get_item_price(self, item_title):
        """
        Gets the price of the item taken from the search results
        :param item_title:
        :return:
        """
        item = self.get_item_from_results(item_title)

        return item.find_element(self.LOCATORS['search_result_item_price'][0],
                                 self.LOCATORS['search_result_item_price'][1]).text

    def get_item_rating(self, item_title):
        """
        Gets the rating of the item from the search results
        :param item_title:
        :return:
        """
        item = self.get_item_from_results(item_title)

        return item.find_element(self.LOCATORS['search_result_item_rating'][0],
                                 self.LOCATORS['search_result_item_rating'][1]).text

    def add_item_and_checkout(self, item_title):
        """
        Adds the item to the cart and proceeds to checkout
        :param item_title:
        :return:
        """
        item = self.get_item_from_results(item_title)

        item.find_element(self.LOCATORS['search_result_item_add_to_cart'][0],
                          self.LOCATORS['search_result_item_add_to_cart'][1]).click()
        # Adding an item to the cart will pop up a modal with an offer, click continue to checkout
        self.get_element(self.LOCATORS['go_to_cart_modal_button']).click()
