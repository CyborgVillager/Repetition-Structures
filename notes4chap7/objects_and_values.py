a = 'banna'
b = 'banna'
if a is b:
    print('True')
else:
    print('False')

a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]
if a is b:
    print('True')
else:
    print('False')
#they have same element, but are not idential
#because not same object
#a = [1,2,3,4,5,6] refers to a list of object who value is specific in a sequence of elements
#same can be said for b = [1,2,3,4,5,6] its another list with its own specific sequence of elements
