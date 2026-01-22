########################################################
#                                                      #
#  Program name: Transmit Image                        #
#  Filename: Transmit Image-main.py                    #
#                                                      #
#  Author: Colin Aiken   Date: 20/01/26                #
#                                                      #
#  Description:                                        #
#     Creates an animated image of ripples eminating   #
#     from one corner.                                 #
#                                                      #
########################################################

# Imports go at the top
from microbit import *
from math import *

display.scroll('Transmit Image')

matrix = ['' ,'', '', '', '']
frames = []

# Build animated image
for radius in range(0,64,3):
    # build image strings in 'matrix'
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
    # build frame by combining sring in 'matrix' in correct format
    frame = ''
    for string in matrix:
        frame += string + ':'
    frame = frame[:-1]
    #append image 'frame' to 'frames' list 
    frames.append(Image(frame))
# Display amimation until stopped
while True:
    display.show(frames, delay=8)
    display.show(frames, delay=8)
    sleep(1000)