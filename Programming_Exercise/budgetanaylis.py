#write a program ask user to amount they
#want to budget for month
#loop should proimp user to enter each expense for month
#keep running total
#when loop is done dipsplay if user is under of over their budget




ask_user = int(input('How much would you like to budget for the month? '))
ask_month_week = int(input('How many weeks are in your month? '))
week_counter = 0
buget_to_meet_or_exceed = 0

for buget in range(ask_month_week): # ask_month_week - week into int
    week_counter += 1
    ask_user_2 = int(input('How much would you like put in for week? ' + str(week_counter)))

    buget_to_meet_or_exceed += ask_user_2
    print('You\ve added $', ask_user_2)


if buget_to_meet_or_exceed > ask_user:
    print('You have met your budget goals of $', ask_user, 'you\ve placed over  $',  buget_to_meet_or_exceed)
#elif buget_to_meet_or_exceed >= ask_user:
#    print('You have exceeded your budget goals, of $', ask_user, 'you currently have $',  buget_to_meet_or_exceed, \
  #        'nice job!')
else:
    print('Unfortuanly you have not met your budget goals', \
              'you only have $',  buget_to_meet_or_exceed, 'instead of your budget amount of $', ask_user, \
          'please try again!')