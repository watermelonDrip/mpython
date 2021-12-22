import time
from pynput.keyboard import Key
from pynput import keyboard

import pyautogui
print(pyautogui.size())
time.sleep(1)
# makes program execution pause for 10 sec``
pyautogui.moveTo(500, 500, duration = 1)
st = True



# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         st =  False
#         return False

# class MyException(Exception): pass
#
# def on_press(key):
#     if key == keyboard.Key.esc:
#         st = False



# Collect events until released
# with keyboard.Listener(
#         on_press=on_press) as listener:
#     try:
#
#
#         while st:
#             pyautogui.moveRel(100, 0, duration=1)
#
#             pyautogui.moveRel(0, -100, duration=1)
#
#             pyautogui.moveRel(-100, 0, duration=1)
#
#             pyautogui.moveRel(0, 100, duration=1)
#
#     except MyException as e:
#         print('{0} was pressed'.format(e.args[0]))



# with keyboard.Listener(
#             on_release=on_release) as listener:
#         listener.join()
#
#     # ...or, in a non-blocking fashion:
#     listener = keyboard.Listener(
#         on_release=on_release)
#     listener.start()
#
try:
    while True:
        pyautogui.moveRel(100, 0, duration = 1)

        pyautogui.moveRel(0, -100, duration = 1)

        pyautogui.moveRel(-100, 0, duration = 1)


        pyautogui.moveRel(0, 100, duration = 1)

except KeyboardInterrupt:
    print ('\n')

#


