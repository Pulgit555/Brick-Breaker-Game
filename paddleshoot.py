import numpy as np
import sys
import os
import colorama
from colorama import Fore, Back, Style
import time
from playsound import playsound
from powerups import Powerups

class Paddleshoot(Powerups):
    ''' defines the paddleshoot power ups for ball'''
    def __init__(self, pad, length, breadth):
        self.original_len = pad.len
        self.x = np.zeros((breadth, length),dtype=object)
        self.y = np.zeros((breadth, length),dtype=object)
        self.x_cord = 0
        self.y_cord = 0
        self.length = length
        self.breadth = breadth
        self.status = np.zeros((breadth, length),dtype=object)
        for i in range(breadth):
            for j in range(length):
                self.status[i][j] = 2
        self.x_speed = np.zeros((breadth, length),dtype=object)
        self.y_speed = np.zeros((breadth, length),dtype=object)
        self.init_time = int(round(time.time()))
        self.x_bullet = np.zeros(100,dtype=object)
        self.y_bullet = np.zeros(100,dtype=object)
        self.status_bullet = np.zeros(100,dtype=object)
        self.r = 0 
        self.stime = 0
        self.b = 0
        self.alreadyOn = 0
        Powerups.__init__(self, Back.BLACK + Fore.WHITE + "-", Back.BLACK + Fore.WHITE + ">")

    def initials(self ,main):
        for i in range(self.breadth):
            for j in range(self.length):
                if (main['design'].powers[i][j] == 7):
                    self.x[i][j] = i
                    self.y[i][j] = j

    def change_val(self, x, y, a, main, i, j):
        self.x[i][j] = x
        self.y[i][j] = y
        if (self.status[i][j] == 1 and a == 0):
            self.stime = int(round(time.time()))
            if (self.alreadyOn == 0):
                self.alreadyOn = self.alreadyOn + 1
            main['ball'].paddleshoot = 1  
            self.x_cord = main['pad'].x_value - 1
            self.y_cord = main['pad'].y_value  
            self.b = 0
        self.status[i][j] = a
        self.x_speed[i][j] = main['ball'].last_xspeed
        self.y_speed[i][j] = main['ball'].last_yspeed

    def move_right(self,main):
        if(self.y_cord + main['pad'].len < self.length):
            main['grid'].change_xy(self.x_cord ,self.y_cord ,Back.BLACK + Fore.GREEN + " ")
            main['grid'].change_xy(self.x_cord ,self.y_cord + main['pad'].len - 1,Back.BLACK + Fore.GREEN + " ")
            self.y_cord = self.y_cord + 1

    def move_left(self,main):
        if(self.y_cord > 0):
            main['grid'].change_xy(self.x_cord ,self.y_cord ,Back.BLACK + Fore.GREEN + " ")
            main['grid'].change_xy(self.x_cord ,self.y_cord + main['pad'].len - 1,Back.BLACK + Fore.GREEN + " ")
            self.y_cord = self.y_cord - 1           
    
    def draw_gun(self, main):
        main['grid'].change_xy(self.x_cord ,self.y_cord ,Back.BLACK + Fore.GREEN + "A")
        main['grid'].change_xy(self.x_cord ,self.y_cord + main['pad'].len - 1,Back.BLACK + Fore.GREEN + "A")
    
    def drawing(self, main):
        for i in range(self.breadth):
            for j in range(self.length):
                if (self.status[i][j] == 1):
                    main['grid'].change_xy(self.x[i][j] ,self.y[i][j] ,Back.BLACK + Fore.WHITE + "-")
                    main['grid'].change_xy(self.x[i][j] ,self.y[i][j] + 1 ,Back.BLACK + Fore.WHITE + ">")

    def mov(self ,main):
        for i in range(self.breadth):
            for j in range(self.length):
                if (self.status[i][j] == 1):
                    main['grid'].change_xy(self.x[i][j] ,self.y[i][j] ,Back.BLACK + Fore.WHITE + " ")
                    main['grid'].change_xy(self.x[i][j] ,self.y[i][j] + 1 ,Back.BLACK + Fore.WHITE + " ")
                    if (self.x[i][j] + self.x_speed[i][j] >= main['ball'].max_u ):
                        self.x[i][j] = main['ball'].max_u-1
                    else:
                        self.x[i][j] = self.x[i][j] + self.x_speed[i][j]
                    self.y[i][j] = self.y[i][j] + self.y_speed[i][j]
                    if (self.y[i][j] + self.y_speed[i][j] <=0 or self.y[i][j] + self.y_speed[i][j] >=85):
                        self.y_speed[i][j] = (-1)*self.y_speed[i][j]
                    main['paddleshoot'].drawing(main)
                    if (self.x[i][j] >= main['ball'].max_u - 2):
                        val = main['pad'].y_value
                        l = main['pad'].len - 1
                        diff = int(self.y[i][j]) - val
                        if (val <= int(self.y[i][j]) and diff <= l):
                            main['paddleshoot'].change_val(self.x[i][j] ,self.y[i][j] ,0 ,main, i, j)
                        elif (val <= int(self.y[i][j] + 1) and int(self.y[i][j] + 1) - val <= l):
                            main['paddleshoot'].change_val(self.x[i][j] ,self.y[i][j] ,0, main, i, j)
                        else:
                            main['grid'].change_xy(i ,j ,Back.BLACK + Fore.WHITE + " ")
                            main['grid'].change_xy(i ,j + 1 ,Back.BLACK + Fore.WHITE + " ")
                            main['paddleshoot'].change_val(self.x[i][j] ,self.y[i][j] ,2, main, i, j)
                    self.x_speed[i][j] = self.x_speed[i][j] + 0.1
    
    def shoot(self, main):
        if(int(round(time.time())) - self.init_time > 5):
            playsound('bullets.mp3')
            self.x_bullet[self.r] = self.x_cord - 1
            self.y_bullet[self.r] = self.y_cord
            main['grid'].change_xy(self.x_bullet[self.r], self.y_bullet[self.r], Back.BLUE + Fore.BLACK + "^")
            self.status_bullet[self.r] = 1
            self.r = self.r + 1
            self.x_bullet[self.r] = self.x_cord - 1
            self.y_bullet[self.r] = self.y_cord + main['pad'].len - 1
            main['grid'].change_xy(self.x_bullet[self.r], self.y_bullet[self.r], Back.BLUE + Fore.BLACK + "^")
            self.status_bullet[self.r] = 1
            self.r = self.r + 1
            self.init_time = int(round(time.time()))

    def mov_bullet(self, main):
        for i in range(self.r):
            if (self.status_bullet[i] == 1):
                main['grid'].change_xy(self.x_bullet[i], self.y_bullet[i], Back.BLACK + Fore.BLACK + " ")
                self.x_bullet[i] = self.x_bullet[i] - 1
                main['grid'].change_xy(self.x_bullet[i], self.y_bullet[i], Back.BLUE + Fore.BLACK + "^")
                a = main['design'].check_status(int(self.x_bullet[i]), int(self.y_bullet[i]))
                if (a != 0):
                    main['design'].change_brick(int(self.x_bullet[i]), int(self.y_bullet[i]), main)
                    self.status_bullet[i] = 0
                if (self.x_bullet[i] == 0):
                    main['grid'].change_xy(self.x_bullet[i], self.y_bullet[i], Back.BLACK + Fore.BLACK + " ")
                    self.status_bullet[i] = 0