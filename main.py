#!/usr/bin/env python3
import sys
from src.logger.logger import logger
from src.bootstrap.bootstrap import bootstrap
from src.commad.command import command


class app(logger):
    def __init__(self, app_name):
        logger.__init__(self)
        self.log_info(app_name)
        self.boot = bootstrap()
        self.boot.start_dep()
        pass

    @command
    def run(self, arg):
        self.log_info('Start Host-switcher')
        return arg


if __name__ == '__main__':
    app = app("Host-switcher")
    app.run(sys.argv)
