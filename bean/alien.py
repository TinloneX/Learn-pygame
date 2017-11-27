#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('../images/ep_13.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width / 4
        self.rect.y = self.rect.height / 4
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_right = self.screen.get_rect().right
        if self.rect.right >= screen_right:
            return True
        elif self.rect.left <= 0:
            return True

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """移动外星人"""
        self.x += (self.settings.alien_speed_x *
                   self.settings.alien_direction)
        self.rect.x = self.x
        # self.y += self.settings.alien_speed_y
        # self.rect.y = self.y
