f = open("w.txt","w")

#f.close()
#f = open("w.txt","r")
#print(f.read())

from pynput.mouse import Controller
mouse = Controller()
print('Current pointer is {0}'.format(mouse.position))



from pynput import mouse

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))
    f.write('Pointer moved to {0}\n'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    f.write('{0} at {1}\n'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    print('')
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
    f.write('Scrolled {0} at {1}\n'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()

f.close()
