########################################################
#                                                      #
#  Program name: Level                                 #
#  Filename: Level-main.py                             #
#                                                      #
#  Author: Colin Aiken   Date: 17/12/25                #
#                                                      #
#  Description:                                        #
#    Simulates a spirit level with "bubble" displayed  #
#    on LED matrix.  Button A cycles through diff-     #
#    erent levels of "digital viscosity" for the       #
#    spirit (1, 2 [default], 4, 8) causing the bubble  #
#    to move slowly, 1 being no viscosity to 8 being   #
#    fairly thick.  Button B cycles through a 2D       #
#    (bubble effected by movement in both axis) or 1D  #
#    (bubble effected by movement on x axis only all-  #
#    -owing micro.bit to be used as a level on it's    #
#    edge) and 2 sensitivity levels, 1 - 4 deg. of     #
#    bubble movement and 2 - 8 deg. of bubble movment, #
#    in following sequence of presses                  #
#          1 - x-axis only                             #
#          2 - both axis s=2                           #
#          3 - x-axis only                             #
#          4 - both axis s=1 [default]                 #
#                                                      #
########################################################

# Imports go at the top
from microbit import *
from math import *

# Display program name
display.scroll("Spirit Level", delay=60)

# Initialize variables
viscosity = 4 # dampening level
sensitivity = 1 # level sensitivity
x_only = False # single axis level when true
display.scroll("both axis V=4 S=1", delay=80)
# angles as displayed
x_angle = 0 
y_angle = 0
# angles as read from accelerometer
x_angle_now = 0
y_angle_now = 0
x_delta = 0
y_delta = 0

# Run forever
while True:
    # pressing button a cycles viscosity level (dampening)
    if button_a.was_pressed():
        viscosity = viscosity + viscosity
        if viscosity > 8:
            viscosity = 1
        display.scroll("V=", delay=80)
        display.scroll(viscosity, delay=80)
    # pressing button b toggles single axis level
    if button_b.was_pressed():
        x_only = not x_only
        if x_only:
            display.scroll("x only",delay=80)
        else:
            display.scroll("both axis", delay=80)
            if sensitivity == 1:
                sensitivity = 2
                display.scroll("S=2", delay=80)
            else:
                sensitivity = 1
                display.scroll("S=1", delay=80)                 
    # read accelerometer and covert to approx. angle
    #   values are reversed as bubles float
    x_angle_now = - accelerometer.get_x() / (12 * sensitivity)
    y_angle_now = - accelerometer.get_y() / (12 * sensitivity)
    # calc damping rates
    x_damped = (x_angle_now - x_angle) / viscosity
    y_damped = (y_angle_now - y_angle) / viscosity
    # calc bubble position change
    x_delta = round(x_delta + (x_damped - x_delta) / viscosity,6)
    y_delta = round(y_delta + (y_damped - y_delta) / viscosity,6)
    # apply change to x pos
    x_angle = x_angle + x_delta
    if x_only: # apply change to y if axis enabled
        y_angle = max(-1.5, min(1.5, y_angle + y_delta))
    else:
        y_angle = y_angle + y_delta
    print(round(x_angle * sensitivity,2),round(y_angle * sensitivity,2))
    if abs(x_angle) > 5 or abs(y_angle) > 5:
        # if approx. more than 5 deg. from level show helper arrows
        if y_angle < -5:
            if x_angle < -5: # bubble off top left
                display.show(Image.ARROW_NW)
            elif x_angle > 5: # bubble off top right
                display.show(Image.ARROW_NE)
            else: # bubble off top
                display.show(Image.ARROW_N)
        elif y_angle > 5:
            if x_angle < -5: # bubble off bottom left
                display.show(Image.ARROW_SW)
            elif x_angle > 5: # bubble off bottom right
                display.show(Image.ARROW_SE)
            else: # bubble off bottom
                display.show(Image.ARROW_S)
        else:
            if x_angle < -5: # bubble off left
                display.show(Image.ARROW_W)
            if x_angle > 5: # bubble off right
                display.show(Image.ARROW_E)        
    else: # display bubble
        for x in range (5):
            for y in range(5):
                # brightess pixel at centre of bubble
                pix_x =cos(radians((x_angle+2 - x)*40))
                if pix_x < 0:
                    pix_x = 0
                pix_y =cos(radians((y_angle+2 - y)*40))
                if pix_y < 0:
                    pix_y = 0
                pix_xy = pix_x * pix_y * 9
                display.set_pixel(x,y,int(pix_xy))
    
    sleep(50)
        
    