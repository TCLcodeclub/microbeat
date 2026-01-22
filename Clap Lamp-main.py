########################################################
#                                                      #
#  Program name: Clap Lamp                             #
#  Filename: Clay Lamp-main.py                         #
#                                                      #
#  Author: Colin Aiken   Date: 21/01/26                #
#                                                      #
#  Description:                                        #
#     Turns a relay on when a load noise is heard      #
#     (like a clap). A second load noise will turn the #
#     relay off again.                                 #
#                                                      #
########################################################

# Imports go at the top
from microbit import *
import music

display.scroll('Clap Lamp', delay=80)

block = Image().invert()
lamp_on = False

pin1.write_digital(0)
microphone.set_threshold(SoundEvent.LOUD, 60)
microphone.set_threshold(SoundEvent.QUIET, 30)

# Acticvate relay several time to test response times
for i in range(20):
    pin1.write_digital(1)
    display.show(block)
    sleep(i*50+50)
    pin1.write_digital(0)
    display.clear()
    sleep(1000-i*50)

# main routine
while True:
    # #load noise triggers routine
    if microphone.was_event(SoundEvent.LOUD):
        print(lamp_on)
        lamp_on = not lamp_on # toggle relay setting
        if lamp_on: # turn relay on
            display.show(block)
            pin1.write_digital(1)
        else: # turn relay off
            display.clear()
            pin1.write_digital(0)
        
  