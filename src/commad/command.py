"""Command."""
from src.logger.logger import logger
from src.commad.action.init_action import init_action
from src.commad.action.create_action import create_action
from src.commad.action.merge_action import merge_action
from src.commad.action.list_action import list_action
from src.commad.action.read_action import read_action
from src.commad.action.edit_action import edit_action
from src.commad.action.set_action import set_action
from src.commad.action.remove_action import remove_action


log = logger()

description = """
Usage: main.py [OPTIONS]

  Host-switcher

Options:
  --init                                                    set current hosts file default hosts file
  --create   [name new file]                                create new hosts file by current hosts file
  --createby [origin-name] [name new file]                  create new hosts file from selected file
  --merge    [origin-name] [origin-name] [name new file]    merge two exist files
  --read     [origin-name]                                  read hosts file
  --edit     [origin-name]                                  edit hosts file
  --set      [origin-name]                                  set hosts file
  --list                                                    list of hosts files
  --remove   [origin-name]                                  remove custom hosts files
  --help                                                    Show this message and exit.

 Dev Options:
  [Option] [param_1...] [param_n] --gui                     write response into the socket
"""


def command(func):
    def getArgs(self, arg):
        try:
            func = getattr(function, arg[1][2:])
            func(arg)
        except Exception as e:
            log.log_warning(e)
            function.help()
    return getArgs

class function:

    def help():
        print(description)

    def init(arg=list):
        gui = False
        last_arg = arg[len(arg)-1]
        if last_arg == "--gui":
            del arg[len(arg)-1]
            gui = True
        init_a = init_action()
        init_r = init_a.copy_current_host_file()
        print_cli.print_dict(init_r, gui)

    def create(arg=list):
        try:
            gui = False
            last_arg = arg[len(arg)-1]
            if last_arg == "--gui":
                del arg[len(arg)-1]
                gui = True
            create_a = create_action()
            create_r = create_a.create_new_file_by_current(None, arg[2])
            print_cli.print_dict(create_r, gui)
        except Exception as e:
            create_a = create_action()
            create_r = create_a.create_new_file_by_current()
            print_cli.print_dict(create_r)

    def createby(arg=list):
        try:
            gui = False
            last_arg = arg[len(arg)-1]
            if last_arg == "--gui":
                del arg[len(arg)-1]
                gui = True
            create_a = create_action()
            create_r = create_a.create_new_file_by_select(arg[2], arg[3])
            print_cli.print_dict(create_r, gui)
        except Exception as e:
            create_a = create_action()
            create_r = create_a.create_new_file_by_select()
            print_cli.print_dict(create_r)

    def merge(arg=list):
        try:
            gui = False
            last_arg = arg[len(arg)-1]
            if last_arg == "--gui":
                del arg[len(arg)-1]
                gui = True
            merge_a = merge_action()
            merge_r = merge_a.merge_files(arg[2], arg[3], arg[4])
            print_cli.print_dict(merge_r, gui)
        except Exception as e:
            merge_a = merge_action()
            merge_r = merge_a.merge_files()
            print_cli.print_dict(merge_r)

    def read(arg=list):
        try:
            gui = False
            last_arg = arg[len(arg)-1]
            if last_arg == "--gui":
                del arg[len(arg)-1]
                gui = True
            read_a = read_action()
            read_r = read_a.read_file(arg[2])
            print_cli.print_dict(read_r, gui)
        except Exception as e:
            print(e)
            read_a = read_action()
            read_r = read_a.read_file()
            print_cli.print_dict(read_r)

    def edit(arg=list):
        try:
            gui = False
            last_arg = arg[len(arg)-1]
            if last_arg == "--gui":
                del arg[len(arg)-1]
                gui = True
            edit_a = edit_action()
            edit_r = edit_a.edit_file(arg[2])
            print_cli.print_dict(edit_r, gui)
        except Exception as e:
            edit_a = edit_action()
            edit_r = edit_a.edit_file()
            print_cli.print_dict(edit_r)

    def set(arg=list):
        try:
            gui = False
            last_arg = arg[len(arg)-1]
            if last_arg == "--gui":
                del arg[len(arg)-1]
                gui = True
            set_a = set_action()
            set_r = set_a.set_file(arg[2])
            print_cli.print_dict(set_r, gui)
        except Exception as e:
            set_a = set_action()
            set_r = set_a.set_file()
            print_cli.print_dict(set_r)

    def list(arg=list):
        try:
            gui = False
            last_arg = arg[len(arg)-1]
            list_a = list_action()
            lof_list = list_a.list_of_file()
            lof = list_a.in_use(lof_list['list'])
            titles = ['File name', 'Create date', 'Update date']
            if last_arg == "--gui":
                del arg[len(arg)-1]
                gui = True
                print(lof)
            else:
                table.print_table(titles, lof)
            print_cli.print_dict(lof_list, gui)
        except Exception as e:
            print(e)

    def remove(arg=list):
        try:
            list_arg = arg[2:]
            gui = False
            last_arg = arg[len(arg)-1]
            if last_arg == "--gui":
                del arg[len(arg)-1]
                gui = True
                list_arg = arg[2:-1]
            for origin in list_arg:
                remove_a = remove_action()
                remove_r = remove_a.remove_file(origin)
                print_cli.print_dict(remove_r, gui)
        except Exception as e:
            while True:
                remove_a = remove_action()
                remove_r = remove_a.remove_file()
                print_cli.print_dict(remove_r)


class print_cli:
    def print_dict(dict_risp, gui=False):
        if gui is True:
            print('socket')
            print(dict_risp)
        else:
            if dict_risp['status'] == 0:
                log.log_info(dict_risp)
                if dict_risp['msg'] is not None:
                    print(' ' + dict_risp['msg'])
            if dict_risp['status'] == -1:
                log.log_error(dict_risp)
                print(' ' + dict_risp['msg'])


class table:
    def print_table(titles=list(), data=list()):
        try:
            col_num = len(titles)
            titles = list(titles)
            table = list()
            table.append(titles)
            for row in data:
                table.append(row)
            col_len = 0
            # get max string
            for row in table:
                for i in range(col_num):
                    if len(row[i]) > col_len:
                        col_len = len(row[i])

            col_len = col_len + 2
            # set len string
            print("-"*(((col_num*col_len)+col_num)-5))
            count_row = 0
            for row in table:
                string_row = "|"
                for i in range(col_num):
                    add_c = col_len - len(row[i])
                    row[i] = row[i] + (" "*add_c)
                    if row[i].find("*") == 0:
                        row[i] = str('\033[1m' + row[i][7:] + ' \033[0;0m')
                    elif i == 0 and count_row != 0:
                        row[i] = str(row[i][6:])
                    if count_row == 0 and i == 0:
                        row[i] = str('\033[1m' + row[i][:-6] + '\033[0;0m')
                    elif count_row == 0 and i != 0:
                        row[i] = str('\033[1m' + row[i] + '\033[0;0m')
                    string_row = string_row + row[i] + "|"
                print(string_row)
                print("-"*(((col_num*col_len)+col_num)-5))
                count_row = count_row + 1
            print("\n")
        except Exception as e:
            print(e)
