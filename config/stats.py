#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class GameStats(object):
    """游戏信息统计"""
    def __init__(self, setting):
        self.setting = setting
        self.game_active = False
        # 初始化飞船信息
        self.__init_ship()

    def __init_ship(self):
        self.ship_life = self.setting.ship_life

    def reset_stats(self):
        """重置游戏过程中可能改变的值"""
        # 初始化飞船信息
        self.__init_ship()

