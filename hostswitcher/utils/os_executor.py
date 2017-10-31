import os, platform, ctypes, subprocess
from . import logger
import hostswitcher.utils.text as text

def get_os():
    return platform.system()

def get_hosts_path():
    if get_os() != 'Windows':
        return '/etc/hosts'
    else:
        return 'C:\Windows\System32\drivers\etc\hosts'

def launch_editor(path=None):
    if get_os() != 'Windows':
        os.system("vim " + path)
    else:
        os.system("notepad " + path)

def is_admin():
    if get_os() != 'Windows':
        return os.getuid() == 0
    else:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

# def change_hosts(filename=None):
#     if get_os() != 'Windows':
#         os.system("sudo cp " + os.path.dirname(filename) + " " + hosts_path())
#     else:
#         os.system("xcopy \"" + os.path.dirname(filename) + "\"  \"" + hosts_path() + "\" /F /Y" )

def change_hosts(filename):
    try:
        if get_os() != 'Windows':
            if is_admin():
                proc = subprocess.call(['cp', filename,  get_hosts_path()])
            else:
                logger().warning('You don\'t have root privileges.')
                proc = subprocess.call(['sudo', 'cp', filename,  get_hosts_path()])
        elif get_os() == 'Windows':
            if is_admin():
                proc = os.system("xcopy \"" + filename + "\"  \"" + get_hosts_path() + "\" /F /Y" )
            else:
                #powershell -Command "Start-Process cmd -Verb RunAs"
                print(text.bold("Hostswitcher must be run as Administrator!", "red"))

        if proc != 0:
            raise SystemExit('Can\'t access to system hosts file.\nExit')
    except OSError as e:
        logger().error(e)