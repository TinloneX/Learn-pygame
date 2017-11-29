#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Group

from bean.alien import Alien
from config.settings import Settings
from bean.ship import Ship
import control.game_function as gf
from config.stats import GameStats
from widget.button import Button
from widget.scoreboard import ScoreBoard


def run_game():
    # 初始化并创建一个屏幕对象
    pygame.init()
    settings = Settings()
    settings.bg_color = (255, 255, 255)
    screen = pygame.display.set_mode(settings.screen_display)
    pygame.display.set_caption(settings.game_name)
    ship = Ship(screen, settings)
    bullets = Group()
    aliens = Group()
    gf.filled_aliens(settings, screen, ship, aliens)
    stats = GameStats(settings)
    btn_play_or_pause = Button(screen, 'PLAY')
    score_board_now = ScoreBoard(settings, screen, stats)

    while True:
        gf.check_event(settings, screen, ship, bullets, aliens, stats, btn_play_or_pause)
        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, ship, bullets, aliens, stats, score_board_now)
            gf.update_aliens(settings, stats, screen, ship, bullets, aliens)
        gf.update_screen(settings, screen, ship, bullets, aliens, stats, btn_play_or_pause, score_board_now)


run_game()
