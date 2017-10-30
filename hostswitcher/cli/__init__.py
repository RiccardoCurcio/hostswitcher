import argparse, os, sys

class cli(object):
    def __init__(self):
        self.__parse_args()

    def __parse_args(self):
        parent_parser=argparse.ArgumentParser(add_help=False)

        main_parser=argparse.ArgumentParser()
        main_parser._optionals.title = None
        main_parser._positionals.title = 'Commands'

        action_subparser = main_parser.add_subparsers(dest='command')

        create_parser = action_subparser.add_parser('create',
            description='Create new hosts file',
            help='Create new hosts file',
            parents=[parent_parser])
        edit_parser = action_subparser.add_parser('edit',
            description='Edit hosts file',
            help='Edit hosts file',
            parents=[parent_parser])
        init_parser = action_subparser.add_parser('init',
            description = 'Set current hosts file default hosts file',
            help = 'Set current hosts file default hosts file',
            parents=[parent_parser])
        ls_parser = action_subparser.add_parser('ls',
            description='List hosts file',
            help='List hosts file',
            parents=[parent_parser])
        combine_parser = action_subparser.add_parser('combine',
            description='Combine two or more existent files',
            help='Combine two or more existent files',
            parents=[parent_parser])
        remove_parser = action_subparser.add_parser('remove',
            description='Remove hosts file',
            help='Remove hosts file',
            parents=[parent_parser])
        set_parser = action_subparser.add_parser('set',
            description='Set hosts file',
            help='Set hosts file',
            parents=[parent_parser])
        show_parser = action_subparser.add_parser('show',
            description='Show hosts file',
            help='Show hosts file',
            parents=[parent_parser])


        ## Setup options for create
        create_parser._positionals.title='Args'
        create_parser._optionals.title=None
        create_parser.add_argument('name', nargs=1,
                                    action='store', help = 'New hosts file name')
        create_parser.add_argument('--from', metavar='ORIGIN', nargs='?', default=None,
                            action='store', help = 'Origin hosts file name')

        ## Setup options for edit
        edit_parser._positionals.title='Args'
        edit_parser._optionals.title=None
        edit_parser.add_argument('name', nargs='?', default='default',
                                    action='store', help = 'Edit selected hosts file. [default: %(default)s]')

        ## Setup options for init
        init_parser._positionals.title=None
        init_parser._optionals.title='Help'

        ## Setup options for combine
        combine_parser._positionals.title='Args'
        combine_parser._optionals.title=None
        combine_parser.add_argument('--from', metavar="NAME", nargs='+',
                                    action='store', help = 'Origin hosts files name', required=True)
        combine_parser.add_argument('name', nargs=1,
                                    action='store', help = 'New hosts file name')

        ## Setup options for remove
        remove_parser._positionals.title='Args'
        remove_parser._optionals.title=None
        remove_parser.add_argument('name', nargs=1,
                                    action='store', help = 'Remove selected hosts file.')

        ## Setup options for set
        set_parser._positionals.title='Args'
        set_parser._optionals.title=None
        set_parser.add_argument('name', nargs='?', default='default',
                                    action='store', help = 'Set selected hosts file. [default: %(default)s]')

        ## Setup options for show
        show_parser._positionals.title='Args'
        show_parser._optionals.title=None
        show_parser.add_argument('name', nargs='?', default='default',
                                    action='store', help = 'Show selected hosts file. [default: %(default)s]')

        ## Setup options for showlist
        ls_parser._positionals.title='Args'
        ls_parser._optionals.title=None

        self.__args = vars(main_parser.parse_args())

        if self.__args['command'] == None:
            main_parser.print_help()
            raise SystemExit(0)

    def args(self):
        return self.__args
