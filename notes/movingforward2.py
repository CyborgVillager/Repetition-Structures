#keep_going_m8 = 'y'

def login():
    keep_going_m8 = 'y'
    while keep_going_m8 == 'y' or keep_going_m8 == 'yes':
        username = input('Please enter your username: ')
        password = input('Please enter your password: ')

        if password == 'password':
            print('Login Successful!')
            keep_going_m8 = input('To retry the login please type yes, or y. ' + '\n'
                                  + 'else press any other key to quit program ')
        else:
            print('Incorrect Login please try again!')
            keep_going_m8 = input('To retry login please type yes, or y. ' + '\n'
                                  + 'else press any other key to quit program ')


login()

