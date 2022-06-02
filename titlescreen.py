import pygame 
import sys 
from mapmodule import makegame
def title():
    # initializing the constructor 
    pygame.init() 
    # screen resolution 
    res = (1000,720) 
    screen = pygame.display.set_mode(res) 

    title = pygame.image.load("./assets/gui/title.png").convert()
    title = pygame.transform.scale(title, res)
    # opens up a window 

    
    # white color 
    color = (255,255,255) 
    
    # light shade of the button 
    color_light = (170,170,170) 
    
    # dark shade of the button 
    color_dark = (100,100,100) 
    
    # stores the width of the 
    # screen into a variable 
    width = screen.get_width() 
    
    # stores the height of the 
    # screen into a variable 
    height = screen.get_height() 
    screen.blit(title, (0, 0))
    # defining a font 
    smallfont = pygame.font.SysFont('Corbel',35) 
    # rendering a text written in 
    # this font 
    text = smallfont.render('play' , True , color) 
    while True: 
        mouse = pygame.mouse.get_pos() 
        for ev in pygame.event.get():  
            if ev.type == pygame.QUIT: 
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                    print("y")
                    makegame()
        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
            pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
            
        else: 
            pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
        
        # superimposing the text onto our button 
        screen.blit(text , (width/2+50,height/2)) 
        
        # updates the frames of the game 
        pygame.display.update() 