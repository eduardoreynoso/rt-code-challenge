import logging

import settings


def setup_logger(name):
    """
    Configures a logger object
    :return: A logger object ready to use
    """
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(settings.DEBUG_LEVEL)
    return logger
