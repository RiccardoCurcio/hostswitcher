import hostswitcher.lib

class edit_command(object):

    def __init__(self, args):
        self.path_hosts = hostswitcher.lib.hosts_path()
        self.file_name = 'default'
        print('run %s command' % __name__)