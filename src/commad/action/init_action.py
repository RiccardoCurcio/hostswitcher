"""Init."""
import os
import shutil
from src.logger.logger import logger
from src.lib.os_resolver import os_resolver


class init_action(logger):
    def __init__(self):
        logger.__init__(self)
        self.osr = os_resolver()
        self.path_pwd = os.path.dirname(os.path.abspath(__file__))
        self.path_hosts_custom = self.path_pwd + '/../../../hosts_files/'
        self.path_hosts = self.osr.get_hosts_path()
        self.file_name = 'hosts.default'
        self.return_dict = dict(
            {
                "status": 0,
                "msg": None
            }
        )

    def copy_current_host_file(self):
        try:
            hosts = self.path_hosts
            default = self.file_name
            name = self.path_hosts_custom + default
            if os.path.exists(name) is True:
                while True:
                    qmsg = ' exists, do you want overwrite it? (yes/no)'
                    msg = ' \033[1m' + default + '\033[0;0m' + qmsg
                    resp = input(msg)
                    if resp == 'yes':
                        shutil.copyfile(hosts, name)
                        msg = '\033[1m' + default + '\033[0;0m overwrited!'
                        return self.__set_return(0, msg)
                    if resp == 'no':
                        msg = '\033[1m' + default + '\033[0;0m not overwrited!'
                        return self.__set_return(0, msg)
            else:
                shutil.copyfile(hosts, name)
                msg = 'Init completed!'
                return self.__set_return(0, msg)
        except Exception as e:
            self.log_warning(e)
            msg = '[ERROR] Init not completed!'
            return self.__set_return(-1, msg)

    def __set_return(self, status=0, msg=None, error=None):
        self.return_dict.update(
            {
                "status": status,
                "msg": msg,
                "error": error
            }
        )
        return self.return_dict
