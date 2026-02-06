########################################################
#                                                      #
#  Program name: Two notes test                        #
#  Filename: Stylophone-main.py                        #
#  Modules:  mcp23017.py                               #
#                                                      #
#  Author: Colin Aiken   Date: 06/02/26                #
#                                                      #
#  Description:                                        #
#    Veroboard Stylophone - plays 8 notes from C4 - C5 #
#    using a MCP23017 expander chip for inputs         #
#                                                      #
########################################################

from microbit import *
from mcp23017 import Mcp23017
from math import *


display.scroll("Stylophone", delay=80)

# List of note semitone offsets and names from international A (440Hz)
notes = [
    {'offset': -8, 'name': 'C'},
    {'offset': -6, 'name': 'D'},
    {'offset': -5, 'name': 'E'},
    {'offset': -4, 'name': 'F'},
    {'offset': -2, 'name': 'G'},
    {'offset':  0, 'name': 'A'},
    {'offset':  2, 'name': 'B'},
    {'offset':  4, 'name': 'C'},
    ]

Stylophone_FX = audio.SoundEffect(
                waveform = audio.SoundEffect.WAVEFORM_TRIANGLE,
                fx = audio.SoundEffect.FX_VIBRATO,
                shape = audio.SoundEffect.SHAPE_LOG
                )
for note in notes:
    Stylophone_FX.freq_start = int(440 * 2 ** (note['offset']/12))
    Stylophone_FX.freq_end = Stylophone_FX.freq_start
    Stylophone_FX.duration = 50
    Stylophone_FX.vol_start = 0
    Stylophone_FX.vol_end = 255
    note.update({'start': Stylophone_FX.copy()})
    
    Stylophone_FX.duration = 1000
    Stylophone_FX.vol_start = 255
    Stylophone_FX.vol_end = 255
    note.update({'main': Stylophone_FX.copy()})
    
    Stylophone_FX.duration = 100
    Stylophone_FX.vol_start = 255
    Stylophone_FX.vol_end = 0
    note.update({'end': Stylophone_FX.copy()})
    del note['offset']

# Set up MCP23017 chip
Keyboard = Mcp23017()
# set all bank A pin to inputs
Keyboard.set_io_direction(0,0xff)
# set all internal pullup resistors on bank A to on
Keyboard.set_io_pullups(0,0xff)


last_keycode  = 0 # initailise last_keycode
key = -1 # no key touvhed
while True: # loop foever
    # debounce routine. Stops noise bieng heard when sytlus moves across
    # veroboard
    debounce = 0
    while debounce < 20:
        temp_keycode = Keyboard.io_read(0)
        if temp_keycode == Keyboard.io_read(0):
            debounce += 1
        else:
            debounce = 0

    # Voltage is pulled low by stylus so keycode is inverse        
    inverse_keycode = Keyboard.io_read(0)
    keycode = inverse_keycode^0xff

    # If stylus is touching veroboard value will non-zero
    if keycode: 
        # Only play note if keycode has changed
        if keycode != last_keycode: 
            key = int(log((keycode),2)) # calculate key no. form keycode
            display.show(notes[key]['name']) # display note name on LEDs

            # play note start (ramps volume up from 0)
            audio.play(notes[key]['start'])
            # play note for 1 second
            audio.play(notes[key]['main'], wait=False)

            last_keycode = keycode
    else:
        # if sytlus removed fade note
        display.clear()
        if key >= 0: # only if valid frequency
            
            audio.play(notes[key]['end'], wait=False)
            key = -1
            last_keycode = 0
 