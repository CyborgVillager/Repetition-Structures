password = input("Please enter your password: ")

while password != 'password':
    print('Wrong password input, please retype it!')
    password = input("Please enter your password: ")
else:
    print('Your password is', password)
    print('Welcome!')
