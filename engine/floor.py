'''Floor class, a collection of rooms'''
from engine.room import genRoom
from engine.seed import genSeed
from random import randint

def genFloor(x):#x is the seed, which is used to generate the floor, and is also used to generate the rooms
    '''Generates floor object'''
    floor=[]
    for i in range(genSeed(x)):
        floor.append(genRoom(randint(0,10000000)))
    return floor
if __name__ == "__main__":
    print(genFloor(1))