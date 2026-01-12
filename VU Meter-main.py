########################################################
#                                                      #
#  Program name: VU Meter                           #
#  Filename: Sound Meter-main.py                       #
#                                                      #
#  Author: Colin Aiken   Date: 12/1/26                 #
#                                                      #
#  Description:                                        #
#    Displays sound level on LED matrix simulating an  #
#    amplitude wave.                                   #
#                                                      #
########################################################

# Imports go at the top
from microbit import *

from math import *

class mcp23017:
    def __init__(self, a = 0x20):
        self.ADD = a

    # BANK A=0 B=1
    def set_dir(self,bank,direction):
        data = bytes([bank,direction])
        i2c.write(self.ADD, data)

    def set_pull(self,bank,pull):
        data = bytes([bank + 0x0c,pull])
        i2c.write(self.ADD,data)

    def dig_write(self,bank,value):
        data = bytes([bank + 0x12,value])
        i2c.write(self.ADD,data)

    def dig_read(self,bank):
        buf = bytes([bank + 0x12])
        i2c.write(self.ADD,buf)
        return i2c.read(self.ADD,1)[0]

display.scroll("VU Meter", delay=60)

# Create 5x5 2D list to store LED levels
w, h = 5, 5
matrix = [[0 for x in range(w)] for y in range(h)] 
stack_volume = 0
peak_volume = 0
peak_height = 0
peak_sustain = -1
current_col = 0

# test
p = mcp23017()
# set bank B to inputs
p.set_dir(1,0xff)
# set bank B to pullup
p.set_pull(1,0xff)
# set bank A to outputs
p.set_dir(0,0)
# turn bank A off
p.dig_write(0,0)

# test the leds
for i in range(1,9):
    p.dig_write(0,(2**i)-1)
    sleep(25)
for i in range(8,-1,-1):
    p.dig_write(0,(2**i)-1)
    sleep(100)
# loop for reading buttons
#while True:
#    btns = p.dig_read(1)
#    p.dig_write(0,btns^0xff)
#    sleep(20)

# loop repeats forever
while True:
    volume = microphone.sound_level()
    if volume > stack_volume:
        stack_volume = volume
    elif stack_volume > 0:
        stack_volume -= 16
        if stack_volume < 0:
            stack_volume = 0
    if volume > peak_volume:
        peak_volume = volume
        peak_height = int(log(peak_volume+1,2))
        peak_sustain = 10
    if peak_sustain == 0:
        peak_volume = 0
        peak_height = 0
        peak_sustain = -1
    else:
        peak_sustain -= 1
        
    bar_height = volume // 8.6
    #stack_height = stack_volume // 32
    stack_height = int(log(stack_volume+1,2))
    p.dig_write(0,(2**stack_height)-1|int(2**(peak_height-1)))
    #print(bar_height,log(volume +1, 2 ))
    #l = log(volume)
    # set LED brightness values for current column
    for row in range(2,-1,-1):
        led_brightness = int(bar_height)
        if led_brightness > 9:
            led_brightness = 9
        matrix[current_col][row] = led_brightness
        if row < 2:
            matrix[current_col][4-row] = led_brightness
        bar_height -= 10
        if bar_height <0:
            bar_height = 0
    # Set LED brightness levels left to right staring with 'oldest' column        
    for col in range(5):
        for row in range(5):
            display.set_pixel(col,row,matrix[(current_col+col + 1) % 5][row])
    current_col = (current_col + 1) % 5
    sleep(85)
        
    