import pygame as pg # importando a biblioteca do pygame
import random # usado para aleatorizar as palavras
import time # usando em time.sleep
import listadepalavras # lista de palavras p dificuldade (ainda nao emplementado) 

# cores do jogo

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# setup da tela do jogo

window = pg.display.set_mode((1000, 600)) # tamanho da janela
pg.display.set_caption('Jogo da Forca') # nome da janela

# fonte do jogo

pg.font.init()

# fonte e tamanho 

font = pg.font.SysFont("Courier New", 50) # fonte, pixels
font_rb = pg.font.SysFont("Courier New", 30)

# vetor com palavras para o jogo 

words = ['CANETA', 'CARRO', 'CASA', 'COMPUTADOR', 'FILHO', 'JOVEM', 'LIVRO', 'PINCEL', 'MESA', 'MORTE',
          'TERRA', 'AGUA', 'AR', 'FOGO', 'CHAPEU', 'DIA', 'ESPIRITO', 'ESCURO', 'FILHO', 'INIMIGO', 'INFERNO']

# variáveis globais

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
   pg.draw.rect(window, black, (700, 100, 230, 70))
   texto = font_rb.render('RECOMEÇAR', 1, white)
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

def restart(cam_word, end_game, chance, letter, tries, click_last_status, click, x, y):
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
            draftwords(words, choosen_word, end_game) # palavra sorteada novamente
      
   return end_game, chance, tries, letter

# tela de game-over

def gameover(window):
   if chance == 6:
      time.sleep(0.5)
      pg.draw.rect(window, black, (0, 0, 1000, 600))
      texto = font.render('GAME OVER', 5, red)
      window.blit(texto, (350, 250))

# lista de letras para imprimir na tela 

def draw_tries(tries):
   font = pg.font.Font(None, 36)
   text = font.render('Tentativas de letras: ' + str(tries) + ':', True, white)
   window.blit(text, (20, 20))

   for index, letter in enumerate(tries):
        text = font.render(letter, True, red)
        window.blit(text, (20 + index * 30, 60))

# função para verificar se o ganhador ganhou

def check_win(tries, cam_word):
   for letter in choosen_word:
      if letter in choosen_word:
         if letter not in tries:
            return False
   return True

# tela de vitória

def victory(window):
   victorytext = font.render('VOCÊ GANHOU!', 1, True, green)
   revealing = font.render('A palavra era: ' + choosen_word, 1, True, green) # revelando a palavra
   window.blit(victorytext, (50, 50))
   window.blit(revealing, (50, 100))

# jogo

while True:
   for event in pg.event.get():
      if event.type == pg.QUIT:
         pg.quit()
         quit()
      if event.type == pg.KEYDOWN and event.unicode.isalpha():  # apenas letras do alfabeto
         letter = str(pg.key.name(event.key)).upper()
      if event.type == pg.MOUSEBUTTONDOWN:
         click = pg.mouse.get_pressed()
         click_last_status = True
         

   window.fill(white)

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
   end_game, chance, tries, letter = restart(cam_word, end_game, chance, letter, tries, click_last_status, click, mouse_position_x, mouse_position_y)
   draw_tries(tries)
   
   # vitoria

   if check_win(tries, cam_word):
      victory(window)

   # game-over

   if chance >= 6:
      end_game = True
      gameover(window)

   # click last status

   if click[0] == True:
      click_last_status = True
   else:
      click_last_status = False

   pg.display.update()