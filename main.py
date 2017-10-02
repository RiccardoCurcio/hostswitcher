#!/usr/bin/env python3
import sys
from src.bootstrap.bootstrap import bootstrap
from src.commad.command import command


class app():
    def __init__(self, app_name):
        pass

    @command
    def run(self, arg):
        return arg


if __name__ == '__main__':
    boot = bootstrap()
    boot.start_app()
    app = app("Host-switcher")
    app.run(sys.argv)
