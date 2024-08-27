import pygame
import sys
from button import Botao
from carta import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)
DARK_GREEN = (0, 100, 0)
DARK_RED = (139, 0, 0)
DARK_BLUE = (0, 0, 139)
NEON_GREEN = (57, 255, 20)

pygame.init()

LARGURA_TELA = 800
ALTURA_TELA = 600
TAMANHO_TELA = (LARGURA_TELA, ALTURA_TELA)
COR_FUNDO = (0, 100, 0) 

tela = pygame.display.set_mode(TAMANHO_TELA)
pygame.display.set_caption("Jogo de Cassino")
fonte = pygame.font.Font(None, 36)

playB = Botao(100, 100, 200, 50, "Play", DARK_BLUE)
exitB = Botao(100, 200, 200, 50, "Exit", DARK_BLUE)
giveB = Botao(100, 200, 200, 50, "Give", GREEN)
stopB = Botao(100, 300, 200, 50, "Stop", RED)
backB = Botao(2, 2, 30, 30, "<", WHITE)
playagainB = Botao(100, 250, 150, 70, "Play again", CYAN)

def escrever_texto(texto, fonte, cor, superficie, x, y):
    texto_surface = fonte.render(texto, True, cor)
    texto_rect = texto_surface.get_rect()
    texto_rect.topleft = (x, y)
    superficie.blit(texto_surface, texto_rect)



LARGURA_CARTA = 440 // 5  
ALTURA_CARTA = 372 // 3   

def main():
    jogo_em_execucao = True
    baralho = Carta(LARGURA_CARTA, ALTURA_CARTA)
    cards = refilCards()
    state = 'menu'
    mycards = []
    dlcards = []
    winner = ''

    while jogo_em_execucao:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_em_execucao = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if state == 'menu':
                    if playB.foi_clicado(evento.pos):
                        mycards.clear()
                        dlcards.clear()
                        cards = refilCards()
                        state = 'play'

                        #Dealer gets 2 cards
                        card = pickCard(cards)
                        cards.remove(card)
                        dlcards.append(card)
                        card = pickCard(cards)
                        cards.remove(card)
                        dlcards.append(card)

                        #Player gets 2 cards
                        card = pickCard(cards)
                        cards.remove(card)
                        mycards.append(card)
                        card = pickCard(cards)
                        cards.remove(card)
                        mycards.append(card)

                    elif exitB.foi_clicado(evento.pos):
                        jogo_em_execucao = False
                elif state == 'play':
                    if backB.foi_clicado(evento.pos):
                        state = 'menu'
                    elif stopB.foi_clicado(evento.pos):
                        state = 'lost'
                        values = cardsValue(mycards)
                        valuesD = cardsValue(dlcards)
                        m = max(values)
                        md = max(valuesD)
                    
                        while md < 17:
                            #dealer gets 1 card
                            card = pickCard(cards)
                            cards.remove(card)
                            dlcards.append(card)
                            valuesD = cardsValue(dlcards)
                            if len(valuesD) == 0:
                                md = 0
                                break
                            md = max(valuesD)

                        if m > md:
                            winner = 'Player'
                        elif m < md:
                            winner = 'Dealer'
                        else:
                            winner = ''
                        print(f'{m}-{md}')
                    elif giveB.foi_clicado(evento.pos):

                        #Player gets 1 card
                        card = pickCard(cards)
                        cards.remove(card)
                        mycards.append(card)
                        if len(cardsValue(mycards)) == 0:
                            state = 'lost'
                            winner = 'Dealer'
                        

                elif state == 'lost':
                    if playagainB.foi_clicado(evento.pos):
                        mycards.clear()
                        dlcards.clear()
                        cards = refilCards()
                        state = 'play'

                        #Dealer gets 2 cards
                        card = pickCard(cards)
                        cards.remove(card)
                        dlcards.append(card)
                        card = pickCard(cards)
                        cards.remove(card)
                        dlcards.append(card)

                        #Player gets 2 cards
                        card = pickCard(cards)
                        cards.remove(card)
                        mycards.append(card)
                        card = pickCard(cards)
                        cards.remove(card)
                        mycards.append(card)
                    
                    elif backB.foi_clicado(evento.pos):
                        state = 'menu'
                        
                
        tela.fill(COR_FUNDO)
        if state == 'menu':
            playB.desenhar(tela)
            exitB.desenhar(tela)
        elif state == 'play':
            giveB.desenhar(tela)
            stopB.desenhar(tela)
            backB.desenhar(tela)
            baralho.desenharMao(tela, mycards, 100, 400)
            baralho.desenharMao(tela, dlcards, 100, 50, True)
            escrever_texto(str(max(cardsValue(mycards))), fonte, PINK, tela, 100 + LARGURA_CARTA + len(mycards)*20, 450)
        elif state == 'lost':
            baralho.desenharMao(tela, mycards, 100, 400)
            baralho.desenharMao(tela, dlcards, 100, 50)
            playagainB.desenhar(tela)
            if len(cardsValue(mycards)) == 0: # arrebentou player
                escrever_texto('Arrebentou !', fonte, RED, tela, 100 + LARGURA_CARTA + len(mycards)*20, 450)
            else:
                escrever_texto(str(max(cardsValue(mycards))), fonte, PINK, tela, 100 + LARGURA_CARTA + len(mycards)*20, 450)
            if len(cardsValue(dlcards)) == 0: # arrebentou dealer
                escrever_texto('Arrebentou !', fonte, RED, tela, 100 + LARGURA_CARTA + len(dlcards)*20, 100)
            else:
                escrever_texto(str(max(cardsValue(dlcards))), fonte, PINK, tela, 100 + LARGURA_CARTA + len(dlcards)*20, 100)
            if winner == 'Player':
                escrever_texto('You won !', fonte, GREEN, tela, 400, 270)
            elif winner == 'Dealer':
                escrever_texto('You lost !', fonte, RED, tela, 400, 270)
            else:
                escrever_texto('Tie !', fonte, YELLOW, tela, 400, 270)
            


        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Executar o jogo
if __name__ == "__main__":
    main()
