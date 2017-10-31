"""Init lib."""
import os
import subprocess
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
            if os.getuid() == 0:
                proc = subprocess.call(['cp', filename,  hosts_path()])
            else:
                logger().warning('You don\'t have root privileges.')
                proc = subprocess.call(['sudo', 'cp', filename,  hosts_path()])
        elif os_resolver() == 'Windows':
            proc = os.system("xcopy \"" + filename + "\"  \"" + hosts_path() + "\" /F /Y" )
        if proc != 0:
            raise SystemExit('Can\'t access to system hosts file.\nExit')
    except OSError as e:
        logger().error(e)
