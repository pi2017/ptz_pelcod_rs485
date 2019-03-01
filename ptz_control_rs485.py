"""
==============================
Antenna Tracker PTZ controller v1.0
Author: Oleksii Savchenko
Date: 01.2019
Update: 02.2019
==============================
Pelco-D protocol
LEFT  - FF 01 00 04 3F 00 44
RIGHT - FF 01 00 02 3F 00 42
UP    - FF 01 00 08 00 27 30
DOWN  - FF 01 00 10 00 27 38
STOP  - FF 01 00 00 00 00 01

"""
import Tkinter
from Tkinter import Tk, Canvas
from PIL import Image, ImageTk
from pynput.keyboard import Key
import sys
import time
import serial
import serial.rs485
import serial.tools.list_ports

# =======Change COMPORT =============================
ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid))

# ====================================================

# Input true comport ===========================
comport = raw_input("Input RS485 port : ")
baud = 19200
# ================================
# ================================
try:
    ser = serial.Serial(comport, baud)
    ser.rs485_mode = serial.rs485.RS485Settings(rts_level_for_tx=True, rts_level_for_rx=False, loopback=False,
                                                delay_before_tx=None, delay_before_rx=None)
    print("Port open: " + str(comport))

except serial.serialutil.SerialException:
    print ("RS-485 not connected..." '\n')
    print ("Please connect RS-485 module ")
    exit()


# =====================================================================
#
# =====================================================================

def up():
    up = bytearray.fromhex('FF 01 00 08 00 27 30')
    print ('UP')
    print ('FF 01 00 08 00 27 30')
    ser.write(up)
    return up


def down():
    down = bytearray.fromhex('FF 01 00 10 00 27 38')
    print ('DOWN')
    print ('FF 01 00 10 00 27 38')
    ser.write(down)
    return down


def right():
    right = bytearray.fromhex('FF 01 00 02 3F 00 42')
    print ('RIGHT')
    print ('FF 01 00 02 20 00 23')
    ser.write(right)
    return right


def left():
    left = bytearray.fromhex('FF 01 00 04 3F 00 44')
    print ('LEFT')
    print ('FF 01 00 04 3F 00 44')
    ser.write(left)
    return left


def stop():
    stop = bytearray.fromhex('FF 01 00 00 00 00 01')
    print ('STOP')
    print ('FF 01 00 00 00 00 01')
    ser.write(stop)
    return stop


def test():
    stop = bytearray.fromhex('FF 01 00 00 00 00 01')
    test = bytearray.fromhex('FF 01 00 0C 27 27 5B')
    print ('TEST')
    print ('FF 01 00 0C 27 27 5B')
    ser.write(test)
    time.sleep(8)
    print('STOP')
    print ('FF 01 00 00 00 00 01')
    ser.write(stop)
    return test


def close_window():
    root.destroy()


# ============================================
#
# MAIN WINDOW
# ============================================
# ============================================
# Keyboard key : Left, Right, Up, Down, Space
# ============================================
def leftKey(event):
    print("Left key pressed...")
    left_step = left()
    ser.write(left_step)
    time.sleep(0.5)
    lock = stop()
    ser.write(lock)


def rightKey(event):
    print("Right key pressed...")
    right_step = right()
    ser.write(right_step)
    time.sleep(0.5)
    lock = stop()
    ser.write(lock)


def upKey(event):
    print("Up key pressed...")
    up_step = up()
    ser.write(up_step)
    time.sleep(0.5)
    lock = stop()
    ser.write(lock)


def downKey(event):
    print("Up key pressed...")
    down_step = down()
    ser.write(down_step)
    time.sleep(0.5)
    lock = stop()
    ser.write(lock)


def spaceKey(event):
    stop_stop = stop()
    ser.write(stop_stop)


# ======= end keyboard =============

root = Tk()
root.title('AntennaTracker v1.0')
root.geometry('500x160')
root.configure(background='black')

root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)
root.bind('<space>', spaceKey)

# Create a canvas
canvas_wight = 110
canvas_height = 110
canvas = Canvas(root, width=canvas_wight, height=canvas_height, background='black')
canvas.place(x=185, y=10, width=110)

# Load the image file
logo = Image.open('./picture/ptz_logo.png')
# Put the image into a canvas compatible class, and stick in an
# arbitrary variable to the garbage collector doesn't destroy it
canvas.image = ImageTk.PhotoImage(logo)
# Add the image to the canvas, and set the anchor to the root left / north west corner
canvas.create_image(0, 0, image=canvas.image, anchor='nw')

# ===============================================================================================================
#
# BUTTONS
# ===============================================================================================================
# UP
button = Tkinter.Button(root, text="UP", fg="white", bg='black', command=up).place(x=65, y=35, width=55)
# DOWN
button = Tkinter.Button(root, text="DOWN", fg="white", bg='black', command=down).place(x=65, y=65, width=55)
# RIGHT
button = Tkinter.Button(root, text="RIGHT", fg="white", bg='black', command=right).place(x=125, y=100, width=55)
# LEFT
button = Tkinter.Button(root, text="LEFT", fg="white", bg='black', command=left).place(x=5, y=100, width=55)
# !!! STOP !!!
button = Tkinter.Button(root, text="STOP", fg="red", bg='black', command=stop).place(x=65, y=100, width=55)
# EXIT
button = Tkinter.Button(root, text="EXIT", fg="black", command=close_window)
button.place(x=420, y=10, width=55)

# TEST!!!
button = Tkinter.Button(root, text="TEST", fg="white", bg='black', width=15, command=test)
button.place(x=300, y=70, width=55)
# PRESET01!!!
button = Tkinter.Button(root, text="PRESET", fg="white", bg='grey', width=15, command=stop)
button.place(x=360, y=70, width=55)
# PRESET01!!!
button = Tkinter.Button(root, text="PRESET", fg="white", bg='gray', width=15, command=stop)
button.place(x=420, y=70, width=55)
# PRESET02!!!
button = Tkinter.Button(root, text="PRESET", fg="white", bg='gray', width=15, command=stop)
button.place(x=300, y=100, width=55)
# PRESET03!!!
button = Tkinter.Button(root, text="PRESET", fg="white", bg='gray', width=15, command=stop)
button.place(x=360, y=100, width=55)
# PRESET04!!!
button = Tkinter.Button(root, text="PRESET", fg="white", bg='gray', width=15, command=stop)
button.place(x=420, y=100, width=55)
# =========================================================
# End of programm
# =========================================================
root.mainloop()
ser.close()
