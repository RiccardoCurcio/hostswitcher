import hostswitcher.lib

class init(object):

    def __init__(self, args):
        self.path_hosts = hostswitcher.lib.hosts_path()
        self.file_name = 'hosts.default'