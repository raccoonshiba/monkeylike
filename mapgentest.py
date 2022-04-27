import pygame
from pygame.locals import *
import engine.room
import random
pygame.init()
seed=""
room=[]
def init(s="steve"):
	global seed,room
	seed=s
	room = engine.room.genRoom(seed)
init()
size=32+16
# Permet de rendre la fenêtre de taille ajustable.
fenetre = pygame.display.set_mode((size*16,size*17), RESIZABLE)

# Une image pour le fond de la fenêtre
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
man = pygame.image.load("./assets/monkeygifs/mangif.gif").convert()
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
chest = pygame.image.load("./assets/chest.png").convert()
chest = pygame.transform.scale(chest, (size, size))

terminals = [terminal, terminal1, terminal2, terminal3, terminal4]
grounds=[ground1,ground2,ground3]
walls=[wall1,wall2,wall3,wall4]
# pls ignore this 
man.set_colorkey((255,255,255)) 
# Affiche l'image dans la fenêtre
def blitback(seed):
	y=0
	random.seed(seed)
	for i in room:
		x=0
		for j in i:
			
			if j == " ":
				fenetre.blit(random.choice(grounds), (x,y))
			if j == "w":
				fenetre.blit(random.choice(walls), (x,y))
			if j == "x":
				fenetre.blit(random.choice(grounds), (x,y))
			if j == "o":
				fenetre.blit(chest, (x,y))
			if j == "T":
				fenetre.blit(random.choice(terminals), (x,y))
			if j == "S":
				fenetre.blit(random.choice(grounds), (x,y))
			if j == "E":
				fenetre.blit(random.choice(grounds), (x,y))
			x+=size
		y+=size
blitback(seed)
# Affiche le personnage au-dessus de l'herbe
fenetre.blit(man, (size, size))

# Actualise la fenêtre
pygame.display.flip()

nPosX = size # Position en X de la personne
nPosY = size # Position en Y de la personne

pygame.key.set_repeat(400, 30)

# Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

# ================================================
# Boucle principale
while continuer:
	for event in pygame.event.get():        
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			# La fenêtre a été fermée ou La touche ESC a été pressée.
			continuer = 0 # Indique de sortir de la boucle.

		if event.type == KEYDOWN:  # currently 0 0 - 720 720
			if event.key == K_RIGHT:
				if room[int(nPosY/(size))][int(nPosX/(size)+1)] not in ["w","T","o"]:
					nPosX += size
			if event.key == K_LEFT: 
				if room[int(nPosY/(size))][int(nPosX/(size))-1] not in ["w","T","o"]:
					nPosX -= size
			if event.key == K_UP: 
				if room[int(nPosY/(size))-1][int(nPosX/(size))] not in ["w","T","o"]:
					nPosY -= size
			if event.key == K_DOWN: 
				if room[int(nPosY/(size)+1)][int(nPosX/(size))] not in ["w","T","o"]:
					nPosY += size
			print(nPosY/size)
			if nPosY/size < 1 or nPosY/size > 14:
				init(random.randint(0,10000))
			print(nPosX/(32+16), nPosY/(32+16))
			blitback(seed)
			fenetre.blit(man, (nPosX, nPosY))

            # Actualise la fenêtre
			pygame.display.flip()
