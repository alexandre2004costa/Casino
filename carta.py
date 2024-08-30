import pygame
import random

class Carta:
    def __init__(self, largura_carta, altura_carta):
        self.largura_carta = largura_carta
        self.altura_carta = altura_carta
        self.naipes = ['C', 'D', 'H', 'S']  # Clubs, Diamonds, Hearts, Spades
        self.valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'] # T is 10

    def obter_posicao_carta(self, carta):
        valor = carta[0] 
        
        coluna = self.valores.index(valor) % 5
        linha = self.valores.index(valor) // 5

        return linha, coluna

    def desenhar(self, tela, carta, x, y, hide = False):
        if hide:
            folha = pygame.image.load('Top-Down/Cards/cb.png').convert_alpha()
            area_carta = pygame.Rect(0, 0, self.largura_carta, self.altura_carta)
            tela.blit(folha, (x, y), area_carta)
            return  
        folha = pygame.image.load(f'Top-Down/Cards/{carta[1]}.png').convert_alpha();
        linha, coluna = self.obter_posicao_carta(carta)
        area_carta = pygame.Rect(coluna * self.largura_carta, linha * self.altura_carta, self.largura_carta, self.altura_carta)
        tela.blit(folha, (x, y), area_carta)

    def desenharMao(self, tela, cards, ix, iy, hide = False):
        for i in cards:
            self.desenhar(tela, i, ix, iy, hide)
            ix += 20


def refilCards():
    cards = []
    for i in 'CDHS':
        for j in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
            cards.append(j+i)
    return cards

def pickCard(cards):
    index = random.randint(0, len(cards) - 1)
    return cards[index]

def cardsValue(cards):
    valores_cartas = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,'J': 10, 'Q': 10, 'K': 10}
    valores_possiveis = [0]
    numero_ases = 0

    for carta in cards:
        valor = carta[0]
        if valor == 'A':
            numero_ases += 1
        else:
            for i in range(len(valores_possiveis)):
                valores_possiveis[i] += valores_cartas[valor]

    for _ in range(numero_ases):
        novos_valores = []
        for valor in valores_possiveis:
            if valor + 1 <= 21:
                novos_valores.append(valor + 1)  
            if valor + 11 <= 21:
                novos_valores.append(valor + 11)  
        valores_possiveis = novos_valores

    valores_possiveis = sorted(set(valores_possiveis))
    m = []
    for i in valores_possiveis:
         if i <= 21:
            m.append(i)
    return m

        