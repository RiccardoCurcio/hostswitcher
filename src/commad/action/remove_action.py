"""remove."""
import os
from src.logger.logger import logger
from src.commad.action.origin_action import origin_action


class remove_action(logger):
    def __init__(self):
        logger.__init__(self)
        self.path_pwd = os.path.dirname(os.path.abspath(__file__))
        self.path_hosts_custom = self.path_pwd + '/../../../hosts_files/'
        self.path_hosts = '/etc/hosts'
        self.file_name = 'hosts.default'
        self.return_dict = dict(
            {
                "status": 0,
                "msg": None
            }
        )

    def remove_file(self, origin=None):
        try:
            if origin is None:
                file_selcted = self.__select_origin()
            else:
                file_selcted = 'hosts.' + origin
            file_path = self.path_hosts_custom + file_selcted
            while True:
                question = ' Do you want remove ' + file_selcted + '? (yes/no)'
                resp = input(question)
                if resp == 'yes':
                    try:
                        os.remove(file_path)
                        msg = '\033[1m' + file_selcted + '\033[0;0m removed!'
                        return self.__set_return(0, msg)
                    except Exception as e:
                        self.log_warning(e)
                        file_s = file_selcted
                        msg = '\033[1m' + file_s + '\033[0;0m not removed!'
                        return self.__set_return(-1, msg, e)
                if resp == 'no':
                    msg = '\033[1m' + file_selcted + '\033[0;0m not removed!'
                    return self.__set_return(0, msg)
        except Exception as e:
            self.log_warning(e)
            return False

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
