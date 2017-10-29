import os
import hostswitcher.lib
from hostswitcher.utils.logger import logger
import hostswitcher.utils.text as t


class show(object):

    def __init__(self, args):
        self.args = args
        self.name = self.args['name']
        self.log = logger()

        self.read_hosts_file()
        self.__print_response()

    def read_hosts_file(self):
        self.response = dict(
            {
                "status": 0,
                "msg": None,
                "error": None
            }
        )

        try:
            with open(os.path.join(self.args['hosts_path'], self.name)) as f:
                print(f.read())
                f.close()
                msg = 'Enjoy hosts!'
                self.__set_response(0,msg)
        except OSError as e:
            error='Can\'t read hosts file %s' % t.bold(self.name)
            self.__set_response(-1, None, error)

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
