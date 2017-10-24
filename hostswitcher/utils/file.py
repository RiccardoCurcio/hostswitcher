import os

all = ['create_path', 'create_file']

def create_path(path):
            try:
                if not os.path.exists(path):
                    os.makedirs(path)
            except OSError as e:
                print(e)

def create_file(filename):

        if not os.path.exists(filename):
            try:
                create_path(os.path.dirname(filename))
            except OSError as e:
                print(e)
        try:
            open(filename,'w').close()
        except OSError as e:
            print(e)