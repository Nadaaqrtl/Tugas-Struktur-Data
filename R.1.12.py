from random import randrange

def my_choice(data):
    x = randrange(0,len(data))
    return data[x]


print(my_choice([0,1,2,3,4,5,6,7,8,9,10,11,12]))
