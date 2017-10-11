#!/usr/bin/env python3
import sys
from src.bootstrap.bootstrap import bootstrap
from src.commad.command import command

class app():
    def __init__(self, app_name):
        # print(sys.platform)
        pass

    @command
    def run(self, arg):
        return arg


if __name__ == '__main__':
    boot = bootstrap()
    boot.start_app(sys.argv[len(sys.argv)-1])
    app = app("Host-switcher")
    app.run(sys.argv)
