'''Generates game object'''
from engine.player import Player
import pygame
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
            screen.fill(pygame.Color("black"))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.move('l', screen)
                        print('l')

                    if event.key == pygame.K_RIGHT:
                        player.move('r', screen)

                    if event.key == pygame.K_UP:
                        player.move('u', screen)

                    if event.key == pygame.K_DOWN:
                        player.move('d', screen)



            #player.move('u')           
            pygame.display.update()

