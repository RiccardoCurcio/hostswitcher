"""edit."""
import os
from src.logger.logger import logger
from src.commad.action.list_action import list_action


class edit_action(logger):
    def __init__(self):
        logger.__init__(self)
        self.path_pwd = os.path.dirname(os.path.abspath(__file__))
        self.path_hosts_custom = self.path_pwd + '/../../../hosts_files/'
        self.path_hosts = '/etc/hosts'
        self.file_name = 'hosts.default'

    def edit_file(self):
        try:
            file_selcted = self.__select_origin()
            file_path = self.path_hosts_custom + file_selcted
            os.system("vim " + file_path)
        except Exception as e:
            self.log_warning(e)
            return False

    def __select_origin(self):
        list_a = list_action()
        lof = list_a.list_of_file()
        count = 0
        for file_name in lof:
            print(str(count) + ' - ' + file_name)
            count = count+1
        question = 'select origin file:'
        resp = input(question)
        return lof[int(resp)]
