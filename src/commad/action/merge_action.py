"""merge."""
import os
import difflib
from src.logger.logger import logger
from src.commad.action.origin_action import origin_action


class merge_action(logger):
    """Merge_action."""

    def __init__(self):
        """Init class."""
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

    def merge_files(self):
        """Merge files."""
        try:
            files = list()
            files.append(self.__select_origin())
            files.append(self.__select_origin())
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