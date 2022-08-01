import logging

def get_logger(name):
    logger = logging.getLogger(name)
    FORMAT = '%(levelname)s | %(name)s:%(lineno)s | %(message)s'
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(FORMAT))
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger