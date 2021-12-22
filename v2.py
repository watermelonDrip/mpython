import time
from pynput.keyboard import Key
from pynput import keyboard

import pyautogui,sys
print('Press Ctrl-C to quit.')

print(pyautogui.size())
time.sleep(1)
# makes program execution pause for 10 sec``
pyautogui.moveTo(500, 500, duration = 1)
st = True

try:
    while st:
        pyautogui.moveRel(100, 0, duration = 1)

        pyautogui.moveRel(0, -100, duration = 1)

        pyautogui.moveRel(-100, 0, duration = 1)


        pyautogui.moveRel(0, 100, duration = 1)

except KeyboardInterrupt:
    print ('SB')
else:
    print('SB')
#

if __name__=='__main__':
    d = parse_command(sys.argv)
    k = d.get('p',None)

    if d.get('p',None) is not None:
        WorkBitch(d['w'])

    elif d.get('r',None) is not None:
        RestDummy(d['r'])
