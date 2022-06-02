'''Player / Monster defined as characters'''
import pygame

class Player:# Player class
    def __init__(self):# hp, atk, defense, affinity
        self.hp = 10
        self.max_hp = 10
        self.atk = 1
        self.defense = 1
        self.xp = 1
        self.level = 1

    def getHp(self):# return hp
        return self.hp

    def getMaxHp(self):# return max hp
        return self.max_hp()

    def getAtk(self):# return atk
        return self.atk

    def getDef(self):# return defense
        return self.defense
    
    