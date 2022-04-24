'''Player / Monster defined as characters'''
import pygame
class Player:
    def __init__(self):
        self.hp = 1
        self.ad = 1
        self.posx = 10
        self.posy = 10
        self.image = pygame.image.load('monkey.png')

    def move(self, direction, screen):
        if direction == 'r':
            screen.fill((0,0,0))
            self.posx += 10
            screen.blit(self.getImage(), (self.getPos()[0], self.getPos()[1]))

        elif direction == 'l':
            screen.fill((0,0,0))
            self.posx -= 10
            screen.blit(self.getImage(), (self.getPos()[0], self.getPos()[1]))

        elif direction == 'u':
            screen.fill((0,0,0))
            self.posy -= 10
            screen.blit(self.getImage(), (self.getPos()[0], self.getPos()[1]))

        elif direction == 'd':
            screen.fill((0,0,0))
            self.posy += 10
            screen.blit(self.getImage(), (self.getPos()[0], self.getPos()[1]))

        elif direction == 'n':
            screen.fill((0,0,0))
            screen.blit(self.getImage(), (self.getPos()[0], self.getPos()[1]))

    def getPos(self):
        return (self.posx, self.posy)
    
    def getImage(self):
        return self.image