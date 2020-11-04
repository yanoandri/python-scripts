for i in range(1,21):
    if i == 4 or i == 13:
        print(r'{} is UNLUCKY !'.format(i))
    else:
        if i % 2 > 0:
            print(r'{} is odd'.format(i))
        else:
            print(r'{} is even'.format(i))
