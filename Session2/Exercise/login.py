count = 0
while count<5:
    username = input('user_name: ')
    password = input('pass_word: ')
    if username == 'd4e' and password == 'd4e':
        print('Welcome back c4e')
        break
    else:
        count += 1
        print('Please try again')    
print('Try again later')