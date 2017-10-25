import os, shutil
import hostswitcher.lib
from hostswitcher.utils.logger import logger
import hostswitcher.utils.text as t

class init_command(object):

    def __init__(self, args):
        self.args = args
        self.log = logger()
        self.sys_hosts_path = hostswitcher.lib.hosts_path()
        self.file_name = 'hosts.default'
        self.response = dict(
            {
                "status": 0,
                "msg": None,
                "error": None
            }
        )
        self.copy_current_host_file()
        self.print_response()

    def copy_current_host_file(self):

        def __overwrite():
            qmsg = '%s %s' % ('exists, do you want overwrite it?',t.underline('(yes/no)'))
            msg = '%s %s' % (t.bold(default), qmsg)
            resp = input(msg)
            if str(resp).lower() == 'yes':
                shutil.copyfile(hosts, name)
                msg = '%s %s' % (t.bold(default), 'overwrited!')
                return self.__set_response(0, msg)
            elif str(resp).lower() == 'no':
                msg = msg = '%s %s' % (t.bold(default), 'not overwrited!')
                return self.__set_response(0, msg)
            else:
                print('Invalid choice. Retry')
                __overwrite()

        try:
            hosts = self.sys_hosts_path
            default = self.file_name
            name = os.path.join(self.args['hosts_path'],default)

            if os.path.exists(name) is True:
                while True:
                    return __overwrite()
            else:
                shutil.copyfile(hosts, name)
                msg = '%s created\nInit completed!' % t.bold(default)
                return self.__set_response(0, msg)
        except Exception as e:
            self.log.warning(e)
            error = '[ERROR] Init not completed!'
            return self.__set_response(-1, error=error)

    def __set_response(self, status=0, msg=None, error=None):
        self.response.update(
            {
                "status": status,
                "msg": msg,
                "error": error
            }
        )
        return self.response

    def print_response(self):
        if self.response['status'] != 0:
            print(self.response['error'])
            raise SystemExit(self.response['status'])
        else:
            print(self.response['msg'])
            