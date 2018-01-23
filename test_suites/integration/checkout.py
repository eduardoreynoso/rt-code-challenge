import os

import unittest2 as unittest
from selenium import webdriver

from controllers.search_controller import SearchController
from controllers.checkout_controller import CheckoutController
from classes.helpers import setup_logger
import settings

logger = setup_logger(__name__)


class Checkout(unittest.TestCase):
    """
    This test suite covers integration test cases between search and checkout
    """

    def setUp(self):
        """
        Runs before each tests, good place to initialize a web driver
        :return:
        """
        logger.debug('Initializing web driver')
        # Initialize the web driver
        self.driver = webdriver.Chrome(os.path.join(
            os.getcwd(), settings.SELENIUM['CHROMEDRIVER_PATH']))

        # Initialize page controllers
        self.search_controller = SearchController(self.driver)
        self.checkout_controller = CheckoutController(self.driver)

    def tearDown(self):
        """
        Runs at the end of each test case, good place to quit the web driver
        :return:
        """
        logger.debug('Quiting web driver')
        self.driver.quit()

    def test_search_by_product_name(self):
        """
        This test case will search for a product given a product name, go to the checkout page and assert product info

        - Preconditions:
            A product named "Final Fantasy XV - Xbox One" with rating 4.6 and price $19.99
        - Steps:
            Open the base url
            Dismiss the email subscribe modal
            Enter the search term "Final Fantasy XV - Xbox One"
            Click search
            Click on the item on the search results to go to the checkout page
        - Expectations
            Email subscribe modal should be visible
            Search results should contain the searched item
            Assert the rating displayed 4.6
            Assert the price displayed is $19.99
            Assert that checkout page is displayed after clicking the link
            Assert the title of the item is "Final Fantasy XV - Xbox One"
            Assert that the price displayed on checkout is $19.99

        :return:
        """
        # Test data
        product_title = 'Final Fantasy XV - Xbox One'
        product_price = '$19.99'
        product_rating = '4.6'

        self.search_controller.open_search_page()
        self.search_controller.dismiss_subscribe_modal()
        self.search_controller.search(product_title)

        self.assertIsNotNone(self.search_controller.get_item_from_results(product_title))
        self.assertEqual(product_price, self.search_controller.get_item_price(product_title))
        self.assertEqual(product_rating, self.search_controller.get_item_rating(product_title))

        self.search_controller.add_item_and_checkout(product_title)

        self.assertTrue(self.checkout_controller.is_checkout_page())
        self.assertTrue(self.checkout_controller.item_in_cart(product_title))
        self.assertEqual(self.checkout_controller.get_total_price(), product_price)
