import hostswitcher.lib
from hostswitcher.utils.logger import logger


class create_command(object):

    def __init__(self, args):
        self.path_hosts = hostswitcher.lib.hosts_path()
        self.file_name = 'hosts.default'