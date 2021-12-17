# 키값을 받아서 처리
# 후킹
# pip install keyboard < 설치

import keyboard
from PIL import ImageGrab
import time

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("F9", screenshot)   # 사용자가  F9 키를 누르면 스크린 샷 저장
# keyboard.add_hotkey("a", screenshot)
# keyboard.add_hotkey("ctrl+shift+s", screenshot)

keyboard.wait("esc")    # 사용자가 esc 를 누를 때 까지 프로그램 수행