"""osresover."""
import platform
import os

class os_resolver:
    """crudlogger."""
    def __init__(self):
        pass

    def get_os(self):
        return platform.system()

    def get_hosts_path(self):
        if self.get_os() != 'Windows':
            return '/etc/hosts'
        else:
            return 'C:\Windows\System32\drivers\etc\hosts'
    
    def launch_editon(self, path=None):
        if self.get_os() != 'Windows':
            os.system("vim " + path)
        else:
            os.system("notepad " + path)
    
    def change_hosts(self, file_path=None):
        if self.get_os() != 'Windows':
            os.system("sudo cp " + file_path + " " + self.get_hosts_path())
        else:
            os.system("xcopy \"" + file_path + "\"  \"" + self.get_hosts_path() + "\" /F /Y" )
