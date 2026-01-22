########################################################
#                                                      #
#  Program name: Proximity Lamp                        #
#  Filename: Proximity Lamp-main.py                    #
#                                                      #
#  Author: Colin Aiken   Date: 22/01/26                #
#                                                      #
#  Description:                                        #
#     Turns a relay on when the radio message 'ping'   #
#     is received (LED matrix lights up to indicate    #
#     this). The relay will long as 'pings' are        #
#     received (i.e tranmitter in range).  If no       #
#     'pings' are received for a set amout of time the #
#     relay will be turned off.                        #
#                                                      #
########################################################

# Imports go at the top
from microbit import *
import radio

pin1.write_digital(0) # turn off relay connected to pin 1
display.scroll('Proximity Lamp', delay=80)
block = Image().invert()
off_delay = 5
signal=0

#for i in range(20):
#    pin1.write_digital(1)
#    display.show(block)
#    sleep(i*50+50)
#    pin1.write_digital(0)
#    display.clear()
#    sleep(1000-i*50)
# Main code block
while True:
    # read radio
    if radio.receive() == 'ping':
        signal = off_delay # set signal timer
    # if 'ping' received turn relay on
    if signal == off_delay:
        display.show(block)
        pin1.write_digital(1)
    # if 'ping' not received after off delay turn relay off
    if signal == 0:
        display.clear()
        pin1.write_digital(0)
    if signal >= 0: #delay countdown
        signal -= 1
    sleep(1000)
