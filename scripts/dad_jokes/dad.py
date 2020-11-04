from termcolor import colored
from pyfiglet import figlet_format
from random import choice
import requests


def print_ascii_message(msg):
    color = 'magenta'
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)


def get_jokes(jokes):
    url = 'https://icanhazdadjoke.com/search'
    response = requests.get(url, headers={'Accept': 'application/json'},
                            params={'term': jokes})
    data = response.json()
    return data['results']


def show_jokes(jokes, keyword):
    if len(jokes) > 1:
        print(f'I\'ve got {len(jokes)} jokes about {keyword}. Here\'s one: ')
        show = choice(jokes)
        print(show['joke'])
    elif kidding == 1:
        print(f'I\'ve got 1 jokes about {keyword}. Here it is: ')
        print(jokes['joke'])
    else:
        print(f'Sorry, i don\'t have any jokes about {keyword}')


print_ascii_message('Dad Joke 3000')
jokes = input('Let me tell you a joke! Give me a topic: ')
kidding = get_jokes(jokes)
show_jokes(kidding, jokes)
