__author__ = 'Makar'

import pygame, sys
from Mikrob import Mikrob
from functions import *
from random import randint, choice
from Bakteria import Bakteria

pygame.init()

size = screen_width, screen_height = [640, 420]
bg_color=[0,0,0]
number_mikrob=3
number_bakteria=3
screen = pygame.display.set_mode(size)
mikrob_body="mikrob-body.png"
bakteria_body="bakteria-body.png"
mikrobs=pygame.sprite.Group()
bakterias=pygame.sprite.Group()
for i in range(number_mikrob):
    mik = Mikrob(
        mikrob_body,create_genom(),
        [randint(0,screen_width),randint(0,screen_height)],
        (choice([-1,1]), choice([-1,1])),
        screen, 0.1)
    mikrobs.add(mik)


for i in range(number_bakteria):
    bak = Bakteria(
        bakteria_body,
        [randint(0,screen_width),randint(0,screen_height)],
        (0, 1),
        screen, 0.09)
    bakterias.add(bak)

clock=pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    time_passed=clock.tick(50)

    screen.fill(bg_color)
    for mikrob in mikrobs:
        mikrob.update(time_passed)
        mikrob.draw(screen)

        if pygame.sprite.spritecollide(mikrob,bakterias, True):
            print "1"


    for bakteria in bakterias:
        bakteria.update(time_passed)
        bakteria.draw(screen)



    pygame.display.update()
