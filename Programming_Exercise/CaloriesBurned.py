#burning 4.2 calories per minute
#write prog that use loop to show
#number of calories burned after
#10, 15,20,25,30 minutes

burn= 4.2
burn_Counter = 0
#calories burned
for calor in float(range(30,burn)):
    burn_Counter += burn
    print(str(calor))