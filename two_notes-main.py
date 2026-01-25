########################################################
#                                                      #
#  Program name: Two notes test                        #
#  Filename: two_notes-main.py                         #
#                                                      #
#  Author: Colin Aiken   Date: 24/01/26                #
#                                                      #
#  Description:                                        #
#    Test for playing two notes simultaneously.        #
#    the following buttons play:                       #
#                                                      #
#        button a     - D5 & A4                        #
#        button b     - C5                             #
#                                                      #
########################################################

# Imports go at the top
from microbit import *
import time
import music
import radio

display.scroll('Two note test', delay=80) # Display program name

# Create the "flash" animation frames.
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]
notes = ['A4', 'B4', 'C5', 'D5', 'E5', 'F5']
note = 0    
while True:
    
    if button_a.was_pressed():
        display.show(flash, delay=100, wait=False)
        radio.send('D5.S.S.')
        radio.send('A4.S.S.')
    if button_b.was_pressed():
        display.show(flash, delay=100, wait=False)
        radio.send('{}.S.S.'.format(notes[note]))
        note = (note + 1) % len(notes)
