import pygame

class Carta:
    def __init__(self, largura_carta, altura_carta):
        self.largura_carta = largura_carta
        self.altura_carta = altura_carta
        self.naipes = ['C', 'D', 'H', 'S']  # Clubs, Diamonds, Hearts, Spades
        self.valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def obter_posicao_carta(self, carta):
        valor = carta[0]  # Extrai o valor da carta (A, 2, 3, ..., K)
        
        coluna = self.valores.index(valor) % 5
        linha = self.valores.index(valor) // 5

        return linha, coluna

    def desenhar(self, tela, carta, x, y):
        folha = pygame.image.load(f'Top-Down/Cards/{carta[1]}.png').convert_alpha();
        linha, coluna = self.obter_posicao_carta(carta)
        area_carta = pygame.Rect(coluna * self.largura_carta, linha * self.altura_carta, self.largura_carta, self.altura_carta)
        tela.blit(folha, (x, y), area_carta)

def refilCards():
    cards = []
    for i in 'CDHS':
        for j in 'A2345678910JQK':
            cards.append(j+i)
    return cards
