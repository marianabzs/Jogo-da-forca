# from operator import truediv
import pygame as pg
import random 

# cores do jogo

white = (255, 255, 255)
black = (0, 0, 0)

# setup da tela do jogo

window = pg.display.set_mode((1000, 600))

# fonte do jogo

pg.font.init()

# fonte e tamanho 

font = pg.font.SysFont("Courier New", 50) # fonte, pixels
font_rb = pg.font.SysFont("Courier New", 30)

# vetor com palavras

words = ["CANETA"
         "BORRACHA"
         "TINTA" 
         "PINCEL"
         "PAPEL"]

tries = ['', '-']
choosen_word = ''
cam_word  = ''
end_game = True
chance = 0
letter = ' '
click_last_status = False

# funcão de desenho da forca

def hangman_draw(window, chance):
   pg.draw.rect(window, white, (0, 0, 1000, 600))
   pg.draw.line(window, black, (100, 500), (100, 100), 10)
   pg.draw.line(window, black, (50, 500), (150, 500), 10)
   pg.draw.line(window, black, (100, 100), (300, 100), 10)
   pg.draw.line(window, black, (300, 100), (300, 150), 10)
   
   if chance >= 1: # head
      pg.draw.circle(window, black, (300, 200), 50, 10)
   if chance >= 2: # body
      pg.draw.line(window, black, (300, 250), (300, 350), 10)
   if chance >= 3: # right arm
      pg.draw. line(window, black, (300, 260), (225, 350), 10)
   if chance >= 4: # left arm
      pg.draw.line(window, black, (300, 260), (375, 350), 10)
   if chance >= 5: # right leg
      pg.draw.line(window, black, (300, 350), (375, 450), 10)
   if chance >= 6: # left leg
      pg.draw.line(window, black, ( 300, 350), (225, 450), 10) 

# desenho do restart button

def restart_button(window):
   pg.draw.rect(window, black, (700, 100, 200, 65))
   texto = font_rb.render('RESTART', 1, white)
   window.blit(texto, (740, 120))

while True:
   for event in pg.event.get():
      if event.type == pg.QUIT:
         pg.quit()
         quit()
      if event.type == pg.KEYDOWN:
         letter = str(pg.key.name(event.key)).upper()
         print(letter)
         
   # jogo
   
   hangman_draw(window, chance)
   restart_button(window)
   
   pg.display.update()