import random

notablepasswords={"easy":20, "medium":10, "hard":5}

def setStage(password):
    random.seed(password)
    if password in notablepasswords:
        return notablepasswords[password]
    return random.randint(5, 20)
