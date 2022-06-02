'''Generates game object'''
from engine.seed import genSeed
from engine.player import Player
from random import randint
from engine.floor import genFloor
def gameGen(x):# x is the seed, which is used to generate the floor, and is also used to generate the rooms
    game=[]
    for i in range(genSeed(x)):
        game.append(genFloor(randint(0,10000000)))
    return game
if __name__=="__main__":
    print(gameGen("s"))