import pygame
from pygame.locals import *
import engine.room
import random
import engine.loader

#---------------liberals

pygame.init()
seed=""
room=[]
def init(s="steve"):
	global seed,room
	seed=s
	room = engine.room.genRoom(seed)
init()
size=32+16
fenetre = pygame.display.set_mode((size*16,size*17), RESIZABLE)
terminals, grounds, walls,evil, man, chest = engine.loader.load(size)
#----------------------liberals
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
				fenetre.blit(chest, (x,y))
			if j == "o":
				fenetre.blit(evil, (x,y))
			if j == "T":
				fenetre.blit(random.choice(terminals), (x,y))
			if j == "S":
				fenetre.blit(random.choice(grounds), (x,y))
			if j == "E":
				fenetre.blit(random.choice(grounds), (x,y))
			x+=size
		y+=size

def attack(x,y):
	return None
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
rotation=0
while continuer:
	for event in pygame.event.get():        
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			# La fenêtre a été fermée ou La touche ESC a été pressée.
			continuer = 0 # Indique de sortir de la boucle.
		
		if event.type == KEYDOWN:  # currently 0 0 - 720 720
			if event.key == K_RIGHT:
				if room[int(nPosY/(size))][int(nPosX/(size)+1)] not in ["w","T","x"]:
					nPosX += size
				rotation=1
			if event.key == K_LEFT: 
				if room[int(nPosY/(size))][int(nPosX/(size))-1] not in ["w","T","x"]:
					nPosX -= size
				rotation=2
			if event.key == K_UP: 
				if  0 < nPosY/size and room[int(nPosY/(size))-1][int(nPosX/(size))] not in ["w","T","x"]:
					nPosY -= size
				rotation=0
			if event.key == K_DOWN: 
				if nPosY/size < 15 and room[int(nPosY/(size)+1)][int(nPosX/(size))] not in ["w","T","x"] :
					nPosY += size
				rotation=3
			if event.key == K_SPACE: 
				if rotation==0:
					if  0 < nPosY/size and room[int(nPosY/(size))-1][int(nPosX/(size))] not in ["w","T","x"]:
						attack(int(nPosY/(size))-1,int(nPosX/(size)))
				if rotation==2:
					if nPosY/size < 15 and room[int(nPosY/(size)+1)][int(nPosX/(size))] not in ["w","T","x"] :
						attack(int(nPosY/(size))+1,int(nPosX/(size)))
				if rotation==1:
					if room[int(nPosY/(size))][int(nPosX/(size)+1)] not in ["w","T","x"]:
						attack(int(nPosY/(size)),int(nPosX/(size)+1))
				if rotation==3:
					if room[int(nPosY/(size))][int(nPosX/(size))-1] not in ["w","T","x"]:
						attack(int(nPosY/(size)),int(nPosX/(size)-1))
			print(nPosY/size)
			if nPosY/size < 1 or nPosY/size > 14:
				init(random.randint(0,10000))
			print(nPosX/(32+16), nPosY/(32+16))
			blitback(seed)
			fenetre.blit(man, (nPosX, nPosY))

            # Actualise la fenêtre
			pygame.display.flip()
