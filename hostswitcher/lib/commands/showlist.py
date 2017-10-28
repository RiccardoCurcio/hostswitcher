import os, time, filecmp
import hostswitcher.lib
from hostswitcher.lib.table import table
from hostswitcher.utils.logger import logger

class showlist_command(object):

    def __init__(self, args):
        self.args = args
        self.hosts_path = self.args['hosts_path']
        self.log = logger()
        
        
        titles = ['File name', 'Create date', 'Update date']
        table.print_table(titles, self.in_use(self.list_of_file()['list']))
       
    def list_of_file(self):
        
        self.response = {
            "status": 0,
            "msg": None,
            "list": list(),
            "error": None
        }

        try:
            list_of_hostsfile = os.listdir(str(self.hosts_path))
            system_files_to_exclude=['.DS_Store']
            for file in system_files_to_exclude:
                list_of_hostsfile.remove(file)
            return self.__set_response(list_of_hostsfile)
        except Exception as e:
            self.log.warning(e)
            return False

    def in_use(self, list_of_file=list):
        response = list()
        for file in list_of_file:
            abspath_file = os.path.join(self.hosts_path,file)
            file_stat = os.stat(abspath_file)
    
            if filecmp.cmp(abspath_file, hostswitcher.lib.hosts_path(), shallow=True) is True:
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

    def __set_response(self, list_of_hostsfile=list, status=0, msg=None, error=None ):
        self.response.update(
            {

                "list": list_of_hostsfile,
                "status": status,
                "msg": msg,
                "error": error
            }
        )
        return self.response