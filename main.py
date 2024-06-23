import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 36)

# Load images from local machine
player_img = pygame.image.load('player.png')
enemy_img = pygame.image.load('enemy.png')
bullet_img = pygame.image.load('bullet.png')
ufo_img = pygame.image.load('ufo.png')
powerup_img = pygame.image.load('powerup.png')

# Player class
class Player:
    def __init__(self, x, y):
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def move(self, dx):
        if 0 <= self.rect.x + dx <= screen_width - self.rect.width:
            self.rect.x += dx

    def draw(self):
        screen.blit(self.image, self.rect.topleft)

# Enemy class
class Enemy:
    def __init__(self, x, y):
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1

    def move(self):
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect.topleft)

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = -5

    def move(self):
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect.topleft)


if __name__ == "__main__":
    main()
