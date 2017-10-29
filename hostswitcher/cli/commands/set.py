import os
import hostswitcher.lib
from hostswitcher.utils.logger import logger
import hostswitcher.utils.text as t


class set(object):

    def __init__(self, args):
        self.args = args
        self.sys_hosts_path = hostswitcher.lib.hosts_path()
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
                hostswitcher.lib.change_hosts(hosts_file)
                msg = '%s %s' % (t.bold(self.name), 'set!')
                return self.__set_response(0, msg)
            else:
                error = '%s %s' % (t.bold(self.name), 'not exists!')
                # self.log.warning(error)
                return self.__set_response(-1,  error=error)
        except Exception as e:
            # self.log.warning(e)
            error = '%s %s' % (t.bold(self.name), 'not set!')
            return self.__set_response(-1,  error=error)

    def __set_response(self, status=0, msg=None, error=None ):
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