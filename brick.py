import numpy as np
import sys
import os
import colorama
from colorama import Fore, Back, Style
import time

class Brick:
    ''' contains the design of different bricks'''
    def __init__(self, len):
        self.len = len

    def create_brick_type_1(self, x, y ,main):
        main['grid'].change_xy(x, y, Fore.RED + Back.GREEN + "<")
        main['design'].change_fg(x, y, 1)
        main['design'].change_flg(x, y, 1)
        for i in range(1,self.len):
            main['grid'].change_xy(x, y + i, Fore.RED + Back.GREEN + "-")
            main['design'].change_fg(x, y + i, 1)
        main['grid'].change_xy(x, y + self.len - 1, Fore.RED + Back.GREEN + ">")
        main['design'].change_fg(x, y + self.len -1, 1)
    
    def create_brick_type_2(self, x, y ,main):
        main['grid'].change_xy(x, y, Fore.RED + Back.YELLOW + "<")
        main['design'].change_fg(x, y, 2)
        main['design'].change_flg(x, y, 2)
        for i in range(1,self.len):
            main['grid'].change_xy(x, y + i, Fore.RED + Back.YELLOW + "-")
            main['design'].change_fg(x, y + i, 2)
        main['grid'].change_xy(x, y + self.len - 1, Fore.RED + Back.YELLOW + ">")
        main['design'].change_fg(x, y + self.len -1, 2)

    def create_brick_type_3(self, x, y ,main):
        main['grid'].change_xy(x, y, Fore.RED + Back.BLUE + "<")
        main['design'].change_fg(x, y, 3)
        main['design'].change_flg(x, y, 3)
        for i in range(1,self.len):
            main['grid'].change_xy(x, y + i, Fore.RED + Back.BLUE + "-")
            main['design'].change_fg(x, y + i, 3)
        main['grid'].change_xy(x, y + self.len - 1, Fore.RED + Back.BLUE + ">")
        main['design'].change_fg(x, y + self.len -1, 3)
    
    def create_brick_type_4(self, x, y ,main):
        main['grid'].change_xy(x, y, Fore.WHITE + Back.MAGENTA + "<")
        main['design'].change_fg(x, y, 4)
        main['design'].change_flg(x, y, 4)
        for i in range(1,self.len):
            main['grid'].change_xy(x, y + i, Fore.WHITE + Back.MAGENTA + "-")
            main['design'].change_fg(x, y + i, 4)
        main['grid'].change_xy(x, y + self.len - 1, Fore.WHITE + Back.MAGENTA + ">")
        main['design'].change_fg(x, y + self.len -1, 4)

    def create_brick_type_5(self, x, y ,main):
        main['grid'].change_xy(x, y, Back.RED + Fore.CYAN + "<")
        main['design'].change_fg(x, y, 5)
        main['design'].change_flg(x, y, 5)
        for i in range(1,self.len):
            main['grid'].change_xy(x, y + i, Back.RED + Fore.CYAN + "-")
            main['design'].change_fg(x, y + i, 5)
        main['grid'].change_xy(x, y + self.len - 1, Back.RED + Fore.CYAN + ">")
        main['design'].change_fg(x, y + self.len -1, 5)