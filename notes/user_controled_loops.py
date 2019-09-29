#give user choice on their numbnr
#after that add 1

max = int(input('ENTER A NUMBER: '))
#for max in range(max): #without +1 it will just go to 4 since range deletes the last num
for max in range(max+1): #this however will give the user their orignal input answer that they requested to see
    print(max)