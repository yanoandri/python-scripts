import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice


BASE_URL = "http://quotes.toscrape.com"

def scrape_quotes():
    print("################## LOADING ##################")
    all_quotes = []
    url = "/page/1"
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        # print(f"Get page in {BASE_URL}{url}......")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            temp = {
                "text" : quote.find(class_="text").get_text(),
                "author" : quote.find(class_="author").get_text(),
                "link" : quote.find("a")["href"],
            }
            all_quotes.append(temp)
            next_button = soup.find(class_="next")
            url = next_button.find("a")["href"] if next_button else None
        sleep(2)
    return all_quotes

def start_game(quotes):
    print("################## LET'S START THE GAME ##################")
    quote = choice(quotes)
    print(quote['text'])
    print(quote['author'])
    remaining_guess = 4
    guess = ""
    while guess.lower() != quote['author'].lower() and remaining_guess >= 0:
        guess = input(f'Who said this quote? Guess remaining : {remaining_guess}\n')
        if guess.lower() == quote['author'].lower():
            print("################## CONGRATULATIONS YOU'RE GUESSES ARE TRUE ##################")
            break
        if remaining_guess == 3:
            res = requests.get(f"{BASE_URL}{quote['link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_='author-born-date').get_text()
            birth_place = soup.find(class_='author-born-location').get_text()
            print(f"A hint : The author was born on {birth_date} in {birth_place}")
        elif remaining_guess == 2:
            print(f"A hint : The initial first name of the author is {quote['author'][0]}")
        elif remaining_guess == 1:
            print(f"A hint : The initial last name of the author is {quote['author'].split(' ')[1][0]}")
        elif remaining_guess == 0:
            print(f"Times up you running out of guess, the answer is {quote['author']}")
        remaining_guess -= 1
    again = input("Do you want to play again? \n")
    if again in ('y', 'yes'):
        start_game(quotes)
    else:
        print("################## GOODBYE THANK YOU FOR PLAYING ##################")

quotes = scrape_quotes()
start_game(quotes)
# print(len(quotes))