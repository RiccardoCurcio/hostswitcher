import os, shutil
import hostswitcher.lib
from hostswitcher.utils.logger import logger
from hostswitcher.utils import launch_editor
import hostswitcher.utils.text as t

class create_command(object):

    def __init__(self, args):
        self.args = args
        self.name = self.args['name'][0]
        self.log = logger()
        self.create_new_file_by_current()
        self.__print_response()

    def create_new_file_by_current(self):
        self.response = dict(
            {
                "newhosts": None,
                "origin": None,
                "status": 0,    
                "msg": None,
                "error": None
            }
        )
        try:
            copy_result = self.__copy_current_hosts()
            hosts_file = os.path.join(self.args['hosts_path'],self.name)
            launch_editor(hosts_file)
        except Exception as e:
            self.log.warning(e)
            msg = '%s %s' % (t.bold(self.name),'not created!')
            return self.__set_return(-1, msg, e)


    def __copy_current_hosts(self):
        def __overwrite():
            qmsg = '%s %s' % ('exists, do you want overwrite it?',t.underline('(yes/no)'))
            msg = '%s %s' % (t.bold(self.name), qmsg)
            resp = input(msg)
            if str(resp).lower() == 'yes':
                shutil.copyfile(current_hosts, new_hosts)
                msg = '%s %s' % (t.bold(self.name), 'overwrited!')
                self.__set_response(new_hosts, current_hosts, msg=msg)
            elif str(resp).lower() == 'no':
                msg = '%s %s' % (t.bold(self.name), 'not overwrited!')
                self.__set_response(new_hosts, current_hosts, msg=msg)
            else:
                print('Invalid choice. Retry')
                __overwrite()
                
        current_hosts = hostswitcher.lib.hosts_path()
        new_hosts = os.path.join(self.args['hosts_path'],self.args['name'][0])
        try:
            if os.path.exists(new_hosts) is True:
                return __overwrite()
                # self.__set_title(new_name, name)
            else:
                shutil.copyfile(
                    current_hosts,
                    new_hosts
                )
                msg = '%s %s' % (t.bold(self.name), 'created!')
                # self.__set_title(new_name, name)
                self.__set_response(new_hosts, current_hosts, msg=msg)
        except Exception as e:
            self.log.warning(e)
            error = '%s %s' % (t.bold(self.name), 'not created!')
            self.__set_response(new_hosts, current_hosts, -1, errror=error)

    def __set_title(self, file_path, name):
        my_file_r = open(
            file_path,
            'r'
        )
        copy_list = list()
        for line in my_file_r:
            copy_list.append(line)
        my_file_r.close()

        my_file_w = open(
            file_path,
            'w'
        )
        my_file_w.seek(0)
        my_file_w.write('#' + name.upper() + '\n')
        for line in copy_list:
            my_file_w.write(line)

        my_file_w.close()

    def __set_response(self, newhosts=None, origin=None, status=0, msg=None, error=None ):
        try:
            self.response.update(
                {
                    "newhosts": newhosts,
                    "origin": origin,
                    "status": status,
                    "msg": msg,
                    "error": error
                }
            )
        except Exception as e:
            print(e)
        return self.response

    def __print_response(self):
        if self.response['status'] != 0:
            print(self.response['error'])
            raise SystemExit(self.response['status'])
        else:
            print(self.response['msg'])