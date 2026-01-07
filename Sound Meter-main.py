########################################################
#                                                      #
#  Program name: Sound Meter                           #
#  Filename: Sound Meter-main.py                       #
#                                                      #
#  Author: Colin Aiken   Date: 18/12/25                #
#                                                      #
#  Description:                                        #
#    Displays sound level on LED matrix simulating an  #
#    amplitude wave.                                   #
#                                                      #
########################################################

# Imports go at the top
from microbit import *
import music

display.scroll("Sound Meter", delay=60)

# Create 5x5 2D list to store LED levels
w, h = 5, 5
matrix = [[0 for x in range(w)] for y in range(h)] 

current_col = 0

# loop repeats forever
while True:
    volume = microphone.sound_level()
    bar_height = volume // 8.6
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
        
    