"""logger."""
import logging
from logging.config import fileConfig

fileConfig('src/logger/logging_config.ini')


class logger:
    """crudlogger."""
    def __init__(self):
        self.log = logging.getLogger("Host-switcher")
        pass

    def log_info(self, obj):
        self.log.info('%s', obj)
        return True

    def log_error(self, obj):
        self.log.error('%s', obj)
        return True

    def log_debug(self, obj):
        self.log.debug('%s', obj)
        return True

    def log_warning(self, obj):
        self.log.warning('%s', obj)
        return True
