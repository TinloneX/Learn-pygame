#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep

import pygame
import sys

from bean.alien import Alien
from bean.bullet import Bullet


def get_number_aliens_x(settings, screen):
    """创建一个外星人并计算一行的容量"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    # 外星人间距为 1/4 外星人宽
    alien_space_w = 1.25 * alien_width
    limited_space_x = settings.screen_width - alien_space_w
    number_alien_x = int(limited_space_x / alien_space_w)
    return int(number_alien_x)


def get_number_aliens_y(settings, screen, ship):
    """创建一个外星人并计算每列容量"""
    alien = Alien(settings, screen)
    alien_height = alien.rect.height
    limited_space_y = settings.screen_height - alien_height * 3 - ship.rect.height
    return int(limited_space_y / (2 * alien_height))


def create_alien(settings, screen, aliens, index, row):
    """创建单个敌人并加入外星人群"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    # 计算外星人及间距所占宽
    space_x = 1.25 * alien_width
    # 计算外星人及间距所占高
    space_y = 2 * alien.rect.height
    # 计算坐标值
    alien.x = alien_width + space_x * index
    alien.y = alien_height + space_y * row
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def filled_aliens(settings, screen, ship, aliens):
    """创建外星人群"""
    # 遍历创建列
    for row in range(get_number_aliens_y(settings, screen, ship)):
        # 遍历创建行
        for index in range(get_number_aliens_x(settings, screen)):
            create_alien(settings, screen, aliens, index, row)


def check_aliens_edges(settings, aliens):
    """检查外星人是否触边"""
    for alien in aliens.sprites():
        # 若外星人处在屏幕边缘
        if alien.check_edges():
            change_aliens_direction(settings, aliens)
            break


def change_aliens_direction(settings, aliens):
    """外星人触边操作"""
    for alien in aliens.sprites():
        alien.rect.y += settings.alien_drop_y
    # 改变x位移方向
    settings.alien_direction *= -1


def check_event(settings, screen, ship, bullets, aliens, stats, btn_play_or_pause):
    """按键监听"""
    for event in pygame.event.get():
        # 监听退出事件
        if event.type == pygame.QUIT:
            sys.exit()
        # 监听按键按下
        elif event.type == pygame.KEYDOWN:
            __event_key_down(event, settings, screen, ship, bullets, aliens, stats)
        # 监听按键抬起
        elif event.type == pygame.KEYUP:
            __event_key_up(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            __check_play_button(settings, screen, ship, bullets, aliens, stats, btn_play_or_pause, mouse_x, mouse_y)


def __check_play_button(settings, screen, ship, bullets, aliens, stats, btn_play_or_pause, mouse_x, mouse_y):
    button_clicked = btn_play_or_pause.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        __play_game(settings, screen, ship, bullets, aliens, stats)


def __play_game(settings, screen, ship, bullets, aliens, stats):
    stats.game_active = True
    stats.reset_stats()
    settings.reset_speed()
    reload_game(settings, screen, ship, bullets, aliens)
    pygame.mouse.set_visible(False)


def __shoot_bullet(settings, screen, ship, bullets):
    """产生子弹，并存储在子弹组中"""
    if len(bullets) < settings.bullet_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def __event_key_down(event, settings, screen, ship, bullets, aliens, stats):
    """处理按键按下事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_lift = True
    elif event.key == pygame.K_SPACE:
        __shoot_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p and not stats.game_active:
        __play_game(settings, screen, ship, bullets, aliens, stats)


def __event_key_up(event, ship):
    """处理按键抬起事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_lift = False


def update_bullets(settings, screen, ship, bullets, aliens, stats, score_board):
    """处理移除屏幕外的子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_aliens_gone(settings, screen, ship, bullets, aliens, stats, score_board)


def check_aliens_gone(settings, screen, ship, bullets, aliens, stats, score_board):
    """处理子弹和外星人的碰撞"""
    collide = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collide:
        for als in collide.values():
            stats.score += settings.alien_score * len(als)
            score_board.prep_score()

    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        filled_aliens(settings, screen, ship, aliens)


def update_aliens(settings, stats, screen, ship, bullets, aliens):
    """更新外星人群"""
    # 检查是否位于屏幕边缘
    check_aliens_edges(settings, aliens)
    aliens.update()
    # 检查alien是否触底
    check_aliens_bottom(settings, stats, screen, ship, bullets, aliens)
    # 检查飞船是否被撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, bullets, aliens)


def reload_game(settings, screen, ship, bullets, aliens):
    aliens.empty()
    bullets.empty()
    filled_aliens(settings, screen, ship, aliens)
    ship.center_ship()


def ship_hit(settings, stats, screen, ship, bullets, aliens):
    """飞船扣血响应"""
    if stats.ship_life > 0:
        stats.ship_life -= 1
        reload_game(settings, screen, ship, bullets, aliens)
        sleep(0.5)
    else:
        # game over
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(settings, stats, screen, ship, bullets, aliens):
    """检查alien是否触底"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, bullets, aliens)
            break


def update_screen(settings, screen, ship, bullets, aliens, stats, btn_play_or_pause, score_board_now):
    """更新屏幕上的图像，并切换到新的屏幕"""
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw()
    # 绘制飞船
    ship.draw()
    aliens.draw(screen)
    score_board_now.show_score()
    if not stats.game_active:
        btn_play_or_pause.draw()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
