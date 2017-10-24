###############################
# Logger
###############################

import logging
import logging.handlers
import os
from hostswitcher.utils.text import *
from hostswitcher.utils.file import *

class logger(logging.Logger):
    
    def __init__(self):
        super(logger, self).__init__(name='hostswitcher')

        self.level=logging.INFO

        try:
            if str(os.getenv('LOG_LEVEL'))==str('DEBUG'):
                self.level=logging.DEBUG
        except Exception as e:
            logging.error(e)

        formatter=logging.Formatter("%(asctime)s %(message)s")

        # handler = logging.StreamHandler()
        handler = logging.handlers.RotatingFileHandler(self.__custom_logs_filename(), 'a', maxBytes=1024)
        handler.setFormatter(formatter)
        self.setLevel(self.level)
        self.addHandler(handler)

    def __custom_logs_filename(self):

        try:
            from win32com.shell import shellcon, shell            
            homedir = shell.SHGetFolderPath(0, shellcon.CSIDL_LOCAL_APPDATA, 0, 0)
        except ImportError:
            homedir = os.path.expanduser("~")

        custom_logs_filename = os.path.abspath(os.path.join(homedir,'.hostswitcher/logs/log'))
        create_file(custom_logs_filename)
        return custom_logs_filename

    def debug(self, message):
        self.log(logging.DEBUG, '%s: %s' % (bold('[DEBUG]'), message))

    def info(self, message):
        self.log(logging.INFO, '%s: %s' % (bold('[INFO]'), message))

    def warning(self, message):
        self.log(logging.WARNING, '%s: %s' % (bold('[WARNING]'), message))

    def error(self, message):
        self.log(logging.ERROR, '%s: %s' % (bold('[ERROR]'), message))

    def critical(self, message):
        self.log(logging.CRITICAL, '%s: %s' % (bold('[CRITICAL]'), message))

    def success(self, message):
        self.log(logging.INFO, '%s: %s' % (bold('[SUCCESS]'), message))