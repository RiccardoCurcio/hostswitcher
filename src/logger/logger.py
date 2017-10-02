"""logger."""
import os
import logging
from logging.config import fileConfig


class logger:
    """crudlogger."""
    def __init__(self):
        self.path_pwd = os.path.dirname(os.path.abspath(__file__))
        self.path_log_files_custom = self.path_pwd + '/../logger/log_files/'
        directory = self.path_log_files_custom
        if not os.path.exists(directory):
            os.makedirs(directory)
        fileConfig('src/logger/logging_config.ini')
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
