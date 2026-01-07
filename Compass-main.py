########################################################
#                                                      #
#  Program name: Compass                               #
#  Filename: Musical Compass-main.py                   #
#                                                      #
#  Author: Colin Aiken   Date: 18/12/25                #
#                                                      #
#  Description:                                        #
#    Uses compass.heading to display an arrow on the   #
#    LED matrix pointing approximately to north for    #
#    for the major compass directions N, NE E, SE, S,  #
#    SW, W, NW.                                        #
#                                                      #
########################################################

# Imports go at the top
from microbit import *
from math import *

# Display program name
display.scroll("Compass", delay=60)
display.show(Image.ALL_ARROWS, delay=60)
# Initialize variables


# Run forever
while True:
    north = 360-compass.heading() # heading is the reverse of needle
         
    if north >= 337.5 or north < 22.5: # N
        display.show(Image.ARROW_N)
    if north >= 292.5 and north < 337.5: # NE
        display.show(Image.ARROW_NW)
    if north >= 247.5 and north < 292.5: # E
        display.show(Image.ARROW_W)
    if north >= 202.5 and north < 247.5: # SE
        display.show(Image.ARROW_SW)
    if north >= 157.5 and north < 202.5: # S
        display.show(Image.ARROW_S)
    if north >= 112.5 and north < 157.5: # SW
        display.show(Image.ARROW_SE)
    if north >= 67.5 and north < 112.5: # W
        display.show(Image.ARROW_E)        
    if north >= 22.5 and north < 67.5: # NW
        display.show(Image.ARROW_NE)
  
    sleep(100)
        
    