'''Floor class, a collection of rooms'''
from room import genRoom
from seed import genSeed
from random import randint

def genFloor(x):
    '''Generates floor object'''
    floor=[]
    for i in range(genSeed(x)):
        floor.append(genRoom(randint(0,10000000)))
    return floor
if __name__ == "__main__":
    print(genFloor(1))