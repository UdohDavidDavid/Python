import pygame
from configs import *
import sys

class GAME:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((window_width, window_height))
        self.caption = pygame.display.set_caption("Pygame window")
        self.clock = pygame.Clock()
        self.running = True

    def run():
        while running:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    running = False
                    sys.exit()

            self.window.fill()
            pygame.display.flip()
            self.clock.tick(FPS)
