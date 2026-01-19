# Imports go at the top
from microbit import *
import music

pin1.write_digital(0)
lamp_on = False
microphone.set_threshold(SoundEvent.LOUD, 100)
display.scroll('Clap Lamp', delay=80)
for i in range(20):
    pin1.write_digital(1)
    sleep(i*50+50)
    pin1.write_digital(0)
    sleep(1000-i*50)
# Code in a 'while True:' loop repeats forever
while True:    
    if microphone.is_event(SoundEvent.LOUD):
        print(lamp_on)
        lamp_on = not lamp_on
        if lamp_on:
            display.show(Image.SQUARE)
            pin1.write_digital(1)
        else:
            display.clear()
            pin1.write_digital(0)
        sleep(250)
  