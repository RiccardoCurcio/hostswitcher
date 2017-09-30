"""Command."""
from src.logger.logger import logger


log = logger()

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
        log.log_info('Command cli start')
        func = getattr(function, arg[1][2:])
        func()

    return getArgs


class function:
    def help():
        print(description)

    def init():
        print('init')

    def create():
        print('create')

    def edit():
        print('edit')

    def set():
        print('set')

    def list():
        print('list')
