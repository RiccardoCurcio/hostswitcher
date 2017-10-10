"""create."""
import os
import shutil
from src.logger.logger import logger
from src.commad.action.origin_action import origin_action
from src.lib.os_resolver import os_resolver


class create_action(logger):
    def __init__(self):
        logger.__init__(self)
        self.osr = os_resolver()
        self.path_pwd = os.path.dirname(os.path.abspath(__file__))
        self.path_hosts_custom = self.path_pwd + '/../../../hosts_files/'
        self.path_hosts = self.osr.get_hosts_path()
        self.file_name = 'hosts'
        self.return_dict = dict(
            {
                "status": 0,
                "origin": None,
                "newfile": None,
                "msg": None,
                "error": None
            }
        )

    def create_new_file_by_current(self, origin=None, name=None):
        try:
            if name is None:
                name = self.__insert_name()
            name = self.file_name + '.' + name
            copy_result = self.__copy_current_hosts(name, origin)
            if copy_result is False:
                # print(copy_result)
                msg = '\033[1m' + name + '\033[0;0m not created!'
                return self.__set_return(-1, msg)
            file_path = self.path_hosts_custom + name
            self.osr.launch_editon(file_path)
            msg = '\033[1m' + name + '\033[0;0m created!'
            if origin is not None:
                origin = origin[6:]
            return self.__set_return(0, msg, None, origin, name[6:])
        except Exception as e:
            self.log_warning(e)
            msg = '\033[1m' + name + '\033[0;0m not created!'
            return self.__set_return(-1, msg, e)

    def create_new_file_by_select(self, origin=None, name=None):
        if origin is None:
            file_selected = self.__select_origin()
        else:
            file_selected = 'hosts.' + origin
        result = self.create_new_file_by_current(file_selected, name)
        return result

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
                    self.__set_title(new_name, name)
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
        except Exception as e:
            self.log_warning(e)
            return False

    def __insert_name(self):
        name = input(" Please insert new hosts file name: ")
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

    def __select_origin(self):
        origin_a = origin_action()
        return origin_a.select_origin()

    def __set_return(self, status=0, msg=None, error=None, ori=None, new=None):
        try:
            self.return_dict.update(
                {
                    "status": status,
                    "origin": ori,
                    "newfile": new,
                    "msg": msg,
                    "error": error
                }
            )
        except Exception as e:
            print(e)
        return self.return_dict
