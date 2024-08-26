import pygame
import sys
from button import Botao
from carta import Carta 
from carta import refilCards

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


playB = Botao(100, 100, 200, 50, "Play", DARK_BLUE)
exitB = Botao(100, 200, 200, 50, "Exit", DARK_BLUE)
giveB = Botao(100, 200, 200, 50, "Give", GREEN)
stopB = Botao(100, 300, 200, 50, "Stop", RED)
backB = Botao(2, 2, 30, 30, "<", WHITE)




LARGURA_CARTA = 440 // 5  
ALTURA_CARTA = 372 // 3   

def main():
    jogo_em_execucao = True
    baralho = Carta(LARGURA_CARTA, ALTURA_CARTA)
    cards = refilCards()
    state = 'menu'
    valor = 0

    #Create cards
    for i in 'CDHS':
        for j in 'A2345678910JQK':
            cards.append(j+i)
    while jogo_em_execucao:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_em_execucao = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if state == 'menu':
                    if playB.foi_clicado(evento.pos):
                        state = 'play'
                    elif exitB.foi_clicado(evento.pos):
                        jogo_em_execucao = False
                elif state == 'play':
                    if backB.foi_clicado(evento.pos):
                        state = 'menu'
                    elif giveB.foi_clicado(evento.pos):

                    
        tela.fill(COR_FUNDO)
        if state == 'menu':
            playB.desenhar(tela)
            exitB.desenhar(tela)
        elif state == 'play':
            giveB.desenhar(tela)
            stopB.desenhar(tela)
            backB.desenhar(tela)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Executar o jogo
if __name__ == "__main__":
    main()
