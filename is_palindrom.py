number = input('Put number : ')
number = int(number)
temp = number
result = 0
while temp != 0:
    modulo = temp % 10
    result = (result * 10) + modulo
    temp = temp // 10

if result == number:
    print('Yes it\'s palindrom')
else:
    print('No it isn\'t')