"""list."""
import os
import filecmp
from src.logger.logger import logger


class list_action(logger):
    def __init__(self):
        logger.__init__(self)
        self.path_pwd = os.path.dirname(os.path.abspath(__file__))
        self.path_hosts_custom = self.path_pwd + '/../../../hosts_files/'
        self.path_hosts = '/etc/hosts'

    def list_of_file(self):
        try:
            dir_hosts = self.path_hosts_custom
            list_of_file = os.listdir(str(dir_hosts))
            return list_of_file
        except Exception as e:
            self.log_warning(e)
            return False

    def in_use(self, lof=list()):
        return_list = list()
        for compare in lof:
            f1 = self.path_hosts_custom + compare
            if filecmp.cmp(f1, self.path_hosts, shallow=1) is True:

                return_list.append(str(' \033[1m' + compare + '\033[0;0m'))
            else:
                return_list.append(str(' '+compare))
        return return_list
