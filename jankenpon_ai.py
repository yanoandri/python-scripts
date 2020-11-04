from random import randint

computer_picks = randint(0,2)
player_two = None

if computer_picks == 0:
    player_two = 'rock'
elif computer_picks == 1:
    player_two = 'paper'
else:
    player_two = 'scissor'

print('...rock...')
print('...paper...')
print('...scissor...')
player_one = input('(Enter your choice): ') 
print('The computer plays {}'.format(player_two)) 
print('SHOOT!')

if player_one and player_two:
    if player_one == player_two:
        player_one = None
    elif player_one == 'rock':
        if player_two == 'scissor':
            player_one = True
        elif player_two == 'paper':
            player_one = False
    elif player_one == 'paper':
        if player_two == 'scissor':
            player_one = False
        elif player_two == 'rock':
            player_one = True
    elif player_one == 'scissor':
        if player_two == 'paper':
            player_one = True
        elif player_two == 'rock':
            player_one = False
else:
    print('invalid format')

if player_one:
    print('You win!')
elif player_one is None:
    print('it\'s a tied')
else:
    print('The computer win!')