"""list."""
import os
import time
import filecmp
from src.logger.logger import logger


class list_action(logger):
    def __init__(self):
        logger.__init__(self)
        self.path_pwd = os.path.dirname(os.path.abspath(__file__))
        self.path_hosts_custom = self.path_pwd + '/../../../hosts_files/'
        self.path_hosts = '/etc/hosts'
        self.return_dict = dict(
            {
                "status": 0,
                "msg": None
            }
        )

    def list_of_file(self):
        try:
            dir_hosts = self.path_hosts_custom
            list_of_file = os.listdir(str(dir_hosts))
            return self.__set_return(0, None, None, list_of_file)
            # return list_of_file
        except Exception as e:
            self.log_warning(e)
            return False

    def in_use(self, lof=list()):
        return_list = list()
        dir_hosts = self.path_hosts_custom
        for compare in lof:
            f1 = self.path_hosts_custom + compare
            a = os.stat(os.path.join(dir_hosts, compare))
            if filecmp.cmp(f1, self.path_hosts, shallow=1) is True:
                # str('\033[1m' + compare + '\033[0;0m'),
                return_list.append(
                    [
                        str('*' + compare),
                        time.ctime(a.st_atime),
                        time.ctime(a.st_ctime)
                    ]
                )
            else:
                return_list.append(
                    [
                        compare,
                        time.ctime(a.st_atime),
                        time.ctime(a.st_ctime)
                    ]
                )

        return return_list

    def __set_return(self, status=0, msg=None, error=None, list_return=list):
        self.return_dict.update(
            {
                "status": status,
                "msg": msg,
                "list": list_return,
                "error": error
            }
        )
        return self.return_dict
