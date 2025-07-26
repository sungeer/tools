import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('app.log')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def handle_uncaught_exception(exc_type, exc_value, exc_traceback):
    logger.critical(
        'Uncaught exception, application will terminate.',
        exc_info=(exc_type, exc_value, exc_traceback),
    )


sys.excepthook = handle_uncaught_exception


def divide(a, b):
    return a / b


def main():
    logger.info('Application start')
    a = 10
    b = 0
    logger.info(divide(a, b))
    logger.info('Application end')


if __name__ == '__main__':
    main()
