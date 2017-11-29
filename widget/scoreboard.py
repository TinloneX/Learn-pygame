#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame


class ScoreBoard(object):
    """显示得分信息的类"""
    def __init__(self, settings, screen, stats):
        """初始化现实得分需要的属性"""
        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.screen_rect = screen.get_rect()

        # 显示得分信息使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
