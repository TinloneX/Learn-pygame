#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame


class Ship(object):
    def __init__(self, screen, settings):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.settings = settings
        # 加载图片并获取其外部矩形
        self.image = pygame.image.load('../images/my_ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_lift = False
        self.center = float(self.rect.centerx)

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_x
        if self.moving_lift and self.rect.left > 0:
            self.center -= self.settings.ship_speed_x
            # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def draw(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
