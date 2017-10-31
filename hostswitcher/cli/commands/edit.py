"""Edit."""
import os
from hostswitcher.utils.logger import logger
from hostswitcher.utils.os_executor import launch_editor
import hostswitcher.utils.text as t


class edit(object):
    """Edit class."""

    def __init__(self, args):
        """Init."""
        self.args = args
        self.name = self.args['name']
        self.log = logger()

        self.__edit_hosts_file()
        self.__print_response()

    def __edit_hosts_file(self):
        self.response = dict(
            {
                "hostsfile": self.name,
                "status": 0,
                "msg": None,
                "error": None
            }
        )
        try:
            hosts_file = os.path.join(
                self.args['hosts_path'],
                self.name
            )
            if os.path.exists(hosts_file):
                launch_editor(hosts_file)
                msg = 'Edit complete for %s!' % t.bold(self.name)
                return self.__set_response(0, msg)
            else:
                error = 'Can not edit %s!' % t.bold(self.name)
                return self.__set_response(-1, error=error)
        except Exception as e:
            self.log.warning(e)
            error = '%s %s' % (
                'Can\'t open file',
                t.bold(self.name)
            )
            return self.__set_response(status=-1,  error=error)

    def __set_response(self, status=0, msg=None, error=None):
        """Private set response."""
        try:
            self.response.update(
                {
                    "hostsfile": self.name,
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
