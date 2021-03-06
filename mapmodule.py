#from tkinter import E
import pygame
from pygame.locals import *
import engine.room
import random
import engine.loader
from engine.enemy import Enemy
from engine.player import Player
from engine.game import gameGen
from engine.floor import genFloor
seed=""
def getseed():
	global seed
	with open('seed.txt') as f:
		seed = f.read()
getseed()
#---------------setup variables
player = Player()
pygame.init()
game=[]
room=[]
note=0
#---------------variable used to switch between rooms
def init():
	global seed,room, game
	game=genFloor(seed)
	print(game[note])
	room = game[note]
#--------------- screen based stuff (loading, blitting, etc)
init()
size=32+16
fenetre = pygame.display.set_mode((size*16,size*17), RESIZABLE)
terminals, grounds, walls,evil, man, chest,monke, manhead = engine.loader.load(size)

#----------------------liberals
enemPos= []

def blitback(seed,ii=True):# used to load in the assets based on the room 
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
				if ii:
					enemPos.append(((int(x/size),int(y/size)), Enemy(random.randint(0,5),random.randint(0,5), "loser"))) 
					print("this shound not happen more than once")
			if j == "T":
				fenetre.blit(random.choice(terminals), (x,y))
			if j == "S":
				fenetre.blit(random.choice(grounds), (x,y))
			if j == "E":
				fenetre.blit(random.choice(grounds), (x,y))
			x+=size
		y+=size



def makeUI(player):# used to make the UI, need to get player hp in UI
	hp = 15 #player.getHp()
	max_hp = 20 #player.getMaxHp()
	xp = 100
	maxXp = 100
	posx = int(size*1.25)
	posy = int(size*16.5)
	hp_to_draw = (hp/max_hp)*(size*5)
	exp_to_draw = (xp/maxXp)*(size*4)
	fenetre.blit(manhead, (posx-size,posy-int(size/2)+(size/4)))
	pygame.draw.rect(fenetre, (255,0,0), (posx,posy,size*5,5))
	pygame.draw.rect(fenetre, (0,255,0), (posx,posy,hp_to_draw,5))
	pygame.draw.rect(fenetre, (255,0,255), (posx,posy+size/4,exp_to_draw,5))
	#pygame.draw.rect(fenetre, (0,0,0), (posx*10,posy*10))

def attack(x,y):#used to check enemies before attacking
	for i in enemPos:
		if i[0]==(y,x):

			#print(i[1].getHp())
			if i[1].getAffinity() == player.getWeaponAffinity():
				i[1].setHp(i[1].getHp() - player.getAtk()*2)
			else:
				i[1].setHp(i[1].getHp() - player.getAtk())
			#print(i[1].getHp())
			#print("monkenolife")
			if i[1].getHp() <=0:
				enemPos.remove(i)
	blitback(seed,False)
blitback(seed)

	
makeUI('')
# Affiche le personnage au-dessus de l'herbe
fenetre.blit(man, (size, size))
for i in enemPos:
	fenetre.blit(monke, (i[0][0]*size,i[0][1]*size) )
# Actualise la fen??tre
pygame.display.flip()

nPosX = size # Position en X de la personne
nPosY = size # Position en Y de la personne

pygame.key.set_repeat(400, 30)

# var to loop the game
continu = 1

# ================================================
# main loop
rotation=0
while continu:
	for event in pygame.event.get():        
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			# La fen??tre a ??t?? ferm??e ou La touche ESC a ??t?? press??e.
			continu = 0 # Indique de sortir de la boucle.
		
		if event.type == KEYDOWN:  # currently 0 0 - 720 720
			if event.key == K_RIGHT:
				if room[int(nPosY/(size))][int(nPosX/(size)+1)] not in ["w","T","x"]:
					nPosX += size
				rotation=1
			if event.key == K_LEFT: 
				if room[int(nPosY/(size))][int(nPosX/(size))-1] not in ["w","T","x"]:
					nPosX -= size
				rotation=3
			if event.key == K_UP: 
				if  0 < nPosY/size and room[int(nPosY/(size))-1][int(nPosX/(size))] not in ["w","T","x"]:
					nPosY -= size
				rotation=0
			if event.key == K_DOWN: 
				if nPosY/size < 15 and room[int(nPosY/(size)+1)][int(nPosX/(size))] not in ["w","T","x"] :
					nPosY += size
				rotation=2
			if event.key == K_SPACE: 
				#print("rtation",rotation)
				attack(int(nPosY/(size)),int(nPosX/(size)))
				if rotation==0:
					if 0 < nPosY/size and room[int(nPosY/(size))-1][int(nPosX/(size))] not in ["w","T","x"]:
						attack(int(nPosY/(size))-1,int(nPosX/(size)))
				if rotation==2:
					if nPosY/size < 15 and room[int(nPosY/(size)+1)][int(nPosX/(size))] not in ["w","T","x"] :
						attack(int(nPosY/(size))+1,int(nPosX/(size)))
				if rotation==1:
					if room[int(nPosY/(size))][int(nPosX/(size)+1)] not in ["w","T","x"]:
						attack(int(nPosY/(size)),int(nPosX/(size)+1))
				if rotation==3:
					print(room[int(nPosY/(size))][int(nPosX/(size))-1])
					if room[int(nPosY/(size))][int(nPosX/(size))-1] not in ["w","T","x"]:
						attack(int(nPosY/(size)),int(nPosX/(size)-1))
			if nPosY/size < 1 or nPosY/size > 14:
				print(nPosX,nPosY)
				enemPos=[]
				if nPosY/size <1:
					nPosX=384
					nPosY=720
					note+=1
				else:
					nPosX=576
					nPosY=0
					note -=1
				print("moving to level", note )
				room=game[note]
				blitback(seed)
			#print(nPosX/(size), nPosY/(size))
			blitback(seed,False)
			makeUI('')
			fenetre.blit(man, (nPosX, nPosY))
			for i in enemPos:
				
				fenetre.blit(monke, (i[0][0]*size,i[0][1]*size) )

            # Actualise la fen??tre
			pygame.display.flip()

