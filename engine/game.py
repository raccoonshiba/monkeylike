'''Generates game object'''
from engine.seed import genSeed
from engine.player import Player
import pygame
from random import randint
from engine.floor import genFloor
def gameGen(x):
    game=[]
    for i in range(genSeed(x)):
        game.append(genFloor(randint(0,10000000)))
    return game

class Game:
    def __init__(self):
        self.running = True

    def run(self):
        player = Player()

        pygame.init()
        screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('monkeylike')
        screen.blit(player.getImage(), (player.getPos()[0], player.getPos()[1]))

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.move('l', screen)
                    if event.key == pygame.K_RIGHT:
                        player.move('r', screen)
                    if event.key == pygame.K_UP:
                        player.move('u', screen)
                    if event.key == pygame.K_DOWN:
                        player.move('d', screen)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player.move('n', screen)
                        
            pygame.display.update()

    
