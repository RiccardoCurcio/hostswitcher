"""Command."""
from src.logger.logger import logger
from src.notification.notification import notification


log = logger()
notification = notification()

description = """
Usage: main.py [OPTIONS]

  Host-switcher

Options:
  --init           set current host file default host file
  --create         create new host file by current host file
  --edit           edit host file
  --set            set host file
  --list           list of host files
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
        notification.send("Init default hosts file")
        print('init')

    def create():
        notification.send("Create new host file")
        print('create')

    def edit():
        notification.send("edit host file")
        print('edit')

    def set():
        notification.send("Set host file")
        print('set')

    def list():
        print('list')
