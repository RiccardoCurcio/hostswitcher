import hostswitcher.lib
from hostswitcher.utils.logger import logger


class create_command(object):

    def __init__(self, args):
        self.args = args
        self.log = logger()
        self.file_name = 'hosts'

        self.response = dict(
            {
                "newfile": None,
                "origin": None,
                "status": 0,    
                "msg": None,
                "error": None
            }
        )