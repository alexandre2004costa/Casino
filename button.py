import pygame

class Botao:
    def __init__(self, x, y, w, h, texto, cor):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.texto = texto
        self.cor = cor
        self.fonte = pygame.font.Font(None, 36)

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.w, self.h))
        texto_renderizado = self.fonte.render(self.texto, True, (0, 0, 0))
        texto_retangulo = texto_renderizado.get_rect(center=(self.x + self.w // 2, self.y + self.h // 2))
        tela.blit(texto_renderizado, texto_retangulo)

    def foi_clicado(self, posicao):
        if self.x < posicao[0] < self.x + self.w and self.y < posicao[1] < self.y + self.h:
            return True
        return False
