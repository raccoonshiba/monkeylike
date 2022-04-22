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
            self.posx += 10
            screen.fill(pygame.Color("black"))
            screen.blit(self.getImage(), (self.getPos()[0], self.getPos()[1]))

        elif direction == 'l':
            self.posx -= 10
            screen.fill(pygame.Color("black"))
            screen.blit(self.getImage(), (self.getPos()[0], self.getPos()[1]))

        elif direction == 'u':
            self.posy -= 10
            screen.fill(pygame.Color("black"))

            screen.blit(self.getImage(), (self.getPos()[0], self.getPos()[1]))

        elif direction == 'd':
            self.posy += 10
            screen.fill(pygame.Color("black"))
            screen.blit(self.getImage(), (self.getPos()[0], self.getPos()[1]))



    def getPos(self):
        return (self.posx, self.posy)
    
    def getImage(self):
        return self.image