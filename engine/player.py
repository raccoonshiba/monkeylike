'''Player / Monster defined as characters'''
import pygame
class Player:
    def __init__(self):
        self.hp = 1
        self.atk = 1
        self.defense = 1
        self.posx = 10
        self.posy = 10

    def get_hp(self):
        return self.hp

    def get_atk(self):
        return self.atk

    def get_def(self):
        return self.defense
        