from input import input_to , Get
from screen import Screen
from paddle import Paddle
from brick import Brick
from design import Design
from ball import Ball
from expand import Expand
from shrink import Shrink
from fastball import Fastball
from paddlegrab import Paddlegrab
from thruball import Thruball
from fireball import Fireball
from paddleshoot import Paddleshoot
from enemy import Enemy
import sys
import termios
import tty
import signal
import os
import time
import colorama
from playsound import playsound

if __name__ == "__main__":
    colorama.init(autoreset=True)
    os.system('clear')
    length = 85
    breadth = 35
    grid = Screen(length, breadth) 
    pad = Paddle(33, 38, 9, length)
    enemy = Enemy(0, 40, length, breadth) 
    design = Design(3, 5, 6, 10, 11, 15, 10, 15, length, breadth)
    bric = Brick(5)
    ball = Ball(32, 42, length, breadth)
    grav = int(round(time.time()))
    start_time = int(round(time.time()))
    expand = Expand(pad ,length ,breadth)
    shrink = Shrink(pad ,length ,breadth)
    fastball = Fastball(pad ,length ,breadth)
    paddlegrab = Paddlegrab(pad ,length ,breadth)
    thruball = Thruball(pad ,length ,breadth)
    fireball = Fireball(pad ,length ,breadth)
    paddleshoot = Paddleshoot(pad, length , breadth)
    main = {'grid' : grid ,'pad' : pad, 'bric' : bric, 'design' : design, 'ball' : ball, 
        'start_time' : start_time, 'expand' : expand, 'shrink' : shrink, 'fastball' : fastball,
        'paddlegrab' : paddlegrab, 'thruball' : thruball , 'enemy' : enemy , 'fireball' : fireball,
        'paddleshoot' : paddleshoot}

    pad.draw(main)
    ball.draw(main)
    design.draw(main)
    grid.print(main)
    expand.initials(main)
    shrink.initials(main)
    fastball.initials(main)
    paddlegrab.initials(main)
    thruball.initials(main)
    fireball.initials(main)
    paddleshoot.initials(main)
    # to get character asynchronoulsy
    getch = Get() 
    while(True):

        if int(round(time.time())) - start_time > 1000:
            main['grid'].print_end(main)
            break

        ch = input_to(getch)
        
        if ch == 'l':
            ball.update_lvl(main)
        elif ch == 'd':
            pad.move_right(main)
            enemy.mov_right(main)
            if (main['ball'].paddleshoot == 1):
                paddleshoot.move_right(main)
        elif ch == 'a':
            pad.move_left(main)
            enemy.mov_left(main)
            if (main['ball'].paddleshoot == 1):
                paddleshoot.move_left(main)
        elif ch == 's':
            ball.change_flg(1)
        elif ch == 'q':
            break
        if (ball.live == 0):
            main['grid'].print_end(main)
            break
        if (main['ball'].level != 3):
            main['design'].change_col(main)

        ball.movement(main)
        if (main['ball'].paddleshoot == 1):
            paddleshoot.draw_gun(main)
            paddleshoot.shoot(main)
        pad.draw(main)
        ball.draw(main)
        design.draw(main)
        main['fireball'].drawing(main)
        main['paddleshoot'].drawing(main)
        if (main['ball'].level == 3 and main['enemy'].health > 0):
            enemy.draw(main)
            enemy.drop_bomb(main)
        paddleshoot.mov_bullet(main)
        enemy.move(main)
        grid.print(main)
        # break