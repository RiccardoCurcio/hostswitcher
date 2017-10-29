from colorama import init
from termcolor import colored
init()

#from colorama import Fore, Back, Style
#print(colored('Hello, World!', 'green', 'on_red'))

all = ['bold', 'underline']

def bold(text, color=None):
    if color in ['grey','red','green','yellow','blue','magenta','cyan','white']:
        return colored(text, color, attrs=['bold'])
    return colored(text, attrs=['bold'])

def underline(text, color=None):
    if color in ['grey','red','green','yellow','blue','magenta','cyan','white']:
        return colored(text, color, attrs=['bold'])
    return colored(text, attrs=['underline'])