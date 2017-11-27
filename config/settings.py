#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Settings(object):
    """储存游戏设置的类"""

    def __init__(self):
        # 初始化屏幕参数
        self.__init_screen()
        # 初始化飞船参数
        self.__init_ship()
        # 初始化子弹参数
        self.__init_bullet()
        # 初始化外星人参数
        self.__init_aliens()

    def __init_screen(self):
        """初始化屏幕参数"""
        self.game_name = 'AlienInvasion'
        self.screen_width = 800
        self.screen_height = 600
        self.screen_display = (self.screen_width, self.screen_height)
        self.bg_color = (230, 230, 230)

    def __init_ship(self):
        """初始化飞船参数"""
        # 飞船水平飞行速度
        self.ship_speed_x = 1.5
        self.ship_life = 3

    def __init_bullet(self):
        """初始化子弹参数"""
        # 子弹垂直飞行速度
        self.bullet_speed_y = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 限制单屏子弹射出上限
        self.bullet_allowed = 5

    def __init_aliens(self):
        self.alien_speed_x = 1
        self.alien_speed_y = 1
        self.alien_drop_y = 10
        self.alien_direction = 1

