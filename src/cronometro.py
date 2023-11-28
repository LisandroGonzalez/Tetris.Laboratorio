from settings import *
from os import path

class Cronometro:
    def __init__(self):
        self.superficie = pygame.Surface((SIDEBAR_ANCHO, PADDING))
        self.rect = self.superficie.get_rect(bottomright = (ANCHO_VENTANA - (PADDING * 2 + SIDEBAR_ANCHO), ALTURA_VENTANA - 280))
        self.superficie_display = pygame.display.get_surface()
        
        self.aux = 1
        
        self.fuente = pygame.font.Font(path.join('./src/imagenes','BebasNeue-Regular.ttf'),20)
        
    def run(self):
        self.superficie.fill(GRIS)
        tiempo = pygame.time.get_ticks()
        minutos = int(tiempo / 1000 / 60)
        segundos = int(tiempo / 1000) % 60
        milisegundos = tiempo % 1000
        
        crono = self.fuente.render(f"Tiempo: {minutos}:{segundos}:{milisegundos}", True, "white")
        self.superficie.blit(crono, (0,0))
        self.superficie_display.blit(self.superficie,self.rect)
