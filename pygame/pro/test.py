# 下面的报错是pycharm的bug
import math
import pygame
import sys

from datetime import datetime, date, time
from pygame.locals import *

pygame.init()
screenTitle = pygame.display.set_caption('Hello World')
screen = pygame.display.set_mode([1200, 650])

white = 255, 255, 255
blue = 45, 72, 200
black = 0, 0, 0

color = 255, 255, 0
# position = 600, 250
# radius = 40
#
# pos_x = 600
# pos_y = 350
# vel_x = 2
# vel_y = 1

# myFont = pygame.font.SysFont("consolas", 60)
# part_1 = False
# down_1 = False
# part_2 = False
# down_2 = False
# part_3 = False
# down_3 = False

# pos_x = 200
# pos_y = 300

# pos1 = pos_x, pos_y, 200, 100
# pos2 = pos_x + 250, pos_y, 200, 100
# pos3 = pos_x + 500, pos_y, 200, 100
# success = False

# today = datetime.today()
# print(today.time().hour)
# print(pygame.font.get_fonts())
man = pygame.image.load("img/man.png").convert_alpha()
keys = pygame.key.get_pressed()
pos_x = 400
pos_y = 200

pos_add_x = 4
pos_add_y = 4

screen.blit(man, (400, 200))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == 100:           # D
        #         pos_x += pos_add_x
        #     elif event.key == 119:         # W
        #         pos_y -= pos_add_y
        #     elif event.key == 97:          # A
        #         pos_x -= pos_add_x
        #     elif event.key == 115:         # S
        #         pos_y += pos_add_y
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_ESCAPE:
        #         sys.exit()
        #     elif event.key == pygame.K_1:
        #         if down_1:  # 该键位已经被按下
        #             down_1 = False
        #             part_1 = False
        #         else:
        #             down_1 = True
        #             part_1 = True
        #     elif event.key == pygame.K_2:
        #         if down_2:
        #             down_2 = False
        #             part_2 = False
        #         else:
        #             down_2 = True
        #             part_2 = True
        #     elif event.key == pygame.K_3:
        #         if down_3:
        #             down_3 = False
        #             part_3 = False
        #         else:
        #             down_3 = True
        #             part_3 = True
        # if part_1 and part_2 and part_3:
        #     success = True
        # else:
        #     success = False
        # if success:
        #     color = 0, 255, 255
        # else:
        #     color = 255, 255, 0
        # if part_1:
        #     pygame.draw.rect(screen, color, pos1, 0)
        # else:
        #     pygame.draw.rect(screen, black, pos1, 0)
        # if part_2:
        #     pygame.draw.rect(screen, color, pos2, 0)
        # else:
        #     pygame.draw.rect(screen, black, pos2, 0)
        # if part_3:
        #     pygame.draw.rect(screen, color, pos3, 0)
        # else:
        #     pygame.draw.rect(screen, black, pos3, 0)
    # screen.fill(blue)
    # screen.blit(textImage, (400, 100))

    # pygame.draw.circle(screen, black, position, radius, 1)

    # pos_x += vel_x
    # pos_y += vel_y
    # if pos_x > 1000 or pos_x < 0:
    #     vel_x = -vel_x
    # if pos_y > 550 or pos_y < 0:
    #     vel_y = -vel_y
    #
    # pos = pos_x, pos_y, 200, 100
    # pygame.draw.rect(screen, color, pos, 0)

    # pygame.draw.line(screen, color, (100, 200), (1000, 400), 15)

    # position = 800, 150, 200, 200
    # pygame.draw.arc(screen, color, position, math.radians(20), math.radians(120), 1)
    # pos = (pos_x, pos_y)
    # screen.blit(space, pos)
    pygame.display.update()
