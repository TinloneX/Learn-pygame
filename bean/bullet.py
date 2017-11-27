#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """对飞船发射子弹进行管理的类"""
    def __init__(self, settings, screen, ship):
        super(Bullet, self).__init__()

        self.screen = screen
        # 在0,0位置创建一个子弹矩形
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        # 指定子弹矩形的初始位置
        self.rect.centerx = ship.rect.centerx
        # 指定子弹的初始高度和飞船高度一致
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = settings.bullet_color
        self.speed_y = settings.bullet_speed_y

    def update(self):
        """更新子弹的移动"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_y
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

