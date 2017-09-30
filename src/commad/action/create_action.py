"""create."""
import os
import shutil
from src.logger.logger import logger


class create_action(logger):
    def __init__(self):
        logger.__init__(self)
        self.path_pwd = os.path.dirname(os.path.abspath(__file__))
        self.path_hosts_custom = self.path_pwd + '/../../../hosts_files/'
        self.path_hosts = '/etc/hosts'
        self.file_name = 'hosts'

    def __copy_current_hosts(self, name):
        hosts = self.path_hosts
        new_name = self.path_hosts_custom + name
        try:
            if os.path.exists(new_name) is True:
                question = name + ' exists, do you want overwrite it? (yes/no)'
                resp = input(question)
                if resp == 'yes':
                    shutil.copyfile(
                        hosts,
                        new_name
                    )
                    return True
                return False
        except Exception as e:
            self.log_warning(e)
            return False
        return True

    def __copy_default_hosts(self):
        return True

    def __insert_name(self):
        name = input("Please insert new hosts file name: ")
        return name

    def create_new_file_by_current(self):
        try:
            name = self.__insert_name()
            name = self.file_name + '.' + name
            copy_result = self.__copy_current_hosts(name)
            if copy_result is False:
                return False
            file_path = self.path_hosts_custom + name
            os.system("vim " + file_path)
            return True
        except Exception as e:
            self.log_warning(e)
            return False
