"""
==============================
Antenna Tracker PTZ controller v1.0
Author: Oleksii Savchenko
Date: 01.2019
Update:
==============================
Pelco-D protocol
LEFT  - FF 01 00 04 3F 00 44
RIGHT - FF 01 00 02 3F 00 42
UP    - FF 01 00 08 00 27 30
DOWN  - FF 01 00 10 00 27 38
STOP  - FF 01 00 00 00 00 01

"""
import tkinter
from tkinter import Tk, Canvas
from PIL import Image, ImageTk
from pynput.keyboard import Key
import sys
import time
import serial
import serial.rs485

# =======Change COMPORT =====
COMPORT = 'com13'
BAUD = 19200
# ==========================
# =============================================================================
try:
    ser = serial.Serial(COMPORT, BAUD)
    ser.rs485_mode = serial.rs485.RS485Settings(rts_level_for_tx=True, rts_level_for_rx=False, loopback=False,
                                                delay_before_tx=None, delay_before_rx=None)
    print("Port open: ", serial.Serial)

except serial.serialutil.SerialException:
    print ("RS-485 not connected...")
    exit()


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
root.geometry('300x150')
root.configure(background='black')
frame = tkinter.Frame(root)
frame = tkinter.Frame(root, width=100, height=100)
frame.config(background='black')
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)
root.bind('<space>', spaceKey)
frame.pack()

# Create a canvas
canvas = Canvas(root, width=300, height=100)
canvas.config(background='black')
canvas.pack()

# Load the image file
im = Image.open('./picture/uss_logo_01.png')
# Put the image into a canvas compatible class, and stick in an
# arbitrary variable to the garbage collector doesn't destroy it
canvas.image = ImageTk.PhotoImage(im)
# Add the image to the canvas, and set the anchor to the root left / north west corner
canvas.create_image(20, 10, image=canvas.image, anchor='nw')

# =====================================
#
# BUTTONS
# =====================================
# UP
button = tkinter.Button(frame,
                        text="UP",
                        fg="white",
                        bg='black',
                        command=up)
button.pack(side=tkinter.TOP)

# DOWN
button = tkinter.Button(frame,
                        text="DOWN",
                        fg="white",
                        bg='black',
                        command=down)
button.pack(side=tkinter.BOTTOM)

# RIGHT
button = tkinter.Button(frame,
                        text="RIGHT",
                        fg="white",
                        bg='black',
                        command=right)
button.pack(side=tkinter.RIGHT)

# LEFT
button = tkinter.Button(frame,
                        text="LEFT",
                        fg="white",
                        bg='black',
                        command=left)
button.pack(side=tkinter.LEFT)

# STOP!!!
button = tkinter.Button(frame,
                        text="STOP",
                        fg="red",
                        bg='black',
                        width=25,
                        command=stop)
button.pack(side=tkinter.LEFT)

button1 = tkinter.Button(root,
                         text="EXIT",
                         fg="white",
                         bg='black',
                         width=10,
                         command=close_window)

button1.pack(side=tkinter.BOTTOM)
button1.place(relx=0.85, rely=0.8, anchor='n')
# =========================================================


# =========================================================
root.mainloop()
ser.close()
