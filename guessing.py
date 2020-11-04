from random import randint

number = randint(1,10)
while True:
    guess = int(input('Guess a number between 1 to 10: '))
    if guess < number:
        print('Too low, try again!')
    elif guess > number:
        print('Too high, try again!')
    else:
        print('You guessed it! You won!')
        temp = input('Do you want to keep playing? (y/n)')
        if temp == 'n':
            print('Thanks for playing. Bye!')
            break
        else:
            number = randint(1, 10)