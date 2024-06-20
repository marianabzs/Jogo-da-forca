# from operator import truediv
import pygame as pg
import random
import time
import listadepalavras 

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

words = ["CANETA",
         "BORRACHA",
         "TINTA",
         "PINCEL",
         "PAPEL"]

tries = ['', '-']
choosen_word = ''
cam_word  = ''
end_game = True
chance = -1
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

# sorteio de palavras

def draftwords(words, choosen_word, end_game):
   if end_game == True:
      word_n = random.randint(0, len(words) - 1)
      choosen_word = words[word_n]
      end_game = False
      chance = 0
   return choosen_word, end_game

# camuflando a palavra

def camuf_words(choosen_word, cam_word, end_game):
   cam_word = choosen_word 
   for n in range(len(cam_word)):
      if cam_word[n:n + 1] not in tries:
         cam_word = cam_word.replace(cam_word[n], '#') 
   return cam_word

# advinhando a letra

def guessingletter(tries, choosen_word, letter, chance):
   if letter not in tries:
      tries.append(letter)
      if letter not in choosen_word:
         chance += 1
   elif letter in tries:
      pass
   return tries, chance

# desenhando a palavra

def worddraw( window, cam_word):
   word = font.render(cam_word, 1, black)
   window.blit(word, (200, 500))

# funcionamento do botao restart

def botaorestart(cam_word, end_game, chance, letter, tries, click_last_status, click, x, y):
   count = 0
   limit = len(cam_word)
   for n in range(len(cam_word)):
      if cam_word[n] != '#':
         count += 1
   if count == limit and click_last_status == False and click[0] == True:
         print("Ok")
         if x >= 700 and x <= 900 and y >= 100 and y <= 165:
            tries = [' ', '-']
            end_game = True 
            chance = 0
            letter = ' '
      
   return end_game, chance, tries, letter


while True:
   for event in pg.event.get():
      if event.type == pg.QUIT:
         pg.quit()
         quit()
      if event.type == pg.KEYDOWN:
         letter = str(pg.key.name(event.key)).upper()

   # var. de posicao do mouse

   mouse = pg.mouse.get_pos()
   mouse_position_x = mouse[0]
   mouse_position_y = mouse[1]

   # var. do click do mouse

   click = pg.mouse.get_pressed()
         
   # jogo
   
   hangman_draw(window, chance)
   restart_button(window)
   choosen_word, end_game = draftwords(words, choosen_word, end_game)
   cam_word = camuf_words(choosen_word, cam_word, tries)
   tries, chance = guessingletter(tries, choosen_word, letter, chance)
   worddraw(window, cam_word)
   end_game, chance, tries, letter = botaorestart(cam_word, end_game, chance, letter, tries, click_last_status, click, mouse_position_x, mouse_position_y)

   # click last status

   if click[0] == True:
      click_last_status = True
   else:
      click_last_status = False

   pg.display.update()