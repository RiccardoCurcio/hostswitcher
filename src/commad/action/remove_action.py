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

    def remove_file(self):
        try:
            file_selcted = self.__select_origin()
            file_path = self.path_hosts_custom + file_selcted
            while True:
                question = 'Do you want remove ' + file_selcted + '? (yes/no)'
                resp = input(question)
                if resp == 'yes':
                    try:
                        os.remove(file_path)
                    except Exception as e:
                        self.log_warning(e)
                        return False
                    return True
                if resp == 'no':
                    return False
        except Exception as e:
            self.log_warning(e)
            return False

    def __select_origin(self):
        origin_a = origin_action()
        return origin_a.select_origin()
