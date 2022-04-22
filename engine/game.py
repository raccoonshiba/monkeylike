'''Generates game object'''
from seed import genSeed
from random import randint
from floor import genFloor
def gameGen(x):
    game=[]
    for i in range(genSeed(x)):
        game.append(genFloor(randint(0,10000000)))
    return game
if __name__ == "__main__":
    print(gameGen(1))