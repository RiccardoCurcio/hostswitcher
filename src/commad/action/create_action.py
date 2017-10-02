"""create."""
import os
import shutil
from src.logger.logger import logger
from src.commad.action.list_action import list_action


class create_action(logger):
    def __init__(self):
        logger.__init__(self)
        self.path_pwd = os.path.dirname(os.path.abspath(__file__))
        self.path_hosts_custom = self.path_pwd + '/../../../hosts_files/'
        self.path_hosts = '/etc/hosts'
        self.file_name = 'hosts'

    def __copy_current_hosts(self, name, origin=None):
        if origin is None:
            hosts = self.path_hosts
        else:
            hosts = self.path_hosts_custom + origin
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
                else:
                    return False
            else:
                shutil.copyfile(
                    hosts,
                    new_name
                )

                self.__set_title(new_name, name)
                return True

            return False
        except Exception as e:
            self.log_warning(e)
            return False
        return True

    def __insert_name(self):
        name = input("Please insert new hosts file name: ")
        return name

    def __set_title(self, file_path, name):
        my_file_r = open(
            file_path,
            'r'
        )
        copy_list = list()
        for line in my_file_r:
            copy_list.append(line)
        my_file_r.close()

        my_file_w = open(
            file_path,
            'w'
        )
        my_file_w.seek(0)
        my_file_w.write('#' + name.upper() + '\n')
        for line in copy_list:
            my_file_w.write(line)

        my_file_w.close()

    def create_new_file_by_current(self, origin=None):
        try:
            name = self.__insert_name()
            name = self.file_name + '.' + name
            copy_result = self.__copy_current_hosts(name, origin)
            if copy_result is False:
                return False
            file_path = self.path_hosts_custom + name
            os.system("vim " + file_path)
            return True
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

    def create_new_file_by_select(self):
        file_selected = self.__select_origin()
        self.create_new_file_by_current(file_selected)
