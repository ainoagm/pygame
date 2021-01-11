import pygame as     pg
import sys
import random

class Game:
    def __init__(self):
        self.pantalla = pg.display.set_mode((888,600))
        pg.display.set_caption("Futuro Arkanoid")


    def bucle_principal(self):
        game_over = False
        while not game_over:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.pantalla.fill((0,0,255))#surface es un modulo para superponer imagenes

            pg.display.flip()#instrucción de actualizar todo lo que haces en la pantalla. Al final del bucle, como última instrucción.

if __name__ == '__main__':
    pg.init()
    game = Game()
    game.bucle_principal()
