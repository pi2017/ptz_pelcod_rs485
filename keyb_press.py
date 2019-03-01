from pynput.keyboard import Key, Listener


def on_press(key):
    print('{0} pressed'.format(
        key))
    if key == Key.left:
        print ("<-LEFT")
    elif key == Key.right:
        print ("RIGHT->")
    elif key == Key.up:
        print ("Up")
    elif key == Key.down:
        print ("Down")
    elif key == Key.space:
        print (">STOP<")


def on_release(key):
    print('{0} release'.format(
        key))

    if key == Key.esc:
        print ("EXIT")
        # Stop listener
        return False


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
