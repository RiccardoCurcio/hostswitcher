from src.logger.logger import logger


class bootstrap(logger):
    def __init__(self):
        logger.__init__(self)
        self.log_info('bootstrap app')
        pass

    def start_dep(self):
        self.log_info('start dep')
        pass
