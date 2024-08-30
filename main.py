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
DARK_RED = (139, 0, 0)
NEON_GREEN = (57, 255, 20)

pygame.init()

LARGURA_TELA = 800
ALTURA_TELA = 600
TAMANHO_TELA = (LARGURA_TELA, ALTURA_TELA)
COR_FUNDO = (0, 100, 0) 

tela = pygame.display.set_mode(TAMANHO_TELA)
imagem_fundo = pygame.image.load('casino.jpeg')
imagem_fundo = pygame.transform.scale(imagem_fundo, TAMANHO_TELA)
mesa_fundo = pygame.image.load('table.jpg')
mesa_fundo = pygame.transform.scale(mesa_fundo, TAMANHO_TELA)
hand = pygame.image.load('meh.png')
thinger = pygame.image.load('dedo.png')
money = pygame.image.load('money.png')
pygame.display.set_caption("Jogo de Cassino")
fonte = pygame.font.Font(None, 36)

coinsImage = []
coinsButtons = []
coinsValues = ['1', '2', '5', '10', '20','50', '100', '250', '500', '1000','5000']
ix = 20
for i in coinsValues:
    img = pygame.image.load(f'coins/{i}.png')
    coinsImage.append(pygame.transform.scale(img, (65,65)))
    coinsButtons.append(Botao(ix, 250, 65, 65, " ", BLACK, WHITE, None, 100,GRAY))
    ix += 65


