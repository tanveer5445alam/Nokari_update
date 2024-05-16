import logging
import inspect

class Logging_Genrator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][1]
        logger = logging.getLogger(name)
        log_file = logging.FileHandler("D:\\programming\\Nokari_profile\\Log\\Nokari.log")
        log_formate = logging.Formatter("%(asctime)s : %(filename)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        log_file.setFormatter(log_formate)
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger

