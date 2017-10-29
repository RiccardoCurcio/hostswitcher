import os

from hostswitcher.lib import commands
from hostswitcher.utils import *
from hostswitcher.utils.logger import logger

all = ['hosts_path', 'change_hosts']

def hosts_path():
        if os_resolver() != 'Windows':
            return '/etc/hosts'
        else:
            return 'C:\Windows\System32\drivers\etc\hosts'

def change_hosts(filename):
    try:
        if os_resolver() != 'Windows':
            os.system("cp " + filename + " " + hosts_path())
        else:
            os.system("xcopy \"" + filename + "\"  \"" + hosts_path() + "\" /F /Y" )
    except OSError as e:
        logger().error(e)