from random import randint, seed

notablepasswords={"easy":20, "medium":10, "hard":5}
def genSeed(password):
    seed(password)
    if password in notablepasswords:
        return notablepasswords[password]
    return randint(5, 20)