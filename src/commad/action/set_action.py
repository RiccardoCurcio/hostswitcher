"""set."""
import os
from src.logger.logger import logger
from src.commad.action.origin_action import origin_action
from src.lib.os_resolver import os_resolver


class set_action(logger):
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

    def set_file(self, origin=None):
        try:
            if origin is None:
                file_selcted = self.__select_origin()
            else:
                file_selcted = 'hosts.' + origin
            file_path = self.path_hosts_custom + file_selcted
            os.system("sudo cp " + file_path + " " + self.path_hosts)
            msg = '\033[1m' + file_selcted + '\033[0;0m set!'
            return self.__set_return(0, msg)
        except Exception as e:
            self.log_warning(e)
            msg = '\033[1m' + file_selcted + '\033[0;0m not set!'
            return self.__set_return(-1, msg, e)

    def __select_origin(self):
        origin_a = origin_action()
        return origin_a.select_origin()

    def __set_return(self, status=0, msg=None, error=None):
        self.return_dict.update(
            {
                "status": status,
                "msg": msg,
                "error": error
            }
        )
        return self.return_dict
