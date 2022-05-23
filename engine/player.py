'''Player / Monster defined as characters'''
import pygame
class Player:
    def __init__(self):
        self.hp = 10
        self.max_hp = 10
        self.atk = 1
        self.defense = 1
        self.xp = 1
        self.level = 1

    def getHp(self):
        return self.hp

    def getMaxHp(self):
        return self.max_hp()

    def getAtk(self):
        return self.atk

    def getDef(self):
        return self.defense
    
    