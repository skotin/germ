#!/usr/bin/env python2.5
# -*- coding: utf-8 -*-
__author__ = 'Макар'

import pygame, functions, sys,math
from vec2d import vec2d
from random import randint

class Bakteria(pygame.sprite.Sprite):
    def __init__(self, body_image, init_position, init_direction, screen, displacement):
        pygame.sprite.Sprite.__init__(self)
        self.body_img = pygame.image.load(body_image).convert_alpha()
        self.image=self.body_img
        self.pos=vec2d(init_position)
        self.direction=vec2d(init_direction).normalized()
        self.displacement=displacement
        self.screen=screen
        self.calorie=randint(400,500)


    def update(self,time_passed):
        self.image_w, self.image_h =self.image.get_size()
        self.image=pygame.transform.rotate(self.body_img,-self.direction.angle)

        displacement=vec2d(
            self.direction.x*self.displacement*time_passed,
            self.direction.y*self.displacement*time_passed)

        self.pos+=displacement

        bounds_rect=self.screen.get_rect().inflate(
            -self.image_w, -self.image_h)
        if self.pos.x<bounds_rect.left:
            self.pos.x=bounds_rect.left
            self.direction.x*=-1
        elif self.pos.x>bounds_rect.right:
            self.pos.x=bounds_rect.right
            self.direction.x*=-1
        elif self.pos.y<bounds_rect.top:
            self.pos.y=bounds_rect.top
            self.direction.y*=-1
        elif self.pos.y>bounds_rect.bottom:
            self.pos.y=bounds_rect.bottom
            self.direction.y*=-1


    def draw(self, screen):
        draw_pos=self.image.get_rect().move(
            self.pos.x-self.image_w / 2,
            self.pos.y-self.image_h / 2
        )
        screen.blit(self.image,draw_pos)
