########################################################
#                                                      #
#  Program name: Shake Bell                            #
#  Filename: Piano conductor-main.py                   #
#                                                      #
#  Author: Colin Aiken   Date: 29/12/25                #
#                                                      #
#  Description:                                        #
#                                                      #
########################################################

# Imports go at the top
from microbit import *
import time
import music
import radio
# Create the "flash" animation frames. Can you work out how it's done?
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

display.scroll('Shake bell', delay=80)
    
while True:
    if accelerometer.was_gesture('shake'):
        display.show(flash, delay=100, wait=False)
        if button_a.is_pressed() and button_b.is_pressed():
            radio.send('E5.S.S.')
        elif button_a.is_pressed():
            radio.send('B4.S.S')
        elif button_b.is_pressed():
            radio.send('C5.S.S')
        else:
            radio.send('A4.S.S.')
       
        
    