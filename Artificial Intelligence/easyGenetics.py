import random

string=[0,0,0,0]

goal = [1,1,1,1]

def fitness(arr):
    fit = 0
    for i in range(4):
        if i ==1:
            fit+=1

    return fit

def mutate(arr):
    pos = int(random.uniform(0,4))
    arr[pos] = 1
    return arr

for i in range(10):
    new_gen = mutate(string)

    if fitness(new_gen) > fitness(string):
        print("new geration fit")
        print(new_gen)
        string=new_gen
    # else:
    #     print("new geration unfit")
    #     print(new_gen)