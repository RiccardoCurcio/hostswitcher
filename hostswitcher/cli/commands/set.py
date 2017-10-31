"""Set."""
import os
import hostswitcher.lib
from hostswitcher.utils.logger import logger
import hostswitcher.utils.text as t
import hostswitcher.utils.os_executor as os_executor

class set(object):
    """Set class."""

    def __init__(self, args):
        """Init."""
        self.args = args
        self.sys_hosts_path = os_executor.get_hosts_path()
        self.name = self.args['name']
        self.log = logger()

        self.__set_file()
        self.__print_response()

    def __set_file(self, origin=None):

        self.response = dict(
            {
                "status": 0,
                "msg": None,
                "error": None
            }
        )

        try:
            hosts_file = os.path.join(self.args['hosts_path'], self.name)
            if os.path.exists(hosts_file):
                os_executor.change_hosts(hosts_file)
                msg = '%s %s' % (t.bold(self.name), 'set!')
                return self.__set_response(0, msg)
            else:
                error = '%s %s' % (t.bold(self.name), 'not exists!')
                return self.__set_response(-1,  error=error)
        except Exception:
            error = '%s %s' % (t.bold(self.name), 'not set!')
            return self.__set_response(-1,  error=error)

    def __set_response(self, status=0, msg=None, error=None):
        try:
            self.response.update(
                {
                    "status": status,
                    "msg": msg,
                    "error": error
                }
            )
        except Exception as e:
            self.log.error(e)
        return self.response

    def __print_response(self):
        if self.response['status'] != 0:
            print(self.response['error'])
            raise SystemExit(self.response['status'])
        else:
            print(self.response['msg'])
