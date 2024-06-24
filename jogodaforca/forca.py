import pygame as pg # importando a biblioteca do pygame
import random # usado para aleatorizar as palavras
import time # usando em time.sleep
import listadepalavras #lista de palavras p dificuldade (ainda nao implementado) 

# cores do jogo

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# setup da tela do jogo

janela = pg.display.set_mode((1000, 600)) # tamanho da janela
pg.display.set_caption('Jogo da Forca') # nome da janela

# fonte do jogo

pg.font.init()

# fonte e tamanho 

font = pg.font.SysFont("Courier New", 50) # fonte, pixels
font_rb = pg.font.SysFont("Courier New", 30)

# variáveis globais

tentativas = ['', '-']
palavra_escolhida = ''
palavra_camuflada  = ''
end_game = True
chance = -1
letra = ' '
click_last_status = False
palavras = ['CANETA', 'CARRO', 'CASA', 'FILHO', 'JOVEM', 'LIVRO', 'PINCEL', 'MESA', 'MORTE', 'TERRA', 'AGUA', 'AR', 'FOGO', 'DIA']

# função de menu com dificuldades

def tela_dificuldades(janela):
   global end_game, palavras
   while True:
      janela.fill(branco)
      texto = font.render('Escolha uma dificuldade:', 1, True, branco)
      janela.blit(texto, (200, 100))

      # botoes para dificuldade

      facil_btn = pg.draw.rect(janela, preto, (350, 250, 240, 60))
      facil_texto = font.render('FACIL', 1, branco)
      janela.blit(facil_texto, (370, 250))

      medio_btn = pg.draw.rect(janela, preto, (350, 350, 240, 60))
      medio_texto = font.render('MEDIO', 1, branco)
      janela.blit(medio_texto, (370, 350))

      dificil_btn = pg.draw.rect(janela, preto, (350, 450, 240, 60))
      dificil_texto = font.render('DIFICIL', 1, branco)
      janela.blit(dificil_texto, (370, 450))

      for event in pg.event.get():
         if event.type == pg.QUIT:
            pg.quit()
            quit()
         if event.type == pg.MOUSEBUTTONDOWN:
            if facil_btn.collidepoint(event.pos):
               palavras = listadepalavras.palavras_faceis
               end_game = False
               return 'facil'
            elif medio_btn.collidepoint(event.pos):
               palavras = listadepalavras.palavras_medias
               end_game = False
               return 'medio'
            elif dificil_btn.collidepoint(event.pos):
               palavras = listadepalavras.palavras_dificeis
               end_game = False
               return 'dificil'

      pg.display.update()

# funcão de desenho da forca

def desenhodaforca(janela, chance):
   pg.draw.rect(janela, branco, (0, 0, 1000, 600))
   pg.draw.line(janela, preto, (100, 500), (100, 100), 10)
   pg.draw.line(janela, preto, (50, 500), (150, 500), 10)
   pg.draw.line(janela, preto, (100, 100), (300, 100), 10)
   pg.draw.line(janela, preto, (300, 100), (300, 150), 10)
   
   if chance >= 1: # cabeça
      pg.draw.circle(janela, preto, (300, 200), 50, 10)
   if chance >= 2: # corpo
      pg.draw.line(janela, preto, (300, 250), (300, 350), 10)
   if chance >= 3: # braço direito
      pg.draw. line(janela, preto, (300, 260), (225, 350), 10)
   if chance >= 4: # braço esquerdo
      pg.draw.line(janela, preto, (300, 260), (375, 350), 10)
   if chance >= 5: # perna direita
      pg.draw.line(janela, preto, (300, 350), (375, 450), 10)
   if chance >= 6: # perna esquerda
      pg.draw.line(janela, preto, ( 300, 350), (225, 450), 10) 

# desenho do restart button

def botao_de_restart(janela):
   pg.draw.rect(janela, preto, (700, 100, 230, 70))
   texto = font_rb.render('RECOMEÇAR', 1, branco)
   janela.blit(texto, (740, 120))

# sorteio de palavras

def palavra_sorteada(palavras, palavra_escolhida, end_game):
   if end_game == True:
      palavra_n = random.randint(0, len(palavras) - 1)
      palavra_escolhida = palavras[palavra_n]
      end_game = False
      chance = 0
   return palavra_escolhida, end_game

# camuflando a palavra

def camuf_palavras(palavra_escolhida, palavra_camuflada, end_game):
   palavra_camuflada = palavra_escolhida 
   for n in range(len(palavra_camuflada)):
      if palavra_camuflada[n:n + 1] not in tentativas:
         palavra_camuflada = palavra_camuflada.replace(palavra_camuflada[n], '#') 
   return palavra_camuflada

