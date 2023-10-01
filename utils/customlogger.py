import logging


class LogGen:
    logger = None

    @staticmethod
    def loggen():
        if LogGen.logger is None:
            logging.basicConfig(filename=r"C:\Users\keert\PycharmProjects\Restful_API_Project\logs\Restful_API.log",
                                format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            handler = logging.FileHandler(r"C:\Users\keert\PycharmProjects\Restful_API_Project\logs\Restful_API.log", mode='w')
            handler.setFormatter(logging.Formatter('%(asctime)s: %(levelname)s: %(message)s'))

            # Create a console handler and set its log level to INFO
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

            LogGen.logger = logging.getLogger()
            LogGen.logger.addHandler(handler)
            LogGen.logger.addHandler(console_handler)
            LogGen.logger.setLevel(logging.INFO)
        return LogGen.logger


def test_print_logs():
    logger = LogGen.loggen()  # Use the logger obtained from LogGen.loggen()
    logger.debug("This is a debug message")  # Debug level is not shown in the console handler
    logger.info("This is an info message")  # This will be shown in the console handler
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    # No need to return the logger; it's obtained using LogGen.loggen()


if __name__ == "__main__":
    test_print_logs()  # Entry point of the program
