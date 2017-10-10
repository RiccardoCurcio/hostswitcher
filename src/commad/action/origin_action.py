"""origin."""
import os
import filecmp
from src.logger.logger import logger
from src.commad.action.list_action import list_action
from src.lib.os_resolver import os_resolver


class origin_action(logger):
    def __init__(self):
        logger.__init__(self)
        self.osr = os_resolver()
        self.path_pwd = os.path.dirname(os.path.abspath(__file__))
        self.path_hosts_custom = self.path_pwd + '/../../../hosts_files/'
        self.path_hosts = self.osr.get_hosts_path()
        self.file_name = 'hosts.default'

    def select_origin(self):
        list_a = list_action()
        lof = list_a.list_of_file()['list']
        count = 0
        print(' [' + str(count) + '] - to exit')
        for file_name in lof:
            count = count+1
            f1 = self.path_hosts_custom + file_name
            if filecmp.cmp(f1, self.path_hosts, shallow=1) is True:
                file_name = '\033[1m' + file_name + '\033[0;0m'
            print(' [' + str(count) + '] - ' + file_name)
        print('\n')
        while True:
            question = ' Select origin file: '
            resp = input(question)
            if resp.isnumeric() is True:
                if int(resp) in range(1, int(count)+1):
                    return lof[int(resp)-1]
                if int(resp) == 0:
                    exit()
        return False
