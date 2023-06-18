import keyboard
import pyautogui
import mouse
import logging
from time import sleep
from win32gui import FindWindow, GetWindowRect

LEAGUE_GAME_CLIENT_WINNAME = "League of Legends (TM) Client"
LEAGUE_CLIENT_WINNAME = "League of Legends"

GAME_JUNGLE_CAMP_GROMP = (0.8348, 0.8521)
GAME_JUNGLE_CAMP_BLUEBUFF = (0.8603, 0.8632)
GAME_JUNGLE_CAMP_MURKWOLF = (0.8543, 0.8827)
GAME_JUNGLE_CAMP_RAPTORS = (0.9124, 0.9126)
GAME_JUNGLE_CAMP_REDBUFF = (0.9012, 0.9207)
GAME_JUNGLE_CAMP_KRUGS = (0.9100, 0.9389)

def size(window_title=LEAGUE_CLIENT_WINNAME):
    window_handle = FindWindow(None, window_title)
    if window_handle == 0:
        pass
    window_rect = GetWindowRect(window_handle)
    return window_rect[0], window_rect[1], window_rect[2], window_rect[3]

def exists(window_title):
    if FindWindow(None, window_title) == 0:
        return False
    return True

def attack_move_click(ratio, wait=1):
    x, y, l, h = size(LEAGUE_GAME_CLIENT_WINNAME)
    updated_x = ((l - x) * ratio[0]) + x
    updated_y = ((h - y) * ratio[1]) + y
    pyautogui.moveTo(updated_x, updated_y)
    sleep(.5)
    #keyboard.press('a') this
    keyboard.press('shift')
    sleep(.2)
    #mouse.click() moves the
    mouse.click('right')
    sleep(.1)
    #keyboard.release('a') map >:(
    keyboard.release('shift')
    sleep(wait)

camp = GAME_JUNGLE_CAMP_KRUGS
middle = (0.5, 0.5)

sleep(5)

while True:
    attack_move_click(middle, 0.5)
    attack_move_click(camp)
    print(camp)
    if keyboard.is_pressed("x"):
        exit()
    #camp = (camp[0], camp[1] - 0.001)