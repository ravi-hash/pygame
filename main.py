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

# Function to check for collisions
def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

# Game loop
def main():
    player = Player(screen_width // 2, screen_height - 60)
    enemies = [Enemy(random.randint(0, screen_width - 64), random.randint(-150, -50)) for _ in range(10)]
    bullets = []
    score = 0
    clock = pygame.time.Clock()
    
    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-player.speed)
        if keys[pygame.K_RIGHT]:
            player.move(player.speed)
        if keys[pygame.K_SPACE]:
            if len(bullets) < 5:
                bullets.append(Bullet(player.rect.centerx, player.rect.top))

        player.draw()
        
        for bullet in bullets:
            bullet.move()
            bullet.draw()
            if bullet.rect.y < 0:
                bullets.remove(bullet)

        for enemy in enemies:
            enemy.move()
            enemy.draw()
            if enemy.rect.y > screen_height:
                enemies.remove(enemy)
                enemies.append(Enemy(random.randint(0, screen_width - 64), random.randint(-150, -50)))
            
            for bullet in bullets:
                if check_collision(enemy.rect, bullet.rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    enemies.append(Enemy(random.randint(0, screen_width - 64), random.randint(-150, -50)))
                    break

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
