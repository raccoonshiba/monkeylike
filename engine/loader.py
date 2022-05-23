'''creates variables, loads them into pygame'''
import pygame
def load(size):
    wall1 = pygame.image.load("./assets/walls/wall1.png").convert()
    wall1 = pygame.transform.scale(wall1, (size, size))
    wall2 = pygame.image.load("./assets/walls/wall2.png").convert()
    wall2 = pygame.transform.scale(wall2, (size, size))
    wall3 = pygame.image.load("./assets/walls/wall3.png").convert()
    wall3 = pygame.transform.scale(wall3, (size, size))
    wall4 = pygame.image.load("./assets/walls/wall4.png").convert()
    wall4 = pygame.transform.scale(wall4, (size, size))
    ground1 = pygame.image.load("./assets/ground/ground1.png").convert()
    ground1 = pygame.transform.scale(ground1, (size, size))
    ground2 = pygame.image.load("./assets/ground/ground2.png").convert()
    ground2 = pygame.transform.scale(ground2, (size, size))
    ground3 = pygame.image.load("./assets/ground/ground3.png").convert()
    ground3 = pygame.transform.scale(ground3, (size, size))
    man = pygame.image.load("./assets/monkeygifs/mangif.gif").convert_alpha()
    man = pygame.transform.scale(man, (size, size))
    terminal = pygame.image.load("./assets/terminal/terminal.png").convert()
    terminal = pygame.transform.scale(terminal, (size, size))
    terminal1 = pygame.image.load("./assets/terminal/terminal1.png").convert()
    terminal1 = pygame.transform.scale(terminal1, (size, size))
    terminal2 = pygame.image.load("./assets/terminal/terminal2.png").convert()
    terminal2 = pygame.transform.scale(terminal2, (size, size))
    terminal3 = pygame.image.load("./assets/terminal/terminal3.png").convert()
    terminal3 = pygame.transform.scale(terminal3, (size, size))
    terminal4 = pygame.image.load("./assets/terminal/terminal4.png").convert()
    terminal4 = pygame.transform.scale(terminal4, (size, size))
    evil = pygame.image.load("./assets/ground/evilspawn.png").convert()
    evil = pygame.transform.scale(evil, (size, size))
    chest = pygame.image.load("./assets/chest.png").convert()
    chest = pygame.transform.scale(chest, (size, size))
    man.set_colorkey((255,255,255)) 
    manhead = pygame.image.load("./assets/monkeygifs/manheadgifpng.png").convert()
    manhead = pygame.transform.scale(manhead, (size, size))
    terminals = [terminal, terminal1, terminal2, terminal3, terminal4]
    grounds = [ground1,ground2,ground3]
    walls = [wall1,wall2,wall3,wall4]
    
    return terminals, grounds, walls,evil, man, chest, manhead