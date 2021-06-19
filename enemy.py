import numpy as np
import sys
import os
import colorama
from colorama import Fore, Back, Style
from playsound import playsound
import time

class Enemy:
    ''' defines the shrink power ups for ball'''
    def __init__(self, x_value, y_value, max_r, max_u):
        self.x_value = x_value
        self.y_value = y_value
        self.max_r = max_r
        self.health = 5
        self.init_time = int(round(time.time()))
        self.x = np.zeros(100,dtype=object)
        self.y = np.zeros(100,dtype=object)
        self.status = np.zeros(100,dtype=object)
        self.r = 0 
    
    def mov_right(self, main):
        if (self.y_value + 5< self.max_r - main['pad'].len//4):
            self.y_value = self.y_value + 1
    
    def mov_left(self, main):
        if (self.y_value > main['pad'].len//4):
            self.y_value = self.y_value - 1
    
    def dec_health(self,main):
        self.health = self.health - 1
        main['ball'].score = main['ball'].score + 20
        if (self.health == 3 or self.health == 1):
            k =0
            for i in range(self.max_r//5):
                main['design'].draw_fg[2][k] = 1
                k = k+5
        elif (self.health == 0):
            main['ball'].score = main['ball'].score + 100
            main['grid'].change_xy(self.x_value, self.y_value, Fore.BLACK + Back.BLACK + ' ')
            main['grid'].change_xy(self.x_value, self.y_value + 1, Fore.BLACK + Back.BLACK + ' ')
            main['grid'].change_xy(self.x_value, self.y_value + 2, Fore.BLACK+ Back.BLACK + ' ')
            main['grid'].change_xy(self.x_value, self.y_value + 3, Fore.BLACK + Back.BLACK + ' ')
            main['grid'].change_xy(self.x_value, self.y_value + 4, Fore.BLACK + Back.BLACK + " ")

            main['grid'].change_xy(self.x_value + 1, self.y_value, Fore.BLACK + Back.BLACK + ' ')
            main['grid'].change_xy(self.x_value + 1, self.y_value + 1, Fore.BLACK + Back.BLACK + ' ')
            main['grid'].change_xy(self.x_value + 1, self.y_value + 2, Fore.BLACK + Back.BLACK + ' ')
            main['grid'].change_xy(self.x_value + 1, self.y_value + 3, Fore.BLACK + Back.BLACK + ' ')
            main['grid'].change_xy(self.x_value +1 , self.y_value + 4, Fore.BLACK+ Back.BLACK + " ")
    
    def drop_bomb(self, main):
        if(int(round(time.time())) - self.init_time > 5):
            playsound('alien.mp3')
            self.x[self.r] = self.x_value + 2
            self.y[self.r] = self.y_value + 2
            main['grid'].change_xy(self.x[self.r], self.y[self.r], Back.RED + Fore.BLACK + "&")
            self.status[self.r] = 1
            self.r = self.r + 1
            self.init_time = int(round(time.time()))
    
    def move(self, main):
        for i in range(self.r):
            if (self.status[i] == 1):
                main['grid'].change_xy(self.x[i], self.y[i], Back.BLACK + Fore.BLACK + " ")
                self.x[i] = self.x[i] + 1
                main['grid'].change_xy(self.x[i], self.y[i], Back.RED + Fore.BLACK + "&")
                if (self.x[i] == main['ball'].max_u - 2):
                    val = main['pad'].y_value
                    l = main['pad'].len - 1
                    diff = int(self.y[i]) - val
                    if (val <= int(self.y[i]) and diff <= l):
                        playsound('crying.mp3')
                        main['ball'].live = main['ball'].live - 1
                    self.status[i] = 0

    def draw(self, main):
        main['grid'].change_xy(self.x_value, self.y_value -1, Back.BLACK + Fore.BLACK + " ")
        main['grid'].change_xy(self.x_value + 1,self.y_value -1, Back.BLACK + Fore.BLACK + " ")
        main['grid'].change_xy(self.x_value, self.y_value, Fore.YELLOW + Back.BLACK + '/')
        main['grid'].change_xy(self.x_value, self.y_value + 1, Fore.YELLOW + Back.BLACK + '-')
        main['grid'].change_xy(self.x_value, self.y_value + 2, Fore.YELLOW + Back.BLACK + '_')
        main['grid'].change_xy(self.x_value, self.y_value + 3, Fore.YELLOW + Back.BLACK + '-')
        main['grid'].change_xy(self.x_value, self.y_value + 4, Fore.YELLOW + Back.BLACK + "\\")

        main['grid'].change_xy(self.x_value + 1, self.y_value, Fore.YELLOW + Back.BLACK + '\\')
        main['grid'].change_xy(self.x_value + 1, self.y_value + 1, Fore.YELLOW + Back.BLACK + '<')
        main['grid'].change_xy(self.x_value + 1, self.y_value + 2, Fore.YELLOW + Back.BLACK + ' ')
        main['grid'].change_xy(self.x_value + 1, self.y_value + 3, Fore.YELLOW + Back.BLACK + '>')
        main['grid'].change_xy(self.x_value +1 , self.y_value + 4, Fore.YELLOW + Back.BLACK + "/")
        main['grid'].change_xy(self.x_value, self.y_value + 5, Back.BLACK + Fore.BLACK + " ")
        main['grid'].change_xy(self.x_value + 1, self.y_value + 5, Back.BLACK + Fore.BLACK + " ")

    
# /-_-\
# \< >/