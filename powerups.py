import numpy as np
import sys
import os
import colorama
from colorama import Fore, Back, Style
import time

class Powerups:
   ''' defines the power ups for ball'''
   def __init__(self ,ptype1 ,ptype2):
        self.time_limit = 40
        self.ptype1 = ptype1
        self.ptype2 = ptype2

   def draw(self ,x ,y ,main ,val):
      main['grid'].change_xy(x ,y ,self.ptype1)
      main['grid'].change_xy(x ,y + 1 ,self.ptype2)
      if (val == 1):
         main['expand'].change_val(x ,y ,1 ,main, x, y)
      elif (val == 2):
         main['shrink'].change_val(x ,y ,1 ,main, x, y) 
      elif (val == 4):
         main['fastball'].change_val(x ,y ,1 ,main, x, y)
      elif (val == 5):
         main['thruball'].change_val(x ,y ,1 ,main, x, y)  
      elif (val == 6):
         main['paddlegrab'].change_val(x ,y ,1 ,main, x, y)
      elif (val == 7):
         main['paddleshoot'].change_val(x ,y ,1 ,main, x, y)
      elif (val == 8):
         main['fireball'].change_val(x ,y ,1 ,main, x, y)
          