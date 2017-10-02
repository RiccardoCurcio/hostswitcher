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
            default = self.file_name
            name = self.path_hosts_custom + default
            if os.path.exists(name) is True:
                while True:
                    qmsg = 'exists, do you want overwrite it? (yes/no)'
                    msg = default + qmsg
                    resp = input(msg)
                    if resp == 'yes':
                        shutil.copyfile(
                            hosts,
                            name
                            )
                        return True
                    if resp == 'no':
                        return False
            else:
                shutil.copyfile(
                    hosts,
                    name
                )
                return True
            return False
        except Exception as e:
            self.log_warning(e)
            return False
