import numpy as np
import sys
import os
import colorama
from colorama import Fore, Back, Style
from playsound import playsound
import time

from numpy.lib.function_base import select

class Design:
    ''' contains the design of brick structure'''
    def __init__(self, x_val_type1, y_val_type1, x_val_type2, y_val_type2, x_val_type3, y_val_type3, x_val_type4, y_val_type4, length, breadth):
        self.x_val_type1 = x_val_type1
        self.y_val_type1 = y_val_type1
        self.x_val_type2 = x_val_type2
        self.y_val_type2 = y_val_type2
        self.x_val_type3 = x_val_type3
        self.y_val_type3 = y_val_type3
        self.x_val_type4 = x_val_type4
        self.y_val_type4 = y_val_type4
        self.length = length
        self.breadth = breadth
        self.powers = np.zeros((breadth, length),dtype=object)
        self.powers1 = np.zeros((breadth, length),dtype=object)
        self.powers2 = np.zeros((breadth, length),dtype=object)
        self.powers3 = np.zeros((breadth, length),dtype=object)
        self.draw_fg = np.zeros((breadth, length),dtype=object)
        self.flags = np.zeros((breadth, length),dtype=object)
        self.flags2 = np.zeros((breadth, length),dtype=object)
        self.flags1 = np.zeros((breadth, length),dtype=object)
        self.flags3 = np.zeros((breadth, length),dtype=object)
        self.color = np.zeros((breadth, length),dtype=object)
        self.color1 = np.zeros((breadth, length),dtype=object)
        self.color2 = np.zeros((breadth, length),dtype=object)
        for i in range(x_val_type1 + 7, x_val_type1 + 8):
            k = y_val_type1 + 20
            self.flags1[i][k] = 1
            self.color1[i][k] = 1
            k = k+10
            for j in range(3):
                self.flags1[i][k] = 1
                self.color1[i][k] = 1
                k = k + 5
            k = k+5
            self.flags1[i][k] = 1
            self.color1[i][k] = 1

        for i in range(x_val_type1 + 9, x_val_type1 + 10):
            k = y_val_type1 + 20
            self.flags2[i][k] = 1
            self.color2[i][k] = 1
            k = k+10
            for j in range(3):
                self.flags2[i][k] = 1
                self.color2[i][k] = 1
                k = k + 5
            k = k+5
            self.flags2[i][k] = 1
            self.color2[i][k] = 1

        for i in range(x_val_type1 ,x_val_type1 + 7):
            k = y_val_type1
            for j in range(8):
                k = y_val_type1 + 10*j
                self.flags2[i][k] = 1

        for i in range(x_val_type2 ,x_val_type2 + 3):
            k = y_val_type2
            for j in range(7):
                k = y_val_type2 + 10*j
                if (j != 3):
                    self.flags2[i][k] = 2
                else:
                    self.flags2[i - 3][k] = 2

        for i in range(x_val_type3 ,x_val_type3 + 1):
            k = y_val_type3
            for j in range(6):
                k = y_val_type3 + 10*j
                self.flags2[i][k] = 3

        for i in range(x_val_type4 ,x_val_type4 + 1):
            k = y_val_type4
            for j in range(6):
                k = y_val_type4 + 10*j
                self.flags2[i][k] = 4

        for i in range(x_val_type2 ,x_val_type2 + 6):
            k = y_val_type2 + 30
            self.flags2[i][k] = 5

        l = []
        r = []
        for i in range(x_val_type1, x_val_type1+ 7):
            k = y_val_type1
            for j in range(3):
                self.flags1[i][k] = 1
                k = k+5
            self.flags1[i][k] = 2
            k = k+ 5
            self.flags1[i][k] = 1
            l.append(k)
            for j in range(5):
                k =k+5
                l.append(k)
                r.append(k)
            k=k+5
            l.append(k)
            self.flags1[i][k] = 1
            k=k+5
            self.flags1[i][k] = 2
            k = k+5
            for j in range(3):
                self.flags1[i][k] = 1
                k = k+5

        for i in l:
            self.flags1[x_val_type2][i] = 5
        for i in range(x_val_type2+1, x_val_type2+4):
            for j in r:
                self.flags1[i][j] = 3

        for i in range(x_val_type2 +3, x_val_type2 + 7):
            k = y_val_type1
            for j in range(3):
                self.flags3[i][k] = 1
                k = k + 5
            k = k + 45
            for j in range(3):
                self.flags3[i][k] = 1
                k = k + 5

        for i in range(x_val_type2 +1, x_val_type2 + 7):
            k = y_val_type1 + 15
            for j in range(2):
                self.flags3[i][k] = 2
                k = k + 5
            k = k + 25
            for j in range(2):
                self.flags3[i][k] = 2
                k = k + 5
        
        for i in range(x_val_type2 - 1, x_val_type2 + 7):
            k = y_val_type1 + 25
            for j in range(2):
                self.flags3[i][k] = 3
                k = k + 5
            k = k + 5
            for j in range(2):
                self.flags3[i][k] = 3
                k = k + 5
        self.flags3[x_val_type2 + 4][y_val_type1 + 35] = 4
        self.flags3[x_val_type2 + 4][0] = 4
        self.flags3[x_val_type2 + 4][y_val_type1 + 75] = 4

        self.draw_fg = self.flags1
        self.powers2[x_val_type1][y_val_type1] = 6
        self.powers2[x_val_type1 + 6][y_val_type1 + 70] = 6
        self.powers2[x_val_type1 + 6][y_val_type1] = 2
        self.powers2[x_val_type1][y_val_type1 + 70] = 2
        self.powers2[x_val_type2 + 1][y_val_type2] = 3
        self.powers2[x_val_type2 + 1][y_val_type2 + 60] = 4
        self.powers2[x_val_type2][y_val_type2 + 10] = 5
        self.powers2[x_val_type2][y_val_type2 + 50] = 5
        self.powers2[x_val_type2 + 2][y_val_type2 + 10] = 1
        self.powers2[x_val_type2 + 2][y_val_type2 + 50] = 1
        
        self.powers1[x_val_type1+ 6][y_val_type1 ] = 7
        self.powers1[x_val_type1+ 6][y_val_type1 + 15] = 7
        self.powers1[x_val_type1+ 6][y_val_type1 +55] = 8
        self.powers1[x_val_type1+ 6][y_val_type1 + 70] = 8

        self.powers = self.powers1
        self.color = self.color1


    def change_fg(self ,x ,y ,value):
        self.flags[int(x)][int(y)] = value

    def change_flg(self ,x ,y ,value):
        self.draw_fg[int(x)][int(y)] = value

    def check_status(self, x, y):
        b = (y//5)*5
        return self.flags[int(x)][int(b)]

    def change_lvl(self, level):
        if(level == 2):
            self.draw_fg = self.flags2
            self.flags = np.zeros((self.breadth, self.length),dtype=object)
            self.powers = self.powers2
            self.color = self.color2
        elif(level == 3):
            self.draw_fg = self.flags3
            self.flags = np.zeros((self.breadth, self.length),dtype=object)
            self.powers = self.powers3
            self.color = np.zeros((self.breadth, self.length),dtype=object)
        
    def change_col(self, main):
        for i in range(self.breadth):
            for j in range(self.length):
                if (self.color[i][j] == 1):
                    self.draw_fg[i][j] = self.draw_fg[i][j]%4 + 1

    def change_brick(self, x, y, main):
        b = int((y//5)*5)
        z = x
        x = int(z)
        if (self.flags[x][b] != 4 and self.flags[x][b] != 0 and b < 81 and x >= 0 and self.flags[x][b] != 5):
            self.flags[x][b] = self.flags[x][b] - 1
            self.draw_fg[x][b] = self.draw_fg[x][b] - 1
            playsound('bricks_breaking .mp3')
            if (self.color[x][b] == 1):
                self.color[x][b] = 0
            if (self.flags[x][b] == 0):
                for i in range(5):
                    main['grid'].change_xy(x, b + i, Back.BLACK + Fore.BLACK + " ")
                if (self.powers[x][b] == 1):
                    main['expand'].draw(x, b, main, 1)
                elif (self.powers[x][b] == 2):
                    main['shrink'].draw(x, b, main, 2)
                elif (self.powers[x][b] == 4):
                    main['fastball'].draw(x, b, main, 4)
                elif (self.powers[x][b] == 5):
                    main['thruball'].draw(x, b, main, 5)
                elif (self.powers[x][b] == 6):
                    main['paddlegrab'].draw(x, b, main, 6)
                elif (self.powers[x][b] == 7):
                    main['paddleshoot'].draw(x, b, main, 7)
                elif (self.powers[x][b] == 8):
                    main['fireball'].draw(x, b, main, 8)   
        elif (self.flags[x][b] == 5):
            playsound('explosive_brick.mp3')
            for i in range(self.breadth):
                for j in range(self.length):
                    if (self.flags[i][j] == 5):
                        if (self.flags[i-1][j] != 0 and self.flags[i-1][j] != 5):
                            main['ball'].score = 10*self.flags[i-1][j] + main['ball'].score
                            self.flags[i-1][j] = 0
                            self.draw_fg[i-1][j] = 0
                            for l in range(5):
                                main['grid'].change_xy(i-1, l + j, Back.BLACK + Fore.BLACK + " ")
                        if (self.flags[i+1][j] != 0 and self.flags[i+1][j] != 5):
                            main['ball'].score = 10*self.flags[i+1][j] + main['ball'].score
                            self.flags[i+1][j] = 0
                            self.draw_fg[i+1][j] = 0
                            for l in range(5):
                                main['grid'].change_xy(i+1, l + j, Back.BLACK + Fore.BLACK + " ")
                        if (self.flags[i][j+5] != 0 and self.flags[i][j+5] != 5):
                            main['ball'].score = 10*self.flags[i][j+5] + main['ball'].score
                            self.flags[i][j+5] = 0
                            self.draw_fg[i][j+5] = 0
                            for l in range(5):
                                main['grid'].change_xy(i, l + j + 5, Back.BLACK + Fore.BLACK + " ")
                        if (self.flags[i][j-5] != 0 and self.flags[i][j-5] != 5):
                            main['ball'].score = 10*self.flags[i][j-5] + main['ball'].score
                            self.flags[i][j-5] = 0
                            self.draw_fg[i][j-5] = 0
                            for l in range(5):
                                main['grid'].change_xy(i, l + j - 5, Back.BLACK + Fore.BLACK + " ")
                        main['ball'].score = 10 + main['ball'].score
                        self.flags[i][j] = 0
                        self.draw_fg[i][j] = 0
                        for l in range(5):
                            main['grid'].change_xy(i, j + l, Back.BLACK + Fore.BLACK + " ") 
        elif (self.flags[x][b] == 4):
            playsound('wall_collision.mp3')
            if (self.color[x][b] == 1):
                self.color[x][b] = 0                

    def change_brick1(self, x, y, main ,c):
        b = int((y//5)*5)
        z = x
        x = int(z)
        if (self.flags[x][b] != 0 and b < 81 and x >= 0 and self.flags[x][b] != 5):
            main['ball'].score = 10*self.flags[x][b] + main['ball'].score
            self.flags[x][b] = 0
            self.draw_fg[x][b] = 0
            if c==0:
                playsound('bricks_breaking .mp3')
            if (self.color[x][b] == 1):
                self.color[x][b] = 0
            if (self.flags[x][b] == 0):
                for i in range(5):
                    main['grid'].change_xy(x, b + i, Back.BLACK + Fore.BLACK + " ")
                if (self.powers[x][b] == 1):
                    main['expand'].draw(x, b, main, 1)
                elif (self.powers[x][b] == 2):
                    main['shrink'].draw(x, b, main, 2)
                elif (self.powers[x][b] == 4):
                    main['fastball'].draw(x, b, main, 4)
                elif (self.powers[x][b] == 5):
                    main['thruball'].draw(x, b, main, 5)
                elif (self.powers[x][b] == 6):
                    main['paddlegrab'].draw(x, b, main, 6)
                elif (self.powers[x][b] == 7):
                    main['paddleshoot'].draw(x, b, main, 7)
                elif (self.powers[x][b] == 8):
                    main['fireball'].draw(x, b, main, 8)
        elif (self.flags[x][b] == 5):
            playsound('explosive_brick.mp3')
            for i in range(self.breadth):
                for j in range(self.length):
                    if (self.flags[i][j] == 5):
                        if (self.flags[i-1][j] != 0 and self.flags[i-1][j] != 5):
                            main['ball'].score = 10*self.flags[i-1][j] + main['ball'].score
                            self.flags[i-1][j] = 0
                            self.draw_fg[i-1][j] = 0
                            for l in range(5):
                                main['grid'].change_xy(i-1, l + j, Back.BLACK + Fore.BLACK + " ")
                        if (self.flags[i+1][j] != 0 and self.flags[i+1][j] != 5):
                            main['ball'].score = 10*self.flags[i+1][j] + main['ball'].score
                            self.flags[i+1][j] = 0
                            self.draw_fg[i+1][j] = 0
                            for l in range(5):
                                main['grid'].change_xy(i+1, l + j, Back.BLACK + Fore.BLACK + " ")
                        if (self.flags[i][j+5] != 0 and self.flags[i][j+5] != 5):
                            main['ball'].score = 10*self.flags[i][j+5] + main['ball'].score
                            self.flags[i][j+5] = 0
                            self.draw_fg[i][j+5] = 0
                            for l in range(5):
                                main['grid'].change_xy(i, l + j + 5, Back.BLACK + Fore.BLACK + " ")
                        if (self.flags[i][j-5] != 0 and self.flags[i][j-5] != 5):
                            main['ball'].score = 10*self.flags[i][j-5] + main['ball'].score
                            self.flags[i][j-5] = 0
                            self.draw_fg[i][j-5] = 0
                            for l in range(5):
                                main['grid'].change_xy(i, l + j - 5, Back.BLACK + Fore.BLACK + " ")
                        main['ball'].score = 10 + main['ball'].score
                        self.flags[i][j] = 0
                        self.draw_fg[i][j] = 0
                        for l in range(5):
                                main['grid'].change_xy(i, j + l, Back.BLACK + Fore.BLACK + " ")
        elif (self.flags[x][b] == 4):
            if c==0:
                playsound('wall_collision.mp3')
            if (self.color[x][b] == 1):
                self.color[x][b] = 0   
    
    def change_brick2(self, x, y, main):
        b = int((y//5)*5)
        z = x
        x = int(z)
        playsound('explosive_brick.mp3')
        main['design'].change_brick1(x,b,main ,1)
        main['design'].change_brick1(x+1,b,main,1)
        main['design'].change_brick1(x-1,b,main,1)
        main['design'].change_brick1(x,b+5,main,1)
        main['design'].change_brick1(x,b-5,main,1)
        main['design'].change_brick1(x+1,b+5,main,1)
        main['design'].change_brick1(x+1,b-5,main,1)
        main['design'].change_brick1(x-1,b+5,main,1)
        main['design'].change_brick1(x-1,b-5,main,1)

    def draw(self,main):
        for i in range(self.breadth):
            for j in range(self.length-1):
                if (self.draw_fg[i][j] == 1):
                    main['bric'].create_brick_type_1(i, j, main)
                elif (self.draw_fg[i][j] == 2):
                    main['bric'].create_brick_type_2(i, j, main)
                elif (self.draw_fg[i][j] == 3):
                    main['bric'].create_brick_type_3(i, j, main)
                elif (self.draw_fg[i][j] == 4):
                    main['bric'].create_brick_type_4(i, j, main) 
                elif (self.draw_fg[i][j] == 5):
                    main['bric'].create_brick_type_5(i, j, main)
        
        for i in range(self.length):
            main['grid'].change_xy(self.breadth - 1 ,i ,Back.BLACK + Fore.WHITE + " ")
    
    def fall_brick(self, main):
        d = 0
        for i in range(self.breadth - 1 , 3,-1):
            for j in range(self.length):
                self.draw_fg[i][j] = self.draw_fg[i-1][j]
                self.powers[i][j] = self.powers[i-1][j]
                self.color[i][j] = self.color[i-1][j]
                if (i == self.breadth-2):
                    if (self.draw_fg[i][j] != 0):
                        d=d+1
        for j in range(self.length):
            self.draw_fg[3][j] = 0
            self.powers[3][j] = 0
            self.color[3][j] = 0
        if (d > 0):
            main['ball'].live = 0
            playsound('crying.mp3')
        for i in range(main['design'].breadth):
                for j in range(main['design'].length):
                    main['grid'].change_xy(i, j, Back.BLACK + Fore.BLACK + " ")
        self.flags = np.zeros((self.breadth, self.length),dtype=object)
