import argparse, os, sys

class cli(object):
    def __init__(self):
        self.__parse_args()          
    
    def __parse_args(self):
        parent_parser=argparse.ArgumentParser(add_help=False)

        main_parser=argparse.ArgumentParser(usage='%(prog)s command')
        main_parser._optionals.title = None
        main_parser._positionals.title = 'Commands'

        action_subparser = main_parser.add_subparsers(dest='command')

        init_parser = action_subparser.add_parser('init', 
            description = 'Set current hosts file default hosts file', 
            help = 'Set current hosts file default hosts file',
            parents=[parent_parser])
        create_parser = action_subparser.add_parser('create',
            description='Create new hosts file by current hosts file', 
            help='Create new hosts file by current hosts file', 
            parents=[parent_parser])
        createby_parser = action_subparser.add_parser('createby', 
            description='Create new hosts file from selected file', 
            help='Create new hosts file from selected file', 
            parents=[parent_parser])
        merge_parser = action_subparser.add_parser('merge', 
            description='Merge two exist files', 
            help='Merge two exist files', 
            parents=[parent_parser])
        read_parser = action_subparser.add_parser('read', 
            description='Read hosts file', 
            help='Read hosts file', 
            parents=[parent_parser])
        edit_parser = action_subparser.add_parser('edit', 
            description='Edit hosts file', 
            help='Edit hosts file', 
            parents=[parent_parser])
        set_parser = action_subparser.add_parser('set', 
            description='Set hosts file', 
            help='Set hosts file', 
            parents=[parent_parser])
        list_parser = action_subparser.add_parser('list', 
            description='List hosts file', 
            help='List hosts file', 
            parents=[parent_parser])
        remove_parser = action_subparser.add_parser('remove', 
            description='Remove hosts file', 
            help='Remove hosts file', 
            parents=[parent_parser])

        ## Setup options for init
        init_parser._positionals.title=None
        init_parser._optionals.title='Help'

        ## Setup options for create
        create_parser._positionals.title='Args'
        create_parser._optionals.title=None
        create_parser.add_argument('name', nargs=1, default=str(),
                                    action='store', help = 'New hosts file name')

        ## Setup options for createby
        createby_parser._positionals.title='Args'
        createby_parser._optionals.title=None
        createby_parser.add_argument('origin', nargs=1, default=str(),
                                    action='store', help = 'Origin hosts file name')
        createby_parser.add_argument('name', nargs=1, default=str(),
                                    action='store', help = 'New hosts file name')

        ## Setup options for merge
        merge_parser._positionals.title='Args'
        merge_parser._optionals.title=None
        merge_parser.add_argument('1st_origin', nargs=1, default=str(),
                                    action='store', help = 'First origin hosts file name')
        merge_parser.add_argument('2nd_origin', nargs=1, default=str(),
                                    action='store', help = 'Second origin hosts file name')
        merge_parser.add_argument('name', nargs=1, default=str(),
                                    action='store', help = 'New hosts file name')

        ## Setup options for read
        read_parser._positionals.title='Args'
        read_parser._optionals.title=None
        read_parser.add_argument('name', nargs=1, default=str(),
                                    action='store', help = 'Hosts origin name')

        self.__args = vars(main_parser.parse_args())    

        if self.__args['command'] == None:
            main_parser.print_help()    
            raise SystemExit(0) 

    def args(self):
        return self.__args