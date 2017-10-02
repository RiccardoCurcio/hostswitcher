"""Command."""
from src.logger.logger import logger
from src.notification.notification import notification
from src.commad.action.init_action import init_action
from src.commad.action.create_action import create_action
from src.commad.action.list_action import list_action


log = logger()
notification = notification()

description = """
Usage: main.py [OPTIONS]

  Host-switcher

Options:
  --init           set current hosts file default hosts file
  --create         create new hosts file by current hosts file
  --createby       create new hosts file by default file
  --edit           edit hosts file
  --set            set hosts file
  --list           list of hosts files
  --help           Show this message and exit.
"""


def command(func):
    def getArgs(self, arg):
        try:
            log.log_info('Command cli start')
            func = getattr(function, arg[1][2:])
            func()
        except Exception as e:
            print('\033[1mOPTION not valid\033[0;0m')
            log.log_warning(e)
            function.help()
    return getArgs


class function:

    def help():
        print(description)

    def init():
        init_a = init_action()
        init_r = init_a.copy_current_host_file()
        if init_r is True:
            notification.send("Init default hosts file")
            print('* Copy current hosts file [ok]')
        else:
            # notification.send("ERROR Init default hosts file")
            print('* Copy current hosts file [N]')

    def create():
        create_a = create_action()
        create_r = create_a.create_new_file_by_current()
        if create_r is True:
            notification.send("Create new hosts file")
            print('* Create new hosts file [ok]')
        else:
            # notification.send("ERROR create new hosts file")
            print('* Create new hosts file [No]')

    def createby():
        notification.send("Create new hosts file by exists hosts file")
        print('createnew')

    def edit():
        notification.send("edit host file")
        print('edit')

    def set():
        notification.send("Set host file")
        print('set')

    def list():
        list_a = list_action()
        lof = list_a.list_of_file()
        lof = list_a.in_use(lof)
        for file_name in lof:
            print(file_name)
