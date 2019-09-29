ask_user = int(input('Enter amount you would like to exceed or meet?'))
buget_exp = 0

retry = 'y'

while retry == 'y' or retry == 'yes' or retry == 'Yes':
    ask_user_2 = int(input('How much would you like to put in today? '))
    buget_exp += ask_user_2
    retry = input('Would you like to continue? If so type (yes), or (y). Else hit ' \
                  'any other key to exit program')

if buget_exp >= ask_user:
 print('You have put in over $', buget_exp, 'out of your main goal of $', ask_user)
else:
    print('You are under your budget, you only put in $', buget_exp, 'out of your', \
          'designated budget of $', ask_user, ' please try again!')