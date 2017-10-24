import hostswitcher.lib

class merge_command(object):

    def __init__(self, args):
        self.path_hosts = hostswitcher.lib.hosts_path()
        self.file_name = 'hosts.default'
        print('run %s command' % __name__)