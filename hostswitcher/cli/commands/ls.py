"""Ls."""
import os
import time
import filecmp
import hostswitcher.lib
from hostswitcher.lib.table import table
from hostswitcher.utils.logger import logger


class ls(object):
    """Ls class."""

    def __init__(self, args):
        """Init."""
        self.args = args
        self.hosts_path = self.args['hosts_path']
        self.log = logger()
        titles = [
            'File name',
            'Create date',
            'Update date'
        ]
        table.print_table(titles, self.in_use(self.list_of_file()['list']))

    def list_of_file(self):
        """List of file."""
        self.response = {
            "status": 0,
            "msg": None,
            "list": list(),
            "error": None
        }

        try:
            list_of_hostsfile = os.listdir(str(self.hosts_path))
            system_files_to_exclude = ['.DS_Store']
            for file in system_files_to_exclude:
                if os.path.exists(os.path.join(self.args['hosts_path'], file)):
                    list_of_hostsfile.remove(file)
            if len(list_of_hostsfile) == 0:
                print('Before list hosts file, you must run init command. \
                \nView help for more information')
                raise SystemExit()
            return self.__set_response(list_of_hostsfile)
        except Exception as e:
            self.log.warning(e)
            return False

    def in_use(self, list_of_file=list):
        """In use."""
        response = list()
        for file in list_of_file:
            abspath_file = os.path.join(
                self.hosts_path,
                file
            )
            file_stat = os.stat(abspath_file)
            cmp_file = filecmp.cmp(
                abspath_file,
                hostswitcher.lib.hosts_path(),
                shallow=True
            )
            if cmp_file is True:
                response.append(
                    [
                        str('* %s' % file),
                        time.ctime(file_stat.st_atime),
                        time.ctime(file_stat.st_ctime)
                    ]
                )
            else:
                response.append(
                    [
                        file,
                        time.ctime(file_stat.st_atime),
                        time.ctime(file_stat.st_ctime)
                    ]
                )

        return response

    def __set_response(self, list_hfile=list, status=0, msg=None, error=None):
        """Private Set response."""
        self.response.update(
            {

                "list": list_hfile,
                "status": status,
                "msg": msg,
                "error": error
            }
        )
        return self.response
