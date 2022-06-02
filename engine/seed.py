from random import randint, seed

notablepasswords={"easy":20, "medium":10, "hard":5}
def genSeed(password):# password is the password of the game, used to define the seed, some seeds give specific results (not implemented)
    seed(password)
    if password in notablepasswords:
        return notablepasswords[password]
    return randint(5, 20)