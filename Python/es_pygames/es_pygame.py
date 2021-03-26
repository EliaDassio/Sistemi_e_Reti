import pygame #installata da noi
import sys #nativa

DIMENSION = (600,600)
BLACK = (0,0,0)
WHITE = (255,255,255)

def drawgrid():
     pass

def main():
    pygame.init()
    global finestra #window o finestra
    finestra = pygame.display.set_mode(DIMENSION)
    finestra.fill(BLACK)
    while True:
        drawgrid()
        #ciclo for gestione eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main()