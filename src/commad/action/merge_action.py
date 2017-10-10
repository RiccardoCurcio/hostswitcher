"""merge."""
import os
import difflib
from src.logger.logger import logger
from src.commad.action.origin_action import origin_action
from src.lib.os_resolver import os_resolver


class merge_action(logger):
    """Merge_action."""

    def __init__(self):
        """Init class."""
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

    def merge_files(self, origin_one=None, origin_two=None, new_name=None):
        """Merge files."""
        try:
            files = list()
            if origin_one is None:
                files.append(self.__select_origin())
            else:
                files.append('hosts.' + origin_one)

            if origin_two is None:
                files.append(self.__select_origin())
            else:
                files.append('hosts.' + origin_two)

            if new_name is None:
                new_name = self.__insert_name()

            new_name = 'hosts.' + new_name
            file_path_new = self.path_hosts_custom + new_name

            new_file_w = open(
                file_path_new,
                'w'
            )
            new_file_w.seek(0)
            for line in self.__merge(files, new_name):
                new_file_w.write(line)
            new_file_w.close()
            self.osr.launch_editon(file_path_new)
            msg = 'Files meged in ' + new_name + '!'
            return self.__set_return(0, msg)
        except Exception as e:
            self.log_warning(e)
            msg = 'no merged!'
            return self.__set_return(-1, msg, e)

    def __select_origin(self):
        origin_a = origin_action()
        return origin_a.select_origin()

    def __merge(self, files=list, file_name=""):
        f = open(self.path_hosts_custom + files[0], 'r')
        f1 = open(self.path_hosts_custom + files[1], 'r')
        str1 = f.read()
        str2 = f1.read()
        str1 = str1.split("\n")
        str2 = str2.split("\n")
        d = difflib.Differ()
        diff = list(d.compare(str2, str1))
        new_file = list()
        new_file.append("#" + file_name.upper())
        new_file.append("#MERGED " + str(files[0]) + ' <-> ' + str(files[1]))
        for line in diff:
            new_file.append(line[2:])
        file_merged = "\n".join(new_file)
        return file_merged

    def __insert_name(self):
        name = input(" Please insert new hosts file name: ")
        return name

    def __set_return(self, status=0, msg=None, error=None):
        self.return_dict.update(
            {
                "status": status,
                "msg": msg,
                "error": error
            }
        )
        return self.return_dict
