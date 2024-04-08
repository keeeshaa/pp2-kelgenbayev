import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
screen_w = 600
screen_h = 600
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK =(0, 0, 0)
radius = 25
x = screen_w / 2
y = screen_h / 2
speed = 20

while True:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    pygame.draw.rect(screen, BLACK, (0, 0, 600, 600), 15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if y - speed >= radius:
            y -= speed
    if pressed[pygame.K_DOWN]:
        if y + speed <= screen_h - radius:
            y += speed
    if pressed[pygame.K_LEFT]:
        if x - speed >= radius:
            x -= speed
    if pressed[pygame.K_RIGHT]:
        if x + speed <= screen_h - radius:
            x += speed
    pygame.display.flip()
    clock.tick(30)