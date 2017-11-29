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
        # 设置速度加速比
        self.speedup_scale = 1.1

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
        """初始化外星人属性"""
        self.alien_speed_x = 1
        self.alien_speed_y = 1
        self.alien_drop_y = 10
        self.alien_direction = 1
        self.alien_score = 10

    def reset_speed(self):
        """重置各速度"""
        self.__init_ship()
        self.__init_aliens()
        self.__init_bullet()

    # noinspection PyAttributeOutsideInit
    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_x *= self.speedup_scale
        self.bullet_speed_y *= self.speedup_scale
        self.alien_speed_y *= self.speedup_scale
        self.alien_score = int(self.alien_score * self.speedup_scale)
        if self.alien_drop_y <= 22:
            self.alien_drop_y *= self.speedup_scale

