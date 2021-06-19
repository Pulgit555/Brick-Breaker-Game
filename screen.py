import numpy as np
import sys
import os
import colorama
from colorama import Fore, Back, Style
import time

class Screen:
    ''' contains the design of main screen '''
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.screen = np.zeros((self.breadth, self.length),dtype=object)
        self.screen[:] = Back.BLACK + Fore.BLACK + " "
        # self.create()

    def change_xy(self,x,y,ch):
        self.screen[int(x)][int(y)] = ch

    def print(self, main):
        print("\033[0;0f", end="")
        # self.screen[37][57] = Fore.RED + Back.GREEN + '}'
        print(Back.BLACK + Fore.WHITE + "Time: " + str(int(round(time.time())) - main['start_time']) + "  ", end="")
        print(Back.BLACK + Fore.WHITE + "Live: " + str(main['ball'].live) + "  ", end="")
        print(Back.BLACK + Fore.WHITE + "Score: " + str(main['ball'].score) + "  ", end="")
        print(Back.BLACK + Fore.WHITE + "Level: " + str(main['ball'].level) + "  ", end="")
        if (main['expand'].alreadyOn == 1):
            print(Back.BLACK + Fore.WHITE + "<>: " + str(int(round(time.time())) - main['expand'].stime) + "  ", end="")
        else:
            print(Back.BLACK + Fore.WHITE + "       ", end="")
        if (main['shrink'].alreadyOn == 1):
            print(Back.BLACK + Fore.WHITE + "><: " + str(int(round(time.time())) - main['shrink'].stime) + "  ", end="")
        else:
            print(Back.BLACK + Fore.WHITE + "       ", end="")
        if (main['thruball'].alreadyOn == 1):
            print(Back.BLACK + Fore.WHITE + "TH: " + str(int(round(time.time())) - main['thruball'].stime) + "  ", end="")
        else:
            print(Back.BLACK + Fore.WHITE + "       ", end="")
        if (main['paddlegrab'].alreadyOn == 1):
            print(Back.BLACK + Fore.WHITE + "PG: " + str(int(round(time.time())) - main['paddlegrab'].stime) + "  ", end="")
        else:
            print(Back.BLACK + Fore.WHITE + "       ", end="")
        if (main['fastball'].alreadyOn == 1):
            print(Back.BLACK + Fore.WHITE + ">>: " + str(int(round(time.time())) - main['fastball'].stime) + "  ", end="")
        else:
            print(Back.BLACK + Fore.WHITE + "       ", end="")
        if (main['paddleshoot'].alreadyOn == 1):
            print(Back.BLACK + Fore.WHITE + "**: " + str(int(round(time.time())) - main['paddleshoot'].stime) + "  ", end="")
        else:
            print(Back.BLACK + Fore.WHITE + "       ", end="")
        if (main['fireball'].alreadyOn == 1):
            print(Back.BLACK + Fore.WHITE + "**: " + str(int(round(time.time())) - main['fireball'].stime) + "  ", end="")
        else:
            print(Back.BLACK + Fore.WHITE + "       ", end="")
        if(main['ball'].level == 3):
            for i in range(main['enemy'].health):
                print(Back.BLACK + Fore.WHITE + "+", end="")
            for i in range(main['enemy'].health, main['enemy'].health+5):
                print(Back.BLACK + Fore.WHITE + " ", end="")
        st = Back.BLACK + Fore.BLACK + "\n"
        for i in range(self.breadth):
            for j in range(self.length):
                st += self.screen[i][j]
            st += Back.BLACK + Fore.BLACK + "\n"
        print(st)

    def print_end(self, main):
        os.system('clear')
        print("\n\n\n")
        print("\033[0;0f", end="")
        # self.screen[37][57] = Fore.RED + Back.GREEN + '}'
        print(Back.BLACK + Fore.WHITE + "Time: " + str(int(round(time.time())) - main['start_time']) + "  ", end="")
        print(Back.BLACK + Fore.WHITE + "Live: " + str(main['ball'].live) + "  ", end="")
        print(Back.BLACK + Fore.WHITE + "Score: " + str(main['ball'].score) + "  ", end="")
        print(Back.BLACK + Fore.WHITE + "Level: " + str(main['ball'].level) + "  ", end="")
        print("\n\n\n")
        print(Fore.GREEN + Back.BLACK + "  ________                         ________                     " + "\n",
		Fore.GREEN + Back.BLACK + " /  _____/_____    _____   ____    \_____  \___  __ ___________ " + "\n",
		Fore.GREEN + Back.BLACK + "/   \  ___\__  \  /     \_/ __ \    /   |   \  \/ // __ \_  __ \\" + "\n",
		Fore.GREEN + Back.BLACK + "\    \_\  \/ __ \|  Y Y  \  ___/   /    |    \   /\  ___/|  | \/" + "\n",
		Fore.GREEN + Back.BLACK + " \______  (____  /__|_|  /\___  >  \_______  /\_/  \___  >__|   " + "\n",
		Fore.GREEN + Back.BLACK + "        \/     \/      \/     \/           \/          \/       " + "\n")