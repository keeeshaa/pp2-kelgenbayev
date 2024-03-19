import pygame
import sys
from datetime import datetime
import math

res = width, height = 800, 800
half_width, half_height = width // 2, height // 2
radius = half_height - 50

clock12 = dict(zip(range(12), range(0, 360, 30)))
clock60 = dict(zip(range(60), range(0, 360, 6)))
clock = pygame.time.Clock()
background_image = pygame.image.load("C:\\Users\\Admin\\Desktop\\pp2\\lab7\clock\\images\\main_clock.png")

def get_clock_pos(clock_dict, clock_hand):
    x = half_width + radius * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = half_height + radius * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


class MickeyHand:
    def __init__(self, screen, image_path):
        self.screen = screen
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.origin = (half_width, half_height) 
        self.angle = 0  

    def update(self, angle):
        self.angle = angle

    def draw(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.origin)
        self.screen.blit(rotated_image, rotated_rect)

def run():
    pygame.init()
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Mickey clock")
    bg_color = (255, 255, 255)

    left_mickey_hand = MickeyHand(screen, "C:\\Users\\Admin\\Desktop\\pp2\\lab7\clock\\images\\left_hand.png")

    right_mickey_hand = MickeyHand(screen, "C:\\Users\\Admin\\Desktop\\pp2\\lab7\\clock\\images\\right_hand.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(bg_color)
        screen.blit(background_image, (0, 0))

        t = datetime.now()
        hour = t.hour % 12 

        hour_angle = clock12[hour]

        right_mickey_hand.update(hour_angle)

        left_mickey_hand.draw()
        right_mickey_hand.draw()

        pygame.display.flip()
        clock.tick(20)

run()
