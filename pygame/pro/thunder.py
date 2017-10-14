import math, pygame, sys, random

from pygame.locals import *

pygame.init()
screen_width = 450
screen_height = 700
black = 0, 0, 0
white = 255, 255, 255
pygame.display.set_caption("Thunder")
screen = pygame.display.set_mode((screen_width, screen_height))
plane = pygame.image.load("img/man.png").convert_alpha()


class Bullet(object):
    def __init__(self, image, site_x, site_y):
        self.image = image
        self.site_x = site_x
        self.site_y = site_y
        self.image = pygame.transform.smoothscale(self.image, (40, 80))

    def load_image(self):
        screen.blit(self.image, (self.site_x, self.site_y))


bullet = Bullet(pygame.image.load("img/man.png").convert_alpha(), 200, 300)
# bullet.load_image()
# bullet = pygame.image.load("img/man.png").convert_alpha()
# bullet = pygame.transform.smoothscale(bullet, 40, 80)
bullet_list = [bullet] * 5


def change_bullet_random_init_site(alist):  # 改变子弹的初始位置
    for


change_bullet_random_init_site(bullet_list)
print("over")
print(bullet_list[0].site_x)
print(bullet_list[1].site_x)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # screen.fill(black)
    pygame.display.update()
