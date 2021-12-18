#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:09:02 2021

@author: elizavetalebosina
"""

"""
Corrected on Wed Sep 22 2021
@author: elizavetalebosina
соавтор - Клячина Алёна
"""

import pygame
from pygame.draw import *
import math


def main():
    
    clock = pygame.time.Clock()
    FPS = 30
    screen = pygame.display.set_mode((800, 900))

    
    window_straight(screen)
    cat_straight(screen)
    cat_scale(screen)
    clew_straight(screen)
    window_rotation(screen)



    pygame.display.update()

    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()
    #background()
    #window(screen, 600, 50, 0.8)
    #window(screen, 300, 50, 0.8)
    #window(screen, 10, 50, 0.8)
    #cat(screen, cat_surface, 550, 450, 2)
    #cat(screen, cat_surface, 400, 700, 4)
    #cat(screen, cat_surface, 620, 730, 4, DARKGRAY, BLUE)
    #cat(screen, cat_surface, 300, 520, 2, DARKGRAY, BLUE, True)
    #cat(screen, cat_surface, 100, 700, 4, DARKGRAY, BLUE, True)
    #cat(screen, cat_surface, 100, 420, 4, BROWN, GREEN, True)
    #cat(screen, cat_surface, 700, 620, 4, BROWN, GREEN, True)
    #clew(screen, clew_surface, 580, 400, 1.4)
    #clew(screen, clew_surface, 150, 550, 0.4)
    #clew(screen, clew_surface, 340, 320, 0.5)
    #clew(screen, clew_surface, 200, 380, 1, True)
    #clew(screen, clew_surface, 550, 500, 0.4, True)
    #clew(screen, clew_surface, 510, 530, 0.7, True)

def background(screen, window_n = False, cat_n = False, clew_n = False):
        '''рисует фон'''
        BG1 = (123, 103, 30)
        BG2 = (82, 69, 17) 
        BLUE = (150, 201, 218)
        DARKGRAY = (51, 51, 51)
        BROWN = (188, 116, 66)
        GREEN = (141, 170, 52)
        rect(screen, BG2, (0, 0, 800, 400))
        rect(screen, BG1, (0, 400, 800, 500))
        if cat_n == True:
            cat(screen, 550, 450, 2, BROWN, GREEN, False)
        if clew_n == True:
            clew(screen, 580, 400, 1.4)
        if window_n == True:
            window(screen, 600, 50, 0.8)
            
def window(screen, x, y, scale=1):
    """
    рисует окно
    screen - поверхность окна
    (x, y) - позиция окна
    scale - масштаб окна относительно исходного
    """
    blue = (150, 201, 218)
    sagegreen = (220, 253, 232)
    rect(screen, sagegreen, (x, y, 250 * scale, 325 * scale))
    rect(screen, blue, (x + 25 * scale, y + 25 * scale, 90 * scale, 75 * scale))
    rect(screen, blue, (x + 135 * scale, y + 25 * scale, 90 * scale, 75 * scale))
    rect(screen, blue, (x + 25 * scale, y + 125 * scale, 90 * scale, 175 * scale))
    rect(screen, blue, (x + 135 * scale, y + 125 * scale, 90 * scale, 175 * scale))

def cat(screen, center_x, center_y, scale=1, main_colour=(188, 116, 66), eyes_colour=(0, 200, 64), flip=False):
    """
    рисует кота/кошку
    screen - экран, на который ложится поверхность кота
    cat_surface - поверхность кота
    (center_x, center_y) - координаты центра кота/кошки
    scale - масштаб относитьно исходного
    main_colour - цвет кота
    eyes_colour - цвет глаз
    flip - отражение (если надо) (flip = False - исходное изображение, flip = True - отраженное)
    """
    pink = (248, 203, 172)
    
     # Поверхность для кота
    PURPLE = (255, 0, 255)
    cat_surface = pygame.Surface((800, 900))
    cat_surface.fill(PURPLE)
    cat_surface.set_colorkey(PURPLE)

    # Хвост кота
    surf_tail = pygame.Surface((160, 65))
    surf_tail.fill(pink)
    surf_tail.set_colorkey(pink)
    ellipse(surf_tail, main_colour, (0, 0, 160, 65))
    ellipse(surf_tail, 'BLACK', (0, 0, 160, 65), 1)
    # tail_rect = surf_tail.get_rect(center=(80, 32.5))
    rot_surf_tail = pygame.transform.rotate(surf_tail, 45)
    rot_tail_rect = rot_surf_tail.get_rect(center=(715, 555))
    cat_surface.blit(rot_surf_tail, rot_tail_rect)

    # Кот крупные детали
    ellipse(cat_surface, main_colour, (350, 500, 350, 150))  # тело
    ellipse(cat_surface, 'BLACK', (350, 500, 350, 150), 1)  # обводка тела

    ellipse(cat_surface, main_colour, (300, 525, 40, 65))  # самая маленькая лапка
    ellipse(cat_surface, 'BLACK', (300, 525, 40, 65), 1)  # самая маленькая лапка

    poligon1_points = [(250, 425), (310, 440), (280, 485)]  # точки левого уха
    polygon(cat_surface, main_colour, poligon1_points)  # левое ухо
    polygon(cat_surface, 'BLACK', poligon1_points, 1)

    poligonm1_points = [(265, 440), (300, 445), (285, 470)]  # точки левого уха маленького
    polygon(cat_surface, pink, poligonm1_points)  # левое маленькое ухо

    poligon2_points = [(450, 425), (390, 440), (420, 485)]  # точки правого уха
    polygon(cat_surface, main_colour, poligon2_points)  # правое ухо
    polygon(cat_surface, 'BLACK', poligon2_points, 1)

    poligonm2_points = [(432, 440), (400, 445), (415, 470)]  # точки маленького правого уха
    polygon(cat_surface, pink, poligonm2_points)  # правое маленькое ухо

    circle(cat_surface, main_colour, (350, 500), 75)  # голова
    circle(cat_surface, 'BLACK', (350, 500), 75, 1)  # обводка головы

    circle(cat_surface, main_colour, (700, 625), 50)  # бедро
    circle(cat_surface, 'BLACK', (700, 625), 50, 1)  # обводка бедра

    ellipse(cat_surface, main_colour, (300, 600, 100, 50))  # передняя лапка
    ellipse(cat_surface, 'BLACK', (300, 600, 100, 50), 1)  # обводка

    ellipse(cat_surface, main_colour, (725, 640, 30, 75))  # маленькая задняя лапка
    ellipse(cat_surface, 'BLACK', (725, 640, 30, 75), 1)  # обводка

    # Глаза
    circle(cat_surface, eyes_colour, (315, 500), 20)  # левый глаз
    circle(cat_surface, eyes_colour, (385, 500), 20)  # правый глаз
    ellipse(cat_surface, 'BLACK', (305, 480, 20, 40))  # левый эллепс
    ellipse(cat_surface, 'BLACK', (375, 480, 20, 40))

    # левый глаз
    surf_eye_1 = pygame.Surface((7, 25))
    surf_eye_1.fill('BLACK')
    surf_eye_1.set_colorkey('BLACK')
    ellipse(surf_eye_1, 'WHITE', (0, 0, 7, 25))
    # eye_1_rect = surf_eye_1.get_rect(center=(3.5, 12.5))
    rot_surf_eye_1 = pygame.transform.rotate(surf_eye_1, 45)
    rot_eye_1_rect = rot_surf_eye_1.get_rect(center=(310, 490))

    # правый глаз
    surf_eye_2 = pygame.Surface((7, 25))
    surf_eye_2.fill('BLACK')
    surf_eye_2.set_colorkey('BLACK')
    ellipse(surf_eye_2, 'WHITE', (0, 0, 7, 25))
    # eye_2_rect = surf_eye_2.get_rect(center=(3.5, 12.5))
    rot_surf_eye_2 = pygame.transform.rotate(surf_eye_2, 45)
    rot_eye_2_rect = rot_surf_eye_2.get_rect(center=(380, 490))
    cat_surface.blit(rot_surf_eye_1, rot_eye_1_rect)
    cat_surface.blit(rot_surf_eye_2, rot_eye_2_rect)

    # Нос и рот
    poligon_nose_points = [(335, 520), (365, 520), (350, 535)]
    polygon(cat_surface, pink, poligon_nose_points)
    polygon(cat_surface, 'BLACK', poligon_nose_points, 1)  # нос
    aaline(cat_surface, 'BLACK', [350, 535], [350, 550], 3)
    arc(cat_surface, 'BLACK', (350, 550, 15, 5), 3.14, 0, 5)
    arc(cat_surface, 'BLACK', (335, 550, 15, 5), 3.14, 0, 5)

    # УСЫ
    surf_1 = pygame.Surface((35, 15))
    surf_1.fill(pink)
    surf_1.set_colorkey(pink)
    arc(surf_1, 'BLACK', (0, 0, 35, 15), 0, math.pi)
    surf_1_rect = surf_eye_1.get_rect(center=(358, 550))

    surf_2 = pygame.transform.rotate(surf_1, 345)
    surf_2_rect = surf_2.get_rect(center=(370, 555))

    surf_3 = pygame.transform.rotate(surf_1, 353)
    surf_3_rect = surf_3.get_rect(center=(370, 550.5))

    surf_4_rect = surf_eye_1.get_rect(center=(313, 550))

    surf_5 = pygame.transform.rotate(surf_1, 7)
    surf_5_rect = surf_5.get_rect(center=(327, 550.5))

    surf_6 = pygame.transform.rotate(surf_1, 15)
    surf_6_rect = surf_6.get_rect(center=(330, 555))

    cat_surface.blit(surf_1, surf_1_rect)
    cat_surface.blit(surf_2, surf_2_rect)
    cat_surface.blit(surf_3, surf_3_rect)
    cat_surface.blit(surf_1, surf_4_rect)
    cat_surface.blit(surf_5, surf_5_rect)
    cat_surface.blit(surf_6, surf_6_rect)

    # Изменение размера и поворот
    new_cat_surface = pygame.transform.scale(cat_surface, (cat_surface.get_width() // scale, cat_surface.get_height() // scale))
    new_cat_surface_rect = new_cat_surface.get_rect(center=(center_x, center_y))
    if flip: new_cat_surface = pygame.transform.flip(new_cat_surface, True, False)

    screen.blit(new_cat_surface, new_cat_surface_rect)

def clew(screen, center_x, center_y, scale = 1, angle = 0):
    """
    рисует клубок
    screen - экран, на который переноситься поверхность клубка
    clew_surface - поверхность клубка
    рисует клубок
    (center_x, center_y) - координаты нетра клубка
    scale - масштаб изображение относительно исходного
    flip = False - исходное изображение, flip = True - отраженное
    """
    # Поверзность для клубка
    PINK = (248, 203, 172)
    clew_surface = pygame.Surface((800, 900))
    clew_surface.fill(PINK)
    clew_surface.set_colorkey(PINK)
    
    # Клубок
    circle(clew_surface, (153, 153, 153), (175, 700), 50)
    circle(clew_surface, 'BLACK', (175, 700), 50, 1)
    # Полосочки на клубке
    arc(clew_surface, 'BLACK', (70, 720, 75, 30), math.pi, 2 * math.pi)
    arc(clew_surface, 'BLACK', (10, 720, 60, 30), 0, math.pi)
    arc(clew_surface, 'BLACK', (150, 690, 40, 40), math.pi, 3 * math.pi / 2, 1)
    arc(clew_surface, 'BLACK', (145, 670, 60, 60), 0, math.pi / 2, 1)
    arc(clew_surface, 'BLACK', (140, 680, 60, 60), math.pi, 5 * math.pi / 3, 1)

    new_clew_surface = pygame.transform.scale(clew_surface, (round(clew_surface.get_width() * scale), round(clew_surface.get_height() * scale)))
    new_clew_surface_rect = new_clew_surface.get_rect(center=(center_x, center_y))
    if angle !=0:
        new_clew_surface = pygame.transform.rotate(new_clew_surface, angle)
        new_clew_surface_rect = new_clew_surface.get_rect(center = (center_x - angle, center_y+angle))
    screen.blit(new_clew_surface, new_clew_surface_rect)
    
    
def window_straight(screen, x_start = 200, x_finish = 400, y = 50, clock = pygame.time.Clock()):
    '''
    Двигает окно по прямой
    screen - поверхность, на которой будет двигаться окно
    x_start - координата по оси х начала движения
    x_finish - координата по оси х конца движения 
    y - координата фигуры по оси у
    '''
    BG1 = (123, 103, 30)
    BG2 = (82, 69, 17) 
    for i in range (x_start, x_finish):
        x = i
        background(screen, False, True, True)
        window(screen, x, y)
        pygame.display.update()
        clock.tick(50)
def cat_straight(screen, y_start = 400, y_finish = 600, x = 550, clock = pygame.time.Clock()):
    '''
    Двигает кота по прямой
    screen - поверхность, на которой будет двигаться кот
    x_start - координата по оси х начала движения
    x_finish - координата по оси х конца движения 
    x - координата фигуры по оси x
    '''
    BG1 = (123, 103, 30)
    BG2 = (82, 69, 17) 
    for i in range (y_start,y_finish):
        y = i
        background(screen, True, False, True)
        cat(screen, x, y, 2)
        pygame.display.update()
        clock.tick(50)
def clew_straight(screen, x_start = 200, x_finish = 400, y = 380, clock = pygame.time.Clock()):
    '''
    Двигает клубок по прямой
    screen - поверхность, на которой будет двигаться клубок
    x_start - координата по оси х начала движения
    x_finish - координата по оси х конца движения 
    y - координата фигуры по оси у
    '''
    BG1 = (123, 103, 30)
    BG2 = (82, 69, 17) 
    for i in range (x_start,x_finish):
        x = i
        background(screen, True, True, False)
        clew(screen, x, y, 1, True)
        pygame.display.update()
        clock.tick(50)
def cat_scale(screen, cat_x = 400, cat_y = 580, clock = pygame.time.Clock()):
    '''
    Делает анимированное масштабирование кота
    screen - поверхность, на которой будет происходить анимация
    cat_x - координата точки центра кота по оси x 
    cat_y - координата точки центра кота по оси y 
    '''
    BG1 = (123, 103, 30)
    BG2 = (82, 69, 17) 
    for i in range (100,1,-1):
        background(screen, True, False, True)
        cat(screen, cat_x, cat_y, scale = i)
        pygame.display.update()
        clock.tick(1000)
        
def rot_center(surface, rect, angle):
    '''
    Осуществляет повторот изображения вокруг заданной точки
    Принимает:
    sufrace - поверхность изображения
    rect - место, где находится поверхность на экране
    angle - угол поворота 
    Возвращает:
    rot_surface - поверхность повёрнутая на angle
    rot_rect - положение rot_surface
    '''
    rot_surface = pygame.transform.rotate(surface, angle)
    rot_rect = rot_surface.get_rect(center=rect.center)
    return rot_surface,rot_rect
    

def window_rotation(screen, center_x = 600, center_y = 200, clock = pygame.time.Clock()):
    '''
    Вращает окно
    screen - поверхность, на которой происходит вращение окна
    center_x - координата центра вращения по оси x
    center_y - координата центра вращения по оси y
    '''
    #Поверхность для поворота окна
    PURPLE = (255, 0, 255)
    window_surface = pygame.Surface((300, 350))
    window_surface.fill(PURPLE)
    window_surface.set_colorkey(PURPLE)
    window(window_surface, 0, 0, 1)
    for i in range(361):
        angle = i
        background(screen, False, True, True)
        rect = window_surface.get_rect(center=(center_x, center_y)) 
        surf, r = rot_center(window_surface, rect, angle)
        screen.blit(surf, r)
        pygame.display.update()
        clock.tick(1000)

main()
