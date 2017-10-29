import os
import hostswitcher.lib
from hostswitcher.utils.logger import logger
import hostswitcher.utils.text as t

class remove(object):

    def __init__(self, args):
        self.args = args
        self.name = self.args['name'][0]
        self.log = logger()

        self.__remove_hosts_file()
        self.__print_response()

    def __remove_hosts_file(self):

        def __ask_remove():
            question = '%s %s %s %s'  % ('Do you want remove',t.bold(self.name),'?',t.underline('(yes/no)'))
            print(question)
            choice = input()
            if str(choice).lower() == 'yes':
                try:
                    os.remove(hosts_file)
                    msg = '%s %s' % (t.bold(self.name), 'removed!')
                    return self.__set_response(0, msg)
                except Exception as e:
                    error = '%s %s' % (t.bold(self.name), 'not removed!')
                    return self.__set_response(-1, error=error)
                
            elif str(choice).lower() == 'no':
                error = '%s %s' % (t.bold(self.name), 'not removed!')
                return self.__set_response(-1, error=error)
            else:
                print('Invalid choice. Retry')
                __ask_remove()

        self.response = {
            "status": 0,
            "msg": None,
            "error": None
        }

        hosts_file = os.path.join(self.args['hosts_path'], self.name)
        if os.path.exists(hosts_file):
            try:
                __ask_remove()
            except Exception as e:
                self.log.error(e)
        else:
            error = 'Nothing to remove. File %s not exists' % t.bold(self.name)
            self.__set_response(-1, error=error)

    def __set_response(self, status=0, msg=None, error=None ):
        try:
            self.response.update(
                {
                    "status": status,
                    "msg": msg,
                    "error": error
                }
            )
        except Exception as e:
            self.log.error(e)
        return self.response

    def __print_response(self):
        if self.response['status'] != 0:
            print(self.response['error'])
            raise SystemExit(self.response['status'])
        else:
            print(self.response['msg'])