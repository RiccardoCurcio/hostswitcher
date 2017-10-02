from src.logger.logger import logger

text = """
╦ ╦╔═╗╔═╗╔╦╗  ╔═╗╦ ╦╦╔╦╗╔═╗╦ ╦╔═╗╦═╗
╠═╣║ ║╚═╗ ║───╚═╗║║║║ ║ ║  ╠═╣║╣ ╠╦╝
╩ ╩╚═╝╚═╝ ╩   ╚═╝╚╩╝╩ ╩ ╚═╝╩ ╩╚═╝╩╚═

"""


class bootstrap(logger):
    def __init__(self):
        logger.__init__(self)
        self.log_info('bootstrap app')
        pass

    def start_app(self):
        self.log_info('start app')
        print(text)
        pass
