"""Init."""
import os
import shutil
from src.logger.logger import logger


class init_action(logger):
    def __init__(self):
        logger.__init__(self)
        self.path_pwd = os.path.dirname(os.path.abspath(__file__))
        self.path_hosts_custom = self.path_pwd + '/../../../hosts_files/'
        self.path_hosts = '/etc/hosts'
        self.file_name = 'hosts.default'

    def copy_current_host_file(self):
        try:
            hosts = self.path_hosts
            name = self.path_hosts_custom + self.file_name
            # print(open(hosts, 'r').read().find('#NO-ENV'))
            shutil.copyfile(
                hosts,
                name
            )
            return True
        except Exception as e:
            self.log_warning(e)
            return False
