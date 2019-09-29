#bug collector collects bugs every day 5 days
#keeps a running total of number of bugs collected during five days

#should ask number of bugs collected for each day, when loop is finioshed total of number
#bugs colelcted

bugs_collected =  0

#how_many = int(input('how many bugs have you collected today?'))

#for loop
for how_many in range(5):
    how_many = int(input('how many bugs have you collected today?'))
    bugs_collected += how_many
    print('You have collected over', bugs_collected, 'bugs for the past five days!')
