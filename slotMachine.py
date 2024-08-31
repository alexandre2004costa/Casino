import pygame
import random
import sys

class slotM:
    def __init__(self):
        self.symbols = [pygame.image.load(f'slots/slot-symbol{i}.png') for i in range(1,5)]
        self.machine = [pygame.image.load(f'slots/slot-machine{i}.png') for i in range(1,6)]
        self.mode = 'stoped'
        self.ydiff = 110
        self.count = 0
        self.rate = 99
        self.inside = [[self.symbols[0]] * 3,[self.symbols[1]] * 3,[self.symbols[2]] * 3]

    def desenhar(self, tela):
        ix = 235
        y = 250
        if self.mode == 'stoped':
            tela.blit(self.machine[0],(0,0))
            for i in self.inside:
                tela.blit(i[0], (ix, y - self.ydiff))
                tela.blit(i[1], (ix, y))
                tela.blit(i[2], (ix, y + self.ydiff))
                ix += 130
            tela.blit(self.machine[3],(0,0))
            tela.blit(self.machine[1],(0,0))

        elif self.mode == 'pushed':
            
            if self.count >= 55 and self.rate <= 1:
                self.rate == 0
                self.res()
            else:
                self.count += self.rate
            tela.blit(self.machine[4],(0,0))
        
            for i in self.inside:
                tela.blit(i[0], (ix, y - self.ydiff + self.count))
                tela.blit(i[1], (ix, y + self.count))
                tela.blit(i[2], (ix, y + self.ydiff + self.count))
                ix += 130

            
            tela.blit(self.machine[3],(0,0))
            tela.blit(self.machine[2],(0,0))
            if self.count >= self.ydiff:
                for i in range(len(self.inside)):
                    simbolo_aleatorio = self.symbols[random.randint(0, 3)]
                    self.inside[i].pop()
                    self.inside[i].insert(0, simbolo_aleatorio)
                self.count = 0
                self.rate = max(0, self.rate - 2)
    
    def push(self):
        self.mode = 'pushed'
        self.count = 0

    def res(self):
        fst = self.inside[0][1]
        sec = self.inside[1][1]
        thr = self.inside[2][1]
        if fst == sec and fst == thr:
            print("WIN")
        elif fst == sec or fst == thr or thr == sec:
            print("TIE")
        else:
            print("LOST")


        




        