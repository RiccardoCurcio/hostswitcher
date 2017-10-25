import os, platform

from . import logger

all = ['os_resolver', 'launch_editor']

def os_resolver():
        return platform.system()

def launch_editor(path=None):
        if os_resolver() != 'Windows':
            os.system("vim " + path)
        else:
            os.system("notepad " + path)