"""Combine."""
import os
from hostswitcher.utils.logger import logger
import hostswitcher.utils.text as t


class combine(object):
    """Combine."""

    def __init__(self, args):
        """Init."""
        self.args = args
        # self.hosts_file_suffix= 'combined'
        # self.name = '%s.%s' % (self.args['name'][0], self.hosts_file_suffix)
        self.name = self.args['name'][0]
        self.origin = self.args['from']
        self.log = logger()

        self.__combine()
        self.__print_response()

    def __combine(self):
        """Private combine."""
        def __remove_duplicate(host_list):
            hosts = list()
            for host in host_list:
                if host not in hosts:
                    hosts.append(host)
            return hosts

        def __write():
            def __overwrite():
                qmsg = '%s %s' % ('exists, do you want overwrite it?',t.underline('(yes/no)'))
                msg = '%s %s' % (t.bold(self.name), qmsg)
                print(msg)
                resp = input()
                if str(resp).lower() == 'yes':
                    try:
                        with open(new_hosts_file, 'w') as f:
                            f.write('#HOSTSWITCHER combined from: %s\n' % ','.join(self.origin))
                            f.writelines(hosts)
                            f.close()
                            msg = '%s %s' % (t.bold(self.name), 'writed!')
                        self.__set_response(status=0, msg=msg)
                    except Exception as e:
                        error = '%s %s' % (t.bold(self.name), 'not writed!')
                        self.__set_response(status=0, error=error)
                elif str(resp).lower() == 'no':
                    error = '%s %s' % (t.bold(self.name), 'not overwrited!')
                    self.__set_response(status=-1, error=error)
                else:
                    print('Invalid choice. Retry')
                    __overwrite()

            if os.path.exists(new_hosts_file):
                __overwrite()
            else:
                try:
                    with open(new_hosts_file, 'w') as f:
                        f.write('#HOSTSWITCHER combined from: %s\n' % ','.join(self.origin))
                        f.writelines(hosts)
                        f.close()
                    msg = '%s %s' % (t.bold(self.name), 'writed!')
                    self.__set_response(status=0, msg=msg)
                except OSError as e:
                    self.log.error(e)

        self.response = {
            "newhosts": self.name,
            "origin": self.origin,
            "missing_origin": list(),
            "status": 0,
            "msg": None,
            "error": None
        }
        hosts = list()
        for file in self.origin:
            hosts.extend(self.__read_host_file(file))
        hosts = __remove_duplicate(hosts)

        new_hosts_file = os.path.join(self.args['hosts_path'], self.name)

        if self.response["status"] == 0:
            __write()

    def __read_host_file(self, hostsfile):
        buffer = list()
        try:
            path = os.path.join(self.args['hosts_path'], hostsfile)
            with open(path, 'r') as f:
                buffer = f.readlines()
                f.close()
        except Exception:
            self.response['missing_origin'].append(hostsfile)
            error = 'Not found %s\nExit'  % (t.bold(','.join(self.response['missing_origin'])))
            self.__set_response(status=-1, error=error)
            return list()

        hostsfile_data = list()

        for line in buffer:
            if not line.startswith('\n'):
                hostsfile_data.append(line)

        return hostsfile_data

    def __set_response(self, newhosts=None, origin=None, status=0, msg=None, error=None):
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
            self.log.error(e)
        return self.response

    def __print_response(self):
        if self.response['status'] != 0:
            print(self.response['error'])
            raise SystemExit(self.response['status'])
        else:
            print(self.response['msg'])
