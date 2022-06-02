import pygame
import sys
pygame.init()
validChars = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
#----------------------------------- displays a password prompting page
class TextBox(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = pygame.font.Font(None, 50)
    self.image = self.font.render("Enter your password", False, [0, 0, 0])
    self.rect = self.image.get_rect()

  def add_chr(self, char):# adds a character to the text
    global shiftDown
    if char in validChars and not shiftDown:
        self.text += char
    elif char in validChars and shiftDown:
        self.text += shiftChars[validChars.index(char)]
    self.update()

  def update(self):# updates the textbox
    old_rect_pos = self.rect.center
    self.image = self.font.render(self.text, False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.rect.center = old_rect_pos


screen = pygame.display.set_mode([640, 480])
textBox = TextBox()
shiftDown = False
textBox.rect.center = [320, 240]

running = True
while running:# main loop
  screen.fill([255, 255, 255])
  screen.blit(textBox.image, textBox.rect)
  pygame.display.flip()
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
        running = False
    if e.type == pygame.KEYUP:
        if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
            shiftDown = False
    if e.type == pygame.KEYDOWN:
        textBox.add_chr(pygame.key.name(e.key))
        if e.key == pygame.K_SPACE:
            textBox.text += " "
            textBox.update()
        if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
            shiftDown = True
        if e.key == pygame.K_BACKSPACE:
            textBox.text = textBox.text[:-1]
            textBox.update()
        if e.key == pygame.K_RETURN:
            if len(textBox.text) > 0:
                seed=textBox.text
                f = open('seed.txt','r+')
                f.truncate(0)
                f.write(str(seed))
                f.close()
                import mapmodule
pygame.display.quit()
pygame.quit()
sys.exit()
#----------------------------------- displays a password prompting page