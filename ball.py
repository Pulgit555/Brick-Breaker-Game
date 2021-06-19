import numpy as np
import sys
import os
import colorama
from colorama import Fore, Back, Style
from playsound import playsound
import time

class Ball:
    ''' contains the design of ball '''
    def __init__(self, x, y, max_r, max_u):
        self.x = x
        self.y = y
        self.x_speed = -1
        self.y_speed = 0
        self.last_xspeed = -1
        self.last_yspeed = 0
        self.max_r = max_r
        self.max_u = max_u
        self.attach = 0
        self.live = 10
        self.score = 0
        self.thruball = 0
        self.fireball = 0
        self.paddleshoot = 0
        self.level = 1
        self.init_time = int(round(time.time()))

    def change_flg(self, value):
        self.attach = value

    def check_flg(self):
        b = self.attach
        return b

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = -1
        self.y_speed = 0
        self.attach = 0

    def update_lvl(self, main):
        if self.level < 3:
            self.level += 1
            main['ball'].reset(main['pad'].x_value - 1, main['pad'].y_value + (main['pad'].len)//2)
            main['design'].change_lvl(self.level)
            for i in range(main['design'].breadth):
                for j in range(main['design'].length):
                    main['grid'].change_xy(i, j, Back.BLACK + Fore.BLACK + " ")
            if (main['expand'].b == 0 and main['expand'].alreadyOn == 1):
                if (main['pad'].len > 3):
                    main['pad'].len = main['pad'].len - 2
                    main['expand'].b = 1
                    main['expand'].alreadyOn = main['expand'].alreadyOn - 1
            if (main['shrink'].b == 0 and main['shrink'].alreadyOn == 1):
                main['pad'].len = main['pad'].len + 2
                main['shrink'].b = 1
                main['shrink'].alreadyOn = main['shrink'].alreadyOn - 1
            if (main['fastball'].b == 0 and main['fastball'].alreadyOn == 1):
                main['fastball'].b = 1
                main['fastball'].alreadyOn = main['fastball'].alreadyOn - 1
            if (main['paddlegrab'].b == 0 and main['paddlegrab'].alreadyOn == 1):
                main['paddlegrab'].b = 1
                main['paddlegrab'].alreadyOn = main['paddlegrab'].alreadyOn - 1
            if (main['thruball'].b == 0 and main['thruball'].alreadyOn == 1):
                main['thruball'].b = 1
                main['thruball'].alreadyOn = main['thruball'].alreadyOn - 1
                main['ball'].thruball = 0
            if (main['fireball'].b == 0 and main['fireball'].alreadyOn == 1):
                main['fireball'].b = 1
                main['fireball'].alreadyOn = main['fireball'].alreadyOn - 1
                main['ball'].fireball = 0
            if (main['paddleshoot'].b == 0 and main['paddleshoot'].alreadyOn == 1):
                main['paddleshoot'].b = 1
                main['paddleshoot'].alreadyOn = main['paddleshoot'].alreadyOn - 1
                main['ball'].paddleshoot = 0
        else:
            playsound('crying.mp3')
            self.live = 0

    def move_right(self, value, main, c, d, k):
        g = self.x_speed
        main['grid'].change_xy(self.x, self.y, Back.BLACK + Fore.BLACK + " ")
        if (self.y + value < self.max_r):
            self.y = self.y + value
        else:
            self.y = self.max_r - 1
            playsound('wall_collision.mp3')
            self.y_speed = (-1)*self.y_speed
        h = self.y
        if ( int(c + d) >=0 and int(c + d) < self.max_u - 1):
            a = main['design'].check_status(int(c + d), int(self.y))
            if (a != 0):
                if (main['thruball'].alreadyOn == 1):
                    main['design'].change_brick1(int(c + d), h, main, 0)
                else:
                    if (main['fireball'].alreadyOn == 1):
                        main['design'].change_brick2(int(c + d), h, main)
                    if (self.y%5 == 0):
                        b = main['design'].check_status(int(c + d), int(self.y - 1))
                        if (b != 0):
                            self.y_speed = (-1)*self.y_speed
                            # self.y = self.y + self.y_speed
                            self.x_speed = (-1)*self.x_speed
                        else :
                            self.y_speed = (-1)*self.y_speed
                            # self.y = self.y + self.y_speed
                            if(self.y_speed == 0):
                                self.x_speed = (-1)*self.x_speed
                    elif (self.y%5 == 4):
                        b = main['design'].check_status(int(c + d), int(self.y + 1))
                        if (b != 0):
                            self.y_speed = (-1)*self.y_speed
                            # self.y = self.y + self.y_speed
                            self.x_speed = (-1)*self.x_speed
                        else :
                            self.x_speed = (-1)*self.x_speed
                            if(self.x_speed == 0):
                                self.y_speed = (-1)*self.y_speed
                    else:
                        if (self.x > self.x + d):
                            b = main['design'].check_status(int(c + d + 1), int(self.y))
                            if b != 0 :
                                self.y_speed = (-1)*self.y_speed
                            else:
                                self.x_speed = (-1)*self.x_speed
                                if(self.x_speed == 0):
                                    self.y_speed = (-1)*self.y_speed
                        else:
                            b = main['design'].check_status(int(c + d - 1), self.y)
                            if b != 0 :
                                self.y_speed = (-1)*self.y_speed
                            else:
                                self.x_speed = (-1)*self.x_speed
                                if(self.x_speed == 0):
                                    self.y_speed = (-1)*self.y_speed     
                    if (a != 4 and a != 5):
                        self.score = self.score + 10
                    if (main['fireball'].alreadyOn == 0):
                        main['design'].change_brick(int(c + d), h, main)
        if ((c+d) == 1 and main['ball'].level == 3 and main['enemy'].health >0):
            if (self.y >= main['enemy'].y_value and self.y < main['enemy'].y_value +5):
                main['enemy'].dec_health(main)
                self.x_speed = (-1)*self.x_speed
                self.x = self.x + self.x_speed
                if (self.y == main['enemy'].y_value):
                    if (self.y_speed > 0):
                        self.y_speed = (-1)*self.y_speed
                if (self.y == main['enemy'].y_value +4):
                    if (self.y_speed < 0):
                        self.y_speed = (-1)*self.y_speed
        if ((c+d) == 0  and main['ball'].level == 3 and main['enemy'].health >0):
            if (self.y >= main['enemy'].y_value and self.y < main['enemy'].y_value +5):
                main['enemy'].dec_health(main)
                self.x_speed = (-1)*self.x_speed
                self.x = self.x + self.x_speed
                if (self.y == main['enemy'].y_value):
                    self.y_speed = (-1)*self.y_speed
                if (self.y == main['enemy'].y_value +4):
                    self.y_speed = (-1)*self.y_speed
        if (k==0):
            e = self.y
            f = self.y_speed
            if (d > 0):
                main['ball'].move_down(d, main, e, f)
            else:
                main['ball'].move_up((-1)*d, main)
            # if (self.x_speed > 0):
            #     main['ball'].move_down(self.x_speed, main, e, f)
            # else:
            #     main['ball'].move_up((-1)*self.x_speed, main)
        else:
            main['grid'].change_xy(self.x, self.y,Back.CYAN + Fore.RED + "O")
    
    def move_left(self, value, main, c, d, k):
        g = self.x_speed
        main['grid'].change_xy(self.x, self.y, Back.BLACK + Fore.BLACK + " ")
        if (self.y - value >= 0):
            self.y = self.y - value
        else:
            self.y = 0
            playsound('wall_collision.mp3')
            self.y_speed = (-1)*self.y_speed
        h = self.y
        if ( int(c + d) >=0 and int(c + d) < self.max_u - 1):
            a = main['design'].check_status(int(c + d), int(self.y))
            if (a != 0):
                if (main['thruball'].alreadyOn == 1):
                    main['design'].change_brick1(int(c + d), h, main, 0)
                else:
                    if (main['fireball'].alreadyOn == 1):
                        main['design'].change_brick2(int(c + d), h, main)
                    if ( self.y%5 == 4):
                        b = main['design'].check_status(int(c + d), int(self.y + 1))
                        if (b != 0):
                            self.y_speed = (-1)*self.y_speed
                            # self.y = self.y + self.y_speed
                            self.x_speed = (-1)*self.x_speed
                        else :
                            self.y_speed = (-1)*self.y_speed
                            # self.y = self.y + self.y_speed
                            if(self.y_speed == 0):
                                self.x_speed = (-1)*self.x_speed
                    elif (self.y%5 == 0):
                        b = main['design'].check_status(int(c + d), int(self.y - 1))
                        if (b != 0):
                            self.y_speed = (-1)*self.y_speed
                            # self.y = self.y + self.y_speed
                            self.x_speed = (-1)*self.x_speed
                        else :
                            self.x_speed = (-1)*self.x_speed
                            if(self.x_speed == 0):
                                self.y_speed = (-1)*self.y_speed
                    else:
                        if (self.x > self.x + d):
                            b = main['design'].check_status(int(c + d + 1), self.y)
                            if b != 0 :
                                self.y_speed = (-1)*self.y_speed
                            else:
                                self.x_speed = (-1)*self.x_speed
                                if(self.x_speed == 0):
                                    self.y_speed = (-1)*self.y_speed
                        else:
                            b = main['design'].check_status(int(c + d - 1), self.y)
                            if b != 0 :
                                self.y_speed = (-1)*self.y_speed
                            else:
                                self.x_speed = (-1)*self.x_speed
                                if(self.x_speed == 0):
                                    self.y_speed = (-1)*self.y_speed 
                    if (a != 4 and a != 5):
                        self.score = self.score + 10
                    if (main['fireball'].alreadyOn == 0):
                        main['design'].change_brick( int(c + d), h, main)
        if ((c+d) == 1  and main['ball'].level == 3 and main['enemy'].health >0):
            if (self.y >= main['enemy'].y_value and self.y < main['enemy'].y_value +5):
                main['enemy'].dec_health(main)
                self.x_speed = (-1)*self.x_speed
                self.x = self.x + self.x_speed
                if (self.y == main['enemy'].y_value):
                    if (self.y_speed > 0):
                        self.y_speed = (-1)*self.y_speed
                if (self.y == main['enemy'].y_value +4):
                    if (self.y_speed < 0):
                        self.y_speed = (-1)*self.y_speed
        if ((c+d) == 0  and main['ball'].level == 3 and main['enemy'].health >0):
            if (self.y >= main['enemy'].y_value and self.y < main['enemy'].y_value +5):
                main['enemy'].dec_health(main)
                self.x_speed = (-1)*self.x_speed
                self.x = self.x + self.x_speed
                if (self.y == main['enemy'].y_value):
                    self.y_speed = (-1)*self.y_speed
                if (self.y == main['enemy'].y_value +4):
                    self.y_speed = (-1)*self.y_speed
        if (k==0):
            e = self.y
            f = self.y_speed
            if (d > 0):
                main['ball'].move_down(d, main, e, f)
            else:
                main['ball'].move_up((-1)*d, main)
            # if (self.x_speed > 0):
            #     main['ball'].move_down(self.x_speed, main, e, f)
            # else:
            #     main['ball'].move_up((-1)*self.x_speed, main)
        else:
            main['grid'].change_xy(self.x, self.y,Back.CYAN + Fore.RED + "O")

    def move_up(self, value, main):
        main['grid'].change_xy(self.x, self.y, Back.BLACK + Fore.BLACK + " ")
        if (self.x - value >= 0):
            self.x = self.x - value
        else:
            self.x = 0
            playsound('wall_collision.mp3')
            self.x_speed = (-1)*self.x_speed
        main['grid'].change_xy(self.x, self.y,Back.CYAN + Fore.RED + "O")
        main['fastball'].mov(main)

    def move_down(self, value, main, e, f):
        main['grid'].change_xy(self.x, self.y, Back.BLACK + Fore.BLACK + " ")
        if (self.x + value < self.max_u - 1 and self.x + value >= self.max_u -2):
            val = main['pad'].y_value
            l = main['pad'].len - 1
            diff = int(e + f) - val
            self.x = self.x + value
            if (val <= int(e + f) and diff <= l):
                if (diff < l//2):
                    self.y_speed = self.y_speed - (l//2 - diff)/4
                    playsound('wall_collision.mp3')
                elif (diff > l//2):
                    self.y_speed = self.y_speed + (diff - l//2)/4
                    playsound('wall_collision.mp3')
                self.x_speed = (-1)*self.x_speed
                if (main['paddlegrab'].alreadyOn == 1):
                    self.attach = 0
                self.x = self.x + self.x_speed
                self.y = self.y + self.y_speed
                if (int(round(time.time())) - self.init_time > 5):
                    main['design'].fall_brick(main)
                    self.init_time = int(round(time.time()))
        elif (self.x + value < self.max_u - 1):
            self.x = self.x + value
            main['grid'].change_xy(self.x, self.y,Back.CYAN + Fore.RED + "O")
        else:
            playsound('crying.mp3')
            self.live = self.live - 1
            main['grid'].change_xy(main['pad'].x_value - 1, main['pad'].y_value + (main['pad'].len)//2, Back.CYAN + Fore.RED + "O")
            if (main['expand'].alreadyOn == 1):
                if (main['pad'].len > 3):
                    main['pad'].len = main['pad'].len - 2
                    main['expand'].b = 1
                    main['expand'].alreadyOn = main['expand'].alreadyOn - 1
            if (main['shrink'].alreadyOn == 1):
                main['pad'].len = main['pad'].len + 2
                main['shrink'].b = 1
                main['shrink'].alreadyOn = main['shrink'].alreadyOn - 1
            if (main['fastball'].alreadyOn == 1):
                # main['ball'].x_speed = main['ball'].x_speed + main['fastball'].x_speed
                main['ball'].y_speed = main['ball'].y_speed + main['fastball'].y_speed 
                main['fastball'].b = 1
                main['fastball'].alreadyOn = main['fastball'].alreadyOn - 1
            if (main['paddlegrab'].alreadyOn == 1):
                main['paddlegrab'].b = 1
                main['paddlegrab'].alreadyOn = main['paddlegrab'].alreadyOn - 1
            if (main['thruball'].alreadyOn == 1):
                main['thruball'].b = 1
                main['thruball'].alreadyOn = main['thruball'].alreadyOn - 1
                main['ball'].thruball = 0
            if (main['fireball'].alreadyOn == 1):
                main['fireball'].b = 1
                main['fireball'].alreadyOn = main['fireball'].alreadyOn - 1
                main['ball'].fireball = 0
            if (main['paddleshoot'].alreadyOn == 1):
                main['paddleshoot'].b = 1
                main['paddleshoot'].alreadyOn = main['paddleshoot'].alreadyOn - 1
                main['ball'].paddleshoot = 0
            main['ball'].reset(main['pad'].x_value - 1, main['pad'].y_value + (main['pad'].len)//2)
        main['fastball'].mov(main)

    def movement(self, main):
        time.sleep(0.1)
        self.last_xspeed = self.x_speed
        self.last_yspeed = self.y_speed
        if ((int(round(time.time())) - main['expand'].stime) == main['expand'].time_limit and main['expand'].b == 0):
            if (main['pad'].len > 3):
                main['pad'].len = main['pad'].len - 2
                main['expand'].b = 1
                main['expand'].alreadyOn = main['expand'].alreadyOn - 1
        if ((int(round(time.time())) - main['shrink'].stime) == main['shrink'].time_limit and main['shrink'].b == 0):
            main['pad'].len = main['pad'].len + 2
            main['shrink'].b = 1
            main['shrink'].alreadyOn = main['shrink'].alreadyOn - 1
        if ((int(round(time.time())) - main['fastball'].stime) == main['fastball'].time_limit and main['fastball'].b == 0):
            main['ball'].x_speed = main['ball'].x_speed + main['fastball'].x_speed
            main['ball'].y_speed = main['ball'].y_speed + main['fastball'].y_speed 
            main['fastball'].b = 1
            main['fastball'].alreadyOn = main['fastball'].alreadyOn - 1
        if ((int(round(time.time())) - main['paddlegrab'].stime) == main['paddlegrab'].time_limit and main['paddlegrab'].b == 0):
            main['paddlegrab'].b = 1
            main['paddlegrab'].alreadyOn = main['paddlegrab'].alreadyOn - 1
        if ((int(round(time.time())) - main['thruball'].stime) == main['thruball'].time_limit and main['thruball'].b == 0):
            main['thruball'].b = 1
            main['thruball'].alreadyOn = main['thruball'].alreadyOn - 1
            main['ball'].thruball = 0
        if ((int(round(time.time())) - main['fireball'].stime) == main['fireball'].time_limit and main['fireball'].b == 0):
            main['fireball'].b = 1
            main['fireball'].alreadyOn = main['fireball'].alreadyOn - 1
            main['ball'].fireball = 0
        if ((int(round(time.time())) - main['paddleshoot'].stime) == main['paddleshoot'].time_limit and main['paddleshoot'].b == 0):
            main['paddleshoot'].b = 1
            main['paddleshoot'].alreadyOn = main['paddleshoot'].alreadyOn - 1
            main['ball'].paddleshoot = 0
        main['expand'].mov(main)
        main['shrink'].mov(main)
        main['paddlegrab'].mov(main)
        main['thruball'].mov(main)
        main['fireball'].mov(main)
        main['paddleshoot'].mov(main)
        if (main['ball'].check_flg() == 1):
            c = self.x
            d = self.x_speed
            if (self.y_speed > 0):
                main['ball'].move_right(self.y_speed, main, c, d, 0)
            else:
                main['ball'].move_left((-1)*self.y_speed, main, c, d, 0)
        else:
            main['fastball'].mov(main)
        

    def draw(self, main):
        if (self.y >= self.max_r):
            self.y = self.max_r - 1
        main['grid'].change_xy(self.x, self.y, Back.CYAN +Fore.RED + "O")