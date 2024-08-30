import pygame

class Botao:
    def __init__(self, x, y, w, h, texto, cor, cor_texto=(0, 0, 0), fonte=None, border_radius=10, hover_color = (255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.texto = texto
        self.cor = cor
        self.cor_texto = cor_texto
        self.fonte = pygame.font.Font(fonte, 36) if fonte else pygame.font.Font(None, 36)
        self.border_radius = border_radius
        self.active = False
        self.hc = hover_color

    def desenhar(self, tela):
        if self.active:
            pygame.draw.rect(tela, self.hc, (self.x, self.y, self.w, self.h), border_radius=self.border_radius)
        else:
            pygame.draw.rect(tela, self.cor, (self.x, self.y, self.w, self.h), border_radius=self.border_radius)
        texto_renderizado = self.fonte.render(self.texto, True, self.cor_texto)
        texto_retangulo = texto_renderizado.get_rect(center=(self.x + self.w // 2, self.y + self.h // 2))
        tela.blit(texto_renderizado, texto_retangulo)

    def foi_clicado(self, posicao):
        return self.x <= posicao[0] <= self.x + self.w and self.y <= posicao[1] <= self.y + self.h
    
    def ativar(self, pos):
        if self.foi_clicado(pos):
            self.active = True
        else:
            self.active = False