playB = Botao(LARGURA_TELA // 2 - 50, 150, 100, 50, "Play", WHITE, DARK_GREEN, None, 10, GREEN)
exitB = Botao(LARGURA_TELA // 2 - 50, 250, 100, 50, "Exit", WHITE, DARK_RED, None, 10, RED)
giveB = Botao(100, 200, 200, 50, "Give", DARK_BLUE, WHITE, None, 20, BLUE)
stopB = Botao(100, 300, 200, 50, "Stop", PURPLE, WHITE, None, 20,PINK)
backB = Botao(2, 2, 30, 30, "<", BLACK, WHITE, None, 20,RED)
betB = Botao(LARGURA_TELA // 2 - 100, 400, 200, 50, "Bet", RED, WHITE, None, 20,ORANGE)
playagainB = Botao(100, 250, 150, 70, "Play again", BLACK, NEON_GREEN, None, 5, GRAY)

def escrever_texto(texto, fonte, cor, superficie, x, y):
    texto_surface = fonte.render(texto, True, cor)
    texto_rect = texto_surface.get_rect()
    texto_rect.topleft = (x, y)
    superficie.blit(texto_surface, texto_rect)

def draw_money(tela, cash, money):
    fonte = pygame.font.Font(None, 70)
    texto_cash = fonte.render(f"{cash}", True, GREEN)
    largura_tela = tela.get_width()
    x_img = largura_tela - money.get_width() - texto_cash.get_width() - 20 
    y_img = 10  
    x_texto = x_img + money.get_width() + 10  
    y_texto = y_img + (money.get_height() // 2 - texto_cash.get_height() // 2) 
    tela.blit(money, (x_img, y_img))
    tela.blit(texto_cash, (x_texto, y_texto))

def draw_coins(tela, coinsImg, coinsB, betValues):
    ix = 20
    y = 250
    for i in range(len(coinsImg)):
        coinsB[i].desenhar(tela)
        opaca = coinsImg[i].convert_alpha()
        opaca.set_alpha(85)
        tela.blit(opaca, (ix, y))
        iy = y
        for _ in range(betValues[i]):
            iy -= 20
            tela.blit(coinsImg[i], (ix, iy))
        ix += 65

LARGURA_CARTA = 440 // 5  
ALTURA_CARTA = 372 // 3   
Xinitial = 100
numberAnim = 100

def main():
    jogo_em_execucao = True
    baralho = Carta(LARGURA_CARTA, ALTURA_CARTA)
    cards = refilCards()
    state = 'menu'
    mycards = []
    dlcards = []
    winner = ''
    cash = 100
    betValue = 0
    betCoinsV = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    i = 0

    while jogo_em_execucao:
        i += 1
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_em_execucao = False

            elif evento.type == pygame.MOUSEMOTION:
                pos = evento.pos
                if state == 'menu':
                    playB.ativar(pos)
                    exitB.ativar(pos)
                elif state == 'playBlackjack':
                    giveB.ativar(pos)
                    stopB.ativar(pos)
                    backB.ativar(pos)
                elif state == 'endBlackjack':
                    playagainB.ativar(pos)
                    backB.ativar(pos)
                elif state == 'betBlackjack':
                    backB.ativar(pos)
                    betB.ativar(pos)
                    [x.ativar(pos) for x in coinsButtons]

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if state == 'menu':
                    if playB.foi_clicado(evento.pos):
                        betValue = 0
                        betCoinsV = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                        mycards.clear()
                        dlcards.clear()
                        cards = refilCards()
                        state = 'betBlackjack'

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
                elif state == 'playBlackjack':
                    if backB.foi_clicado(evento.pos):
                        state = 'menu'
                    elif stopB.foi_clicado(evento.pos):
                        values = cardsValue(mycards)
                        valuesD = cardsValue(dlcards)
                        m = max(values)
                        md = max(valuesD)
                        if md < 17: # Dealer needs to receive cards until 17 points
                            i = 0
                            state = 'DanimBlackjack'
                            card = pickCard(cards)
                            cards.remove(card)
                            dlcards.append(card)
                        else:
                            state = 'endBlackjack'
                            if m > md:
                                winner = 'Player'
                                cash += betValue * 2
                            elif m < md:
                                winner = 'Dealer'
                            else:
                                winner = '' 
                                cash += betValue   

                    elif giveB.foi_clicado(evento.pos):

                        #Player gets 1 card
                        card = pickCard(cards)
                        cards.remove(card)
                        mycards.append(card)
                        i = 0
                        state = 'PanimBlackjack'
                        

                elif state == 'endBlackjack':
                    if playagainB.foi_clicado(evento.pos):
                        betValue = 0
                        betCoinsV = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                        mycards.clear()
                        dlcards.clear()
                        cards = refilCards()
                        state = 'betBlackjack'

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

                elif state == 'betBlackjack':
                    if betB.foi_clicado(evento.pos):
                        cash -= betValue
                        state = 'playBlackjack'
                    elif backB.foi_clicado(evento.pos):
                        state = 'menu'
                    for i in range(len(coinsButtons)):
                        if coinsButtons[i].foi_clicado(evento.pos) and betValue + int(coinsValues[i]) <= cash:
                            betCoinsV[i] += 1
                            betValue += int(coinsValues[i])
                
        tela.blit(mesa_fundo, (0,0))
        
        if state == 'menu':
            tela.blit(imagem_fundo, (0, 0))
            playB.desenhar(tela)
            exitB.desenhar(tela)
            draw_money(tela, cash, money)

        elif state == 'betBlackjack':
            draw_money(tela, cash, money)
            backB.desenhar(tela)
            draw_coins(tela, coinsImage, coinsButtons, betCoinsV)
            betB.desenhar(tela)
            escrever_texto(f'Total Bet : {str(betValue)}', pygame.font.Font(None, 50), NEON_GREEN, tela, 300, 10)

        elif state == 'playBlackjack':
            draw_money(tela, cash, money)
            giveB.desenhar(tela)
            stopB.desenhar(tela)
            backB.desenhar(tela)
            baralho.desenharMao(tela, mycards, Xinitial, 400)
            baralho.desenharMao(tela, dlcards, Xinitial, 50, True)
            escrever_texto(str(max(cardsValue(mycards))), fonte, PINK, tela, Xinitial + LARGURA_CARTA + len(mycards)*20, 450)

        elif state == 'endBlackjack':
            backB.desenhar(tela)
            baralho.desenharMao(tela, mycards, Xinitial, 400)
            baralho.desenharMao(tela, dlcards, Xinitial, 50)
            playagainB.desenhar(tela)
            if len(cardsValue(mycards)) == 0: # arrebentou player
                escrever_texto('Bummm !', fonte, RED, tela, Xinitial + LARGURA_CARTA + len(mycards)*20, 450)
            else:
                escrever_texto(str(max(cardsValue(mycards))), fonte, PINK, tela, Xinitial + LARGURA_CARTA + len(mycards)*20, 450)
            if len(cardsValue(dlcards)) == 0: # arrebentou dealer
                escrever_texto('Bummm !', fonte, RED, tela, Xinitial + LARGURA_CARTA + len(dlcards)*20, 100)
            else:
                escrever_texto(str(max(cardsValue(dlcards))), fonte, PINK, tela, Xinitial + LARGURA_CARTA + len(dlcards)*20, 100)
            if winner == 'Player':
                escrever_texto('You won !', fonte, GREEN, tela, 400, 270)
            elif winner == 'Dealer':
                escrever_texto('You lost !', fonte, RED, tela, 400, 270)
            else:
                escrever_texto('Tie !', fonte, YELLOW, tela, 400, 270)

        elif state == 'PanimBlackjack':
            baralho.desenharMao(tela, mycards[:-1], Xinitial, 400)
            baralho.desenharMao(tela, dlcards, Xinitial, 50, True)
            tela.blit(hand, ( Xinitial + 20*(len(mycards)-1) + LARGURA_CARTA - i - 20, 400))
            baralho.desenhar(tela, mycards[-1], Xinitial + 20*(len(mycards)-1) + LARGURA_CARTA - i + 10, 400, True)    
            tela.blit(thinger, ( Xinitial + 20*(len(mycards)-1) + LARGURA_CARTA - i - 20, 400))  
            if i >= numberAnim:
                state = 'playBlackjack'
                if len(cardsValue(mycards)) == 0:
                    state = 'endBlackjack'
                    winner = 'Dealer'
        elif state == 'DanimBlackjack':
            baralho.desenharMao(tela, mycards, Xinitial, 400)
            baralho.desenharMao(tela, dlcards[:-1], Xinitial, 50)
            tela.blit(hand, ( Xinitial + 20*(len(dlcards)-1) + LARGURA_CARTA - i - 20, 50))
            baralho.desenhar(tela, dlcards[-1], Xinitial + 20*(len(dlcards)-1) + LARGURA_CARTA - i + 10, 50, True)
            tela.blit(thinger, ( Xinitial + 20*(len(dlcards)-1) + LARGURA_CARTA - i - 20, 50))  
            if i >= numberAnim:
                i = 0
                if len(cardsValue(dlcards)) == 0: # Arrebentou
                    state = 'endBlackjack'
                    winner = 'Player'
                    cash += betValue * 2
                else:
                    m = max(cardsValue(mycards))
                    md = max(cardsValue(dlcards))
                    if md < 17: # Pedir mais uma carta
                        card = pickCard(cards)
                        cards.remove(card)
                        dlcards.append(card)
                    else:
                        if m > md:
                            winner = 'Player'
                            cash += betValue * 2
                        elif m < md:
                            winner = 'Dealer'
                        else:
                            winner = ''
                            cash += betValue     
                        state = 'endBlackjack'
            


        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Executar o jogo
if __name__ == "__main__":
    main()
