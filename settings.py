import os
import logging

# The environment that we are going to run tests against
ENV_BASE_URL = os.environ.get('ENV_BASE_URL', 'https://www.bestbuy.com/')

# Set the debug level
if os.environ.get('DEBUG_LEVEL') == 'DEBUG':
    DEBUG_LEVEL = logging.DEBUG
else:
    DEBUG_LEVEL = logging.INFO

# Selenium configuration
SELENIUM = {
    'SELENIUM_TIMEOUT': os.environ.get('SELENIUM_TIMEOUT', 10),
    'POLL_FREQUENCY': os.environ.get('SELENIUM_POLL_FREQUENCY', 0.5),
    'CHROMEDRIVER_PATH': os.environ.get('CHROMEDRIVER_PATH', 'drivers/chromedriver')
}
