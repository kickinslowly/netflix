import pyautogui
import time


def skip():
    try:
        skip_img = pyautogui.locateCenterOnScreen('skip.png', confidence=.8)
        next_img = pyautogui.locateCenterOnScreen('next.png', confidence=.8)
        next_img_hulu = pyautogui.locateCenterOnScreen('next_hulu.png', confidence=.8)
        skip_img_hbo = pyautogui.locateCenterOnScreen('skip_hbo.png', confidence=.8)
        skip_img_hbo_intro = pyautogui.locateCenterOnScreen('skip_intro_hbo.png', confidence=.8)
        next_img_hbo = pyautogui.locateCenterOnScreen('next_hbo.png', confidence=.8)
        full_img_hbo = pyautogui.locateCenterOnScreen('fullscreen_hbo.png', confidence=.8)
        time.sleep(.25)
        if full_img_hbo:
            pyautogui.moveTo(full_img_hbo)
            pyautogui.click()
            print('Back to fullscreen!')
        if skip_img:
            pyautogui.moveTo(skip_img)
            pyautogui.click()
            print('Netflix Series Intro Skipped! Enjoy the show!')
        elif next_img:
            pyautogui.moveTo(next_img)
            pyautogui.click()
            print('Onward to the next Netflix episode!')
        elif next_img_hulu:
            pyautogui.moveTo(next_img_hulu)
            pyautogui.click()
            print('Onward to the next Hulu episode!')
        elif skip_img_hbo:
            pyautogui.moveTo(skip_img_hbo)
            pyautogui.click()
            print('Skipping HBO ads!')
        elif skip_img_hbo_intro:
            pyautogui.moveTo(skip_img_hbo_intro)
            pyautogui.click()
            print('Skipping HBO Series Intro!')
        elif next_img_hbo:
            pyautogui.moveTo(next_img_hbo)
            pyautogui.click()
            print('Onward to the next HBO episode!')
            time.sleep(1)
        if full_img_hbo:
            pyautogui.moveTo(full_img_hbo)
            pyautogui.click()
            print('Back to fullscreen!')
    except OSError:
        print('OSError Excepted')
        time.sleep(.25)


while True:
    skip()

