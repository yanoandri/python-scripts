from termcolor import colored, cprint
from pyfiglet import figlet_format


def print_ascii_message(msg, color):
    valid_color = ('red', 'green', 'yellow', 'blue',
                   'cyan', 'magenta', 'white')
    if color not in valid_color:
        color = 'magenta'
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)


message = input('Enter Message : ')
color_art = input('Enter color you want :')
print_ascii_message(message, color_art)
