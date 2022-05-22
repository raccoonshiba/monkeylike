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

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp()

    def get_atk(self):
        return self.atk

    def get_def(self):
        return self.defense
        