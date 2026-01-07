########################################################
#                                                      #
#  Program name: Earthquake                            #
#  Filename: Earthquake-main.py                        #
#                                                      #
#  Author: Colin Aiken   Date: 16/12/25                #
#                                                      #
#  Description:                                        #
#   Measures acceleration on z-axis and dispays a      #
#   scrolling bar chart on the on the LED matrix.      #
#   Pressing button A play sound that changes pitch    #
#   with the movement.                                 #
#                                                      #
########################################################

# Imports go at the top
from microbit import *
import music

display.scroll("Earthquake", delay=60)

# Create 5x5 2D list to store LED levels
w, h = 5, 5
matrix = [[0 for x in range(w)] for y in range(h)] 

current_col = 0

# loop repeats forever
while True:
    g_pitch = accelerometer.get_z() /5
    bar_height = abs(g_pitch) /8
    if button_a.is_pressed(): # play sound when button A pressed
        music.pitch(440 + int(g_pitch))
    else:
        music.stop()
    # set LED brightness values for current column
    for row in range(4,-1,-1):
        led_brightness = int(bar_height)
        if led_brightness > 9:
            led_brightness = 9
        matrix[current_col][row] = led_brightness
        bar_height -= 10
        if bar_height <0:
            bar_height = 0
    # Set LED brightness levels left to right staring with 'oldest' column        
    for col in range(5):
        for row in range(5):
            display.set_pixel(col,row,matrix[(current_col+col + 1) % 5][row])
    current_col = (current_col + 1) % 5
    sleep(100)
        
    