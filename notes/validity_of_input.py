user_age = int(input('Please enter your age: '))

while user_age < 0 or user_age > 250:
    print('Your age is invalid')
    user_age = int(input('Please retype it:'))
else:
    print('Your age is', user_age)
