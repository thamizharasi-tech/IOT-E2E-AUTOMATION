import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=r'..\stability.log',
                            format='%(asctime)s %(levelname)s %(filename)s %(name)s ' \
                                   '%(lineno)s "%(message)s"', datefmt='%Y-%m-%d %a %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
