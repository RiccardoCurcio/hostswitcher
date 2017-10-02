import os
from src.commad.action.init_action import init_action

text = """
╦ ╦╔═╗╔═╗╔╦╗  ╔═╗╦ ╦╦╔╦╗╔═╗╦ ╦╔═╗╦═╗
╠═╣║ ║╚═╗ ║───╚═╗║║║║ ║ ║  ╠═╣║╣ ╠╦╝
╩ ╩╚═╝╚═╝ ╩   ╚═╝╚╩╝╩ ╩ ╚═╝╩ ╩╚═╝╩╚═

"""


class bootstrap():
    def __init__(self):
        self.path_pwd = os.path.dirname(os.path.abspath(__file__))
        self.path_hosts_custom = self.path_pwd + '/../../hosts_files/'

        pass

    def start_app(self):
        self.__crete_hosts_file_dir()
        print(text)
        pass

    def __crete_hosts_file_dir(self):
        directory = self.path_hosts_custom
        if not os.path.exists(directory):
            os.makedirs(directory)
            init_a = init_action()
            init_a.copy_current_host_file()
