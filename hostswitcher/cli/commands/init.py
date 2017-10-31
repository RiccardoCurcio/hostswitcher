"""Init."""
import os
import shutil
import hostswitcher.lib
from hostswitcher.utils.logger import logger
import hostswitcher.utils.text as t
from hostswitcher.utils.os_executor import get_hosts_path


class init(object):
    """Init."""

    def __init__(self, args=None):
        """Init."""
        self.args = args
        self.log = logger()
        self.sys_hosts_path = get_hosts_path()
        self.file_name = 'default'
        self.copy_current_host_file()
        self.__print_response()

    def copy_current_host_file(self):
        """Copy current host file."""
        def __overwrite():
            """Private overwrite."""
            question = '%s %s' % (
                'exists, do you want overwrite it?',
                t.underline('(yes/no)')
            )
            msg = '%s %s' % (t.bold(default), question)
            print(msg)
            choice = input()
            if str(choice).lower() == 'yes':
                shutil.copyfile(sys_hosts, hosts_filename)
                msg = '%s %s' % (t.bold(default), 'overwrited!')
                return self.__set_response(0, msg)
            elif str(choice).lower() == 'no':
                msg = msg = '%s %s' % (t.bold(default), 'not overwrited!')
                return self.__set_response(0, msg)
            else:
                print('Invalid choice. Retry')
                __overwrite()

        self.response = dict(
            {
                "status": 0,
                "msg": None,
                "error": None
            }
        )

        try:
            sys_hosts = self.sys_hosts_path
            default = self.file_name
            hosts_filename = os.path.join(self.args['hosts_path'], default)

            if os.path.exists(hosts_filename) is True:
                while True:
                    return __overwrite()
            else:
                shutil.copyfile(sys_hosts, hosts_filename)
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

    def __print_response(self):
        if self.response['status'] != 0:
            print(self.response['error'])
            raise SystemExit(self.response['status'])
        else:
            print(self.response['msg'])
