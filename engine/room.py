'''Generates room object'''
from seed import genSeed
from random import randint
#setstage
def genRoom(x):
    genSeed(str(x))
    room=[[" "]*16 for i in range(16)]
    for i in range(16):
        room[0][i]="w"
        room[i][0]="w"
        room[i][15]="w"
        room[15][i]="w"
    for i in range(randint(0,1),randint(2,9)):
        room[randint(1,14)][randint(1,14)]="o"
    room[15][8]="E"
    room[0][12]="E"
    for i in range(randint(0,2),randint(2,6)):
        room[randint(1,14)][randint(1,14)]="x"
    for i in range(randint(0,2)):
        room[randint(1,14)][randint(1,14)]="T"
    if randint(0,1000)<=5:
        room[randint(1,14)][randint(1,14)]="S"
        return room
    return room
#getanomalousroom
def getanomalyroom():
    while True:
        x=randint(0,10000000)
        for i in range(16):
            if "S" in genRoom(x)[i]:
                return x

if __name__ == "__main__":
    x=getanomalyroom()
    print(x)
    print(genRoom(x))
