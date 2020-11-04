print('...rock...')
print('...paper...')
print('...scissor...')
player_one = input('(enter player 1\'s choice): ') 
player_two = input('(enter player 2\'s choice): ') 
print('SHOOT!')
if player_one and player_two:
    if player_one == 'rock':
        if player_two == 'scissor':
            player_one = True
        elif player_two == 'paper':
            player_one = False
        else:
            player_one = None
    elif player_one == 'paper':
        if player_two == 'scissor':
            player_one = False
        elif player_two == 'rock':
            player_one = True
        else:
            player_one = None
    elif player_one == 'scissor':
        if player_two == 'paper':
            player_one = True
        elif player_two == 'rock':
            player_one = False
        else:
            player_one = None
else:
    print('invalid format')

if player_one:
    print('player1 wins')
elif player_one is None:
    print('draw')
else:
    print('player2 wins')
