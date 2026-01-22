########################################################
#                                                      #
#  Program name: Proximity Transmitter                 #
#  Filename: Proximity Transmitter-main.py             #
#                                                      #
#  Author: Colin Aiken   Date: 22/01/26                #
#                                                      #
#  Description:                                        #
#     Creates an animated image of ripples eminating   #
#     from one corner.                                 #
#     Transmitter is initialy turned off. Pressing     #
#     button 'a' turns on the transmitter and the      #
#     message 'ping' send over radio which operates a  #
#     relay on the other Microbit. While active the    #
#     aminated image is diplayed for every trans-      #
#     mission. Pressing button 'b' stops the trans-    #
#     mitter                                           #
#                                                      #
########################################################

# Imports go at the top
from microbit import *
from math import *
import radio

matrix = ['' ,'', '', '', '']
frames = []
transmit_on = False

display.scroll('Proximity transmitter', delay=80)
radio.config(power=1)

# Build animated image
for radius in range(0,64,3):
    for y in range(5):
        if y == 0:
            angle = atan2(1,1)
        else:
            angle = atan2(y,0)
        brightness = round(max(0,9 - abs(y * 9 - sin(angle) * radius)))
        matrix[y] = '%i' % (brightness)
        if y > 0:
            matrix[0] += '%i' % (brightness)
        for x in range(1, y + 1):
            angle = atan2(y,x)
            brightness = round(max(0,9 - abs(y * 9 - sin(angle) * radius)))
            matrix[y] += '%i' % (brightness)
            if y > x:
                matrix[x] += '%i' % (brightness)
    frame = ''
    for string in matrix:
        frame += string + ':'
    frame = frame[:-1]
    frames.append(Image(frame))

# Main loop    
while True:
    # button 'a' turn on transmitter
    if button_a.was_pressed():
        transmit_on = True
        radio.on
    # button 'b' torns off transmitter
    if button_b.was_pressed():
        transmit_on = False
        radio.off
    # transmit message while active
    if transmit_on:
        display.show(frames, delay=8)
        radio.send('ping')
        display.show(frames, delay=8)
    sleep(1648) # makes 2 seconds when added image animation time