import pygame, sys,math
from vec2d import vec2d
from random import *
from functions import *

class Mikrob(pygame.sprite.Sprite):
    def __init__(self, body_image,init_genom, init_position, init_direction, screen, displacement):
        pygame.sprite.Sprite.__init__(self)
        self.body_img = pygame.image.load(body_image).convert_alpha()
        self.image=self.body_img
        self.pos=init_position
        self.direction=vec2d(init_direction).normalized()
        self.displacement=displacement
        self.screen=screen
        self._counter=0
        self.genom=init_genom
        self.energy=randint(100,600)


    def update(self,time_passed):
        if self.energy>0:

            self._change_direction(time_passed)
            self.image=pygame.transform.rotate(self.body_img,-self.direction.angle)


            displacement=vec2d(
                self.direction.x*self.displacement*time_passed,
                self.direction.y*self.displacement*time_passed)

            self.pos+=displacement

            self.image_w, self.image_h =self.image.get_size()

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
            self.energy-=0.5




    def draw(self, screen):
        draw_pos=self.image.get_rect().move(
            self.pos.x-self.image_w / 2,
            self.pos.y-self.image_h / 2
        )
        screen.blit(self.image,draw_pos)

    def _change_direction(self,time_passed):
        self._counter+=time_passed
        if self._counter>randint(400,500):
            _gen=random.choice(self.genom)
            self.direction.rotate(gen2angle(_gen))
            self._counter=0
            










