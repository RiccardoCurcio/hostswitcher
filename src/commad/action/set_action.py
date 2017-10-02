"""set."""
import os
from src.logger.logger import logger
from src.commad.action.origin_action import origin_action


class set_action(logger):
    def __init__(self):
        logger.__init__(self)
        self.path_pwd = os.path.dirname(os.path.abspath(__file__))
        self.path_hosts_custom = self.path_pwd + '/../../../hosts_files/'
        self.path_hosts = '/etc/hosts'
        self.file_name = 'hosts.default'

    def set_file(self):
        try:
            file_selcted = self.__select_origin()
            file_path = self.path_hosts_custom + file_selcted
            os.system("sudo cp " + file_path + " " + self.path_hosts)
            return True
        except Exception as e:
            self.log_warning(e)
            return False

    def __select_origin(self):
        origin_a = origin_action()
        return origin_a.select_origin()
