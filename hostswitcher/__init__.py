from hostswitcher.cli import cli
from hostswitcher.version import version
from hostswitcher.utils.file import *
from hostswitcher.utils import os_resolver

import os

__version__ = version
__title__ = 'hostswitcher'

class Hostswitcher(object):
    
    title = '''
        ╦ ╦╔═╗╔═╗╔╦╗  ╔═╗╦ ╦╦╔╦╗╔═╗╦ ╦╔═╗╦═╗
        ╠═╣║ ║╚═╗ ║───╚═╗║║║║ ║ ║  ╠═╣║╣ ╠╦╝
        ╩ ╩╚═╝╚═╝ ╩   ╚═╝╚╩╝╩ ╩ ╚═╝╩ ╩╚═╝╩╚═
        '''
    
    def __init__(self):
        self.__print_title()
        self.__custom_hosts_path()
        self.__start_cli()

    def __print_title(self):
        print(self.title)
        print('OS: %s' % (os_resolver()), end='\n\n')

    def __start_cli(self):
        self.cli = cli()
        self.args = self.cli.args()
    
    def __custom_hosts_path(self):

        try:
            from win32com.shell import shellcon, shell            
            homedir = shell.SHGetFolderPath(0, shellcon.CSIDL_LOCAL_APPDATA, 0, 0)
        except ImportError:
            homedir = os.path.expanduser("~")

        self.custom_hosts_path = os.path.join(homedir,'.hostswitcher/hosts_files')
        create_path(self.custom_hosts_path)

    def run(self):
        lib = __import__('lib')
        commands = getattr(lib, 'commands')
        class_ = getattr(commands, '%s_%s' % (self.args['command'], 'command'))
        
        cmd = class_(self.args)
        

def main():
    app = Hostswitcher()
    app.run()