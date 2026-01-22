########################################################
#                                                      #
#  Program name: Shake Bell                            #
#  Filename: Shake Bell-main.py                        #
#                                                      #
#  Author: Colin Aiken   Date: 18/01/26                #
#                                                      #
#  Description:                                        #
#    Sends message to anorther Microbit with a note    #
#    to play based to the following button being       #
#    pressed:                                          #
#        no button    - A4                             #
#        button a     - B4                             #
#        button b     - C5                             #
#        button a & b - D5                             #
#                                                      #
########################################################

# Imports go at the top
from microbit import *
import time
import music
import radio

display.scroll('Shake bell', delay=80) # Display program name

# Create the "flash" animation frames.
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

    
while True:
    if accelerometer.was_gesture('shake'):
        display.show(flash, delay=100, wait=False)
        if button_a.is_pressed() and button_b.is_pressed():
            radio.send('D5.S.S.')
        elif button_a.is_pressed():
            radio.send('B4.S.S')
        elif button_b.is_pressed():
            radio.send('C5.S.S')
        else:
            radio.send('A4.S.S.')
       
        
    