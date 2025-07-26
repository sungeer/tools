import sys

from tools.util_log.demo import logger


def handle_uncaught_exception(exc_type, exc_value, exc_traceback):
    logger.opt(exception=(exc_type, exc_value, exc_traceback)).critical('Critical exception, application will shutdown.')


sys.excepthook = handle_uncaught_exception
