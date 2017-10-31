from hostswitcher.cli import cli
from hostswitcher.version import version
from hostswitcher.utils.os_executor import *
from hostswitcher.utils.os_executor import get_os
from hostswitcher.utils.logger import logger
from hostswitcher.utils.file import *

import os

__version__ = version
__title__ = 'hostswitcher'

class Hostswitcher(object):

    title = '''
        ╦ ╦╔═╗╔═╗╔╦╗  ╔═╗╦ ╦╦╔╦╗╔═╗╦ ╦╔═╗╦═╗
        ╠═╣║ ║╚═╗ ║───╚═╗║║║║ ║ ║  ╠═╣║╣ ╠╦╝
        ╩ ╩╚═╝╚═╝ ╩   ╚═╝╚╩╝╩ ╩ ╚═╝╩ ╩╚═╝╩╚═
        '''

    log = logger()

    def __init__(self):
        self.__print_title()
        self.__hosts_path()
        self.__check_default()
        self.__start_cli()

    def __print_title(self):
        print(self.title)
        print('Version: %s' % (__version__))
        print('OS: %s\n\n' % (get_os()))

    def __start_cli(self):
        self.cli = cli()
        self.args = self.cli.args()

    def __hosts_path(self):

        homedir = os.path.expanduser("~")

        if get_os() == 'Windows':
            homedir += "\\AppData\\Roaming"

        self.hosts_path = os.path.join(homedir, '.hostswitcher/hosts_files')
        create_path(self.hosts_path)

    def __check_default(self):
        hosts_filename = os.path.join(self.hosts_path, 'default')
        if os.path.exists(hosts_filename) is False:
            from hostswitcher.cli import commands
            class_ = getattr(commands, 'init')
            class_({"hosts_path": self.hosts_path})

    def run(self):
        from hostswitcher.cli import commands
        class_ = getattr(commands, self.args['command'])
        self.args['hosts_path'] = self.hosts_path
        class_(self.args)

def main():
    app = Hostswitcher()
    app.run()
