import numpy as np
import sys
import os
import colorama
from colorama import Fore, Back, Style
import time

class Paddle:
    ''' contains the design of paddle '''
    def __init__(self, x_value, y_value, len, max_r):
        self.x_value = x_value
        self.y_value = y_value
        self.len = len
        self.max_l = 0
        self.max_r = max_r

    def move_right(self, main):
        if (self.y_value < self.max_r - self.len):
            main['grid'].change_xy(self.x_value, self.y_value, Back.BLACK + Fore.BLACK + " ")
            self.y_value = self.y_value + 1
            if (main['ball'].check_flg() == 0):
                main['ball'].move_right(1, main, main['ball'].x, main['ball'].x_speed, 1)
    
    def move_left(self, main):
        if (self.y_value >= 1):
            main['grid'].change_xy(self.x_value, self.y_value + self.len - 1, Back.BLACK + Fore.BLACK + " ")
            self.y_value = self.y_value - 1
            if (main['ball'].check_flg() == 0):
                main['ball'].move_left(1, main, main['ball'].x, main['ball'].x_speed, 1)

    def draw(self, main):
        for i in range(self.y_value):
            main['grid'].change_xy(self.x_value, i, Back.BLACK + Fore.BLACK + " ")
        main['grid'].change_xy(self.x_value, self.y_value, Fore.RED + Back.WHITE + '{')
        for i in range(1, self.len):
            main['grid'].change_xy(self.x_value, self.y_value + i, Fore.RED + Back.WHITE + '_')
        main['grid'].change_xy(self.x_value, self.y_value + self.len - 1, Fore.RED + Back.WHITE + '}')
        for i in range(self.y_value + self.len ,self.max_r):
            main['grid'].change_xy(self.x_value, i, Back.BLACK + Fore.BLACK + " ")