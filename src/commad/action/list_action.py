"""list."""
import os
from src.logger.logger import logger


class list_action(logger):
    def __init__(self):
        logger.__init__(self)
        self.path_pwd = os.path.dirname(os.path.abspath(__file__))
        self.path_hosts_custom = self.path_pwd + '/../../../hosts_files/'

    def list_of_file(self):
        try:
            dir_hosts = self.path_hosts_custom
            list_of_file = os.listdir(str(dir_hosts))
            return list_of_file
        except Exception as e:
            self.log_warning(e)
            return False
