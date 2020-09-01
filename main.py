import pyautogui
import time


def skip():
    try:
        skip_img = pyautogui.locateCenterOnScreen('skip.png', confidence=.8)
        time.sleep(.25)
        if skip_img:
            pyautogui.moveTo(skip_img)
            pyautogui.click()
            print('Netflix Series Intro Skipped! Enjoy the show!')

    except OSError:
        print('OSError Excepted')
        time.sleep(.25)


while True:
    skip()