# advinhando a letra

def advinhando_letra(tentativas, palavra_escolhida, letra, chance):
   if letra not in tentativas:
      tentativas.append(letra)
      if letra not in palavra_escolhida:
         chance += 1
   elif letra in tentativas:
      pass
   return tentativas, chance

# desenhando a palavra

def desenhoda_palavra( janela, palavra_camuflada):
   palavra = font.render(palavra_camuflada, 1, preto)
   janela.blit(palavra, (200, 500))

# funcionamento do botao restart

def restart(palavra_camuflada, end_game, chance, letra, tentativas, click_last_status, click, x, y):
   count = 0
   limit = len(palavra_camuflada)
   for n in range(len(palavra_camuflada)):
      if palavra_camuflada[n] != '#':
         count += 1
   if count == limit and click_last_status == False and click[0] == True:
         print("Ok")
         if x >= 700 and x <= 900 and y >= 100 and y <= 165:
            tentativas = [' ', '-']
            end_game = True 
            chance = 0
            letra = ' '
            click_last_status = True
      
   return end_game, chance, tentativas, letra

# tela de game-over

def gameover(janela):
    if chance == 6:
        pg.draw.line(janela, preto, ( 300, 350), (225, 450), 10)       
        time.sleep(0.5)
        pg.draw.rect(janela, preto, (0, 0, 1000, 600))
        texto = font.render('TENTE NOVAMENTE', 5, vermelho)
        revelando = font.render('A palavra era: ' + palavra_escolhida, 2, vermelho) # revelando a palavra
        janela.blit(texto, (50, 50))
        janela.blit(revelando, (60, 100))


# lista de letras para imprimir na tela 

def draw_tentativas(tentativas):
   font = pg.font.Font(None, 36)
   text = font.render('Tentativas de letras: ' + str(tentativas) + ':', True, branco)
   janela.blit(text, (20, 20))

   for index, letra in enumerate(tentativas):
        text = font.render(letra, True, vermelho)
        janela.blit(text, (20 + index * 30, 60))

# função para verificar se o ganhador ganhou

def check_win(tentativas, palavra_camuflada):
   for letra in palavra_escolhida:
      if letra in palavra_escolhida:
         if letra not in tentativas:
            return False
   return True

# tela de vitória

def vitoria(janela):
   textodevitoria = font.render('VOCÊ GANHOU!', 1, True, verde)
   revelando = font.render('A palavra era: ' + palavra_escolhida, 1, True, verde) # revelando a palavra
   janela.blit(textodevitoria, (50, 50))
   janela.blit(revelando, (50, 100))

# jogo

while True:

  # dificuldade_escolhida = tela_dificuldades(janela)
   #while dificuldade_escolhida:
   for event in pg.event.get():
      if event.type == pg.QUIT:
         pg.quit()
         quit()
      if event.type == pg.KEYDOWN and event.unicode.isalpha():  # apenas letras do alfabeto, antes contava carac. especiais
         letra = str(pg.key.name(event.key)).upper()
      if event.type == pg.MOUSEBUTTONDOWN:
         click = pg.mouse.get_pressed()
         click_last_status = True
         if click[0] == True: # botao esquerdo do mouse 
            x, y = pg.mouse.get_pos()
            if x >= 700 and x <= 900 and y >= 100 and y <= 165:
               tentativas = [' ', '-']
               end_game = True 
               chance = 0
               letra = ' '
               click_last_status = True

   # var. de posicao do mouse

   mouse = pg.mouse.get_pos()
   mouse_position_x = mouse[0] # botao esquerdo
   mouse_position_y = mouse[1] # botao direito

   # var. do click do mouse

   click = pg.mouse.get_pressed()
            
   # jogo

   desenhodaforca(janela, chance)
   botao_de_restart(janela)
   palavra_escolhida, end_game = palavra_sorteada(palavras, palavra_escolhida, end_game)
   palavra_camuflada = camuf_palavras(palavra_escolhida, palavra_camuflada, tentativas)
   tentativas, chance = advinhando_letra(tentativas, palavra_escolhida, letra, chance)
   desenhoda_palavra(janela, palavra_camuflada)
   # end_game, chance, tentativas, letra = restart(palavra_camuflada, end_game, chance, letra, tentativas, click_last_status, click, mouse_position_x, mouse_position_y)
   draw_tentativas(tentativas)
      
   # vitoria

   if check_win(tentativas, palavra_camuflada):
      vitoria(janela)

   # game-over

   if chance >= 6:
      end_game = True
      gameover(janela)
      time.sleep(0.8)

   # click last status

   if click[0] == True:
      click_last_status = True
   else:
      click_last_status = False

   pg.display.update()