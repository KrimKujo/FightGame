import pygame
from game import Game

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Fighting Game")
pygame.display.set_icon(pygame.image.load('assets/logo.png'))

game = Game(screen)
if __name__ == '__main__':
    pygame.init()
    game.run()
    pygame.quit()
