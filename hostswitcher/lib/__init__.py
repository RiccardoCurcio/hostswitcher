import os

from hostswitcher.lib import commands
from hostswitcher.utils import *

all = ['hosts_path', 'change_hosts']

def hosts_path():
        if os_resolver() != 'Windows':
            return '/etc/hosts'
        else:
            return 'C:\Windows\System32\drivers\etc\hosts'

def change_hosts(filename=None):
        if os_resolver() != 'Windows':
            os.system("sudo cp " + os.path.dirname(filename) + " " + hosts_path())
        else:
            os.system("xcopy \"" + os.path.dirname(filename) + "\"  \"" + hosts_path() + "\" /F /Y" )