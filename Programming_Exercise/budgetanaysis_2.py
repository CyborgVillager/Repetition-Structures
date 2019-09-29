ask_user = int(input('How much would you like to budget for the month? '))
buget_to_meet_or_exceed = 0
retry = 'y'

while  retry == 'y' or  retry =='yes':
    ask_user_2 = int(input('How much would you like put in for this week? '))
    buget_to_meet_or_exceed += float(ask_user_2)
    retry = input('To continue type (y) or (yes), else type other key to exit program ')

print('You currently have $', buget_to_meet_or_exceed)


'''''''''
    buget_to_meet_or_exceed += ask_user_2
    print('You\ve added $', ask_user_2)

    if buget_to_meet_or_exceed > ask_user:
        print('You have met your budget goals of $', ask_user, 'you\ve placed over  $',  buget_to_meet_or_exceed)
    # elif buget_to_meet_or_exceed >= ask_user: print('You have exceeded your budget goals, of $', ask_user,
    # 'you currently have $',  buget_to_meet_or_exceed, \ 'nice job!')
    else:
        print('Unfortuanly you have not met your budget goals', \
                  'you only have $',  buget_to_meet_or_exceed, 'instead of your budget amount of $', ask_user, \
              'please try again!')
'''''''''