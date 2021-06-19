import numpy as np
import sys
import os
import colorama
from colorama import Fore, Back, Style
import time
from powerups import Powerups

class Expand(Powerups):
    ''' defines the expand power ups for ball'''
    def __init__(self, pad, length, breadth):
        self.original_len = pad.len
        self.x = np.zeros((breadth, length),dtype=object)
        self.y = np.zeros((breadth, length),dtype=object)
        self.length = length
        self.breadth = breadth
        self.status = np.zeros((breadth, length),dtype=object)
        for i in range(breadth):
            for j in range(length):
                self.status[i][j] = 2
        self.x_speed = -1
        self.stime = 0
        self.b = 0
        self.alreadyOn = 0
        Powerups.__init__(self, Back.BLACK + Fore.WHITE + "<", Back.BLACK + Fore.WHITE + ">")

    def initials(self ,main):
        for i in range(self.breadth):
            for j in range(self.length):
                if (main['design'].powers[i][j] == 1):
                    self.x[i][j] = i
                    self.y[i][j] = j

    def change_val(self, x, y, a, main, i, j):
        self.x[i][j] = x
        self.y[i][j] = y
        if (self.status[i][j] == 1 and a == 0):
            self.stime = int(round(time.time()))
            if (self.alreadyOn == 0):
                main['pad'].len = main['pad'].len + 2
                self.alreadyOn = self.alreadyOn + 1
            self.b = 0
        self.status[i][j] = a

    def mov(self ,main):
        for i in range(self.breadth):
            for j in range(self.length):
                if (self.status[i][j] == 1):
                    main['grid'].change_xy(self.x[i][j] ,self.y[i][j] ,Back.BLACK + Fore.WHITE + " ")
                    main['grid'].change_xy(self.x[i][j] ,self.y[i][j] + 1 ,Back.BLACK + Fore.WHITE + " ")
                    self.x[i][j] = self.x[i][j] + 1
                    main['grid'].change_xy(self.x[i][j] ,self.y[i][j] ,Back.BLACK + Fore.WHITE + "<")
                    main['grid'].change_xy(self.x[i][j] ,self.y[i][j] + 1 ,Back.BLACK + Fore.WHITE + ">")
                    if (self.x[i][j] == main['ball'].max_u - 2):
                        val = main['pad'].y_value
                        l = main['pad'].len - 1
                        diff = int(self.y[i][j]) - val
                        if (val <= int(self.y[i][j]) and diff <= l):
                            main['expand'].change_val(self.x[i][j] ,self.y[i][j] ,0 ,main, i, j)
                        elif (val <= int(self.y[i][j] + 1) and int(self.y[i][j] + 1) - val <= l):
                            main['expand'].change_val(self.x[i][j] ,self.y[i][j] ,0, main, i, j)
                    elif (self.x[i][j] > main['ball'].max_u - 2):
                        main['grid'].change_xy(i ,j ,Back.BLACK + Fore.WHITE + " ")
                        main['grid'].change_xy(i ,j + 1 ,Back.BLACK + Fore.WHITE + " ")
                        main['expand'].change_val(self.x[i][j] ,self.y[i][j] ,2, main, i, j)

    def draw(self ,x ,y ,main ,val):
        main['grid'].change_xy(x ,y ,Back.BLACK + Fore.WHITE + "<")
        main['grid'].change_xy(x ,y + 1 ,Back.BLACK + Fore.WHITE + ">")
        main['expand'].change_val(x ,y ,1 ,main, x, y)