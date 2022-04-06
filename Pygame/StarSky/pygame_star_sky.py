import pygame
from pygame.locals import *
import tkinter
import random
import sys

SIZE = WIDTH, HEIGHT = tkinter.Tk().winfo_screenwidth(), tkinter.Tk().winfo_screenheight()
STARS_COUNT = 600
STARS = []

window = pygame.display.set_mode(SIZE, FULLSCREEN)
clock = pygame.time.Clock()


class Star:
    def __init__(self, x, y):
        self.coord = [x, y]
        self.x = x
        self.y = y
        self.star_radius = random.randint(1, 4)
        self.speed = 200
        self.center_x = 500
        self.center_y = 500

    def draw(self):
        pygame.draw.circle(window, (255, 255, 255), self.coord, self.star_radius)

    def move(self):
        leg_x = self.center_x - self.coord[0]  # катет x
        leg_y = self.center_y - self.coord[1]  # катет y
        self.coord[0] -= (leg_x / self.speed)
        self.coord[1] -= (leg_y / self.speed)

        self.star_radius += abs(1000 - min(self.coord[0], self.coord[1])) / 20000

        if self.coord[1] > HEIGHT:
            self.coord[1] = self.y
            self.star_radius = random.randint(1, 4)
        if self.coord[1] < 0:
            self.coord[1] = self.y
            self.star_radius = random.randint(1, 4)
        if self.coord[0] > WIDTH:
            self.coord[0] = self.x
            self.star_radius = random.randint(1, 4)
        if self.coord[0] < 0:
            self.coord[0] = self.x
            self.star_radius = random.randint(1, 4)

    def speed_up(self):
        if self.speed > 4:
            self.speed -= 2

    def speed_down(self):
        self.speed += 2

    def mouse_direction(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.center_x, self.center_y = mouse_x, mouse_y


def fill_stars():
    for i in range(STARS_COUNT):
        x = random.randrange(100, 1800)
        y = random.randrange(100, 900)
        STARS.append(Star(x, y))


def main():
    fill_stars()

    while True:
        clock.tick(60)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit()

        if keys[K_w]:
            for star in STARS:
                star.speed_up()
        if keys[K_s]:
            for star in STARS:
                star.speed_down()

        for star in STARS:
            star.draw()
            star.move()
            star.mouse_direction()

        pygame.display.flip()
        window.fill((0, 0, 0))


if __name__ == '__main__':
    main()