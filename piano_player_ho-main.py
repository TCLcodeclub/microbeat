########################################################
#                                                      #
#  Program name: Piano Key Player with handopver       #
#  Filename: piano_player_ho-main.py                   #
#                                                      #
#  Author: Colin Aiken   Date: 28/12/25                #
#                                                      #
#  Description:                                        #
#                                                      #
########################################################

# Imports go at the top
from microbit import *
import time
import music
import radio
notes = {'C': -8, 'D': -6, 'E': -5, 'F': -4, 'G': -2, 'A': 0, 'B': 2}
notetype = {'S': 4, 'm': 2, 'c': 1, 'q': 0.5, 's': 0.25, 'd': 0.125  }
note = 50
display.scroll("Piano Player handover", delay=60)
player=0
beat = 320
decay = 0.995
volume = 0
receivedKey = ""

def calcNoteLength(noteTypeStr):
    length = int(beat * notetype[noteTypeStr[3]])
    if len(noteTypeStr) > 4:
        for i in noteTypeStr[4:]:
            if i == '.':
                length = int(length * 1.5)
            else:
                length = int(length + beat * notetype[i])
    return length
    

def playKey(message):
    noteStart = time.ticks_ms()
    global receivedKey
    receivedKey = ""
    note = notes[message[0]] + int(message[1]) * 12
    display.show(message[0])
    if message[2] == '#':
        note += 1
        display.set_pixel(4, 0, 9)
    elif message[2] == 'f':
        note -= 1
        display.set_pixel(4, 4, 9)
    freq = int(27.5*2 **(note/12))
    notelength = calcNoteLength(message)
    noteEnd = noteStart + notelength
    volume = 255
    music.pitch(freq)
    # decay note
    noteNow = time.ticks_ms()
    dloop = 0
    while time.ticks_diff(noteEnd,noteNow) > 0:
        if dloop == 0:
            dloop = 5
            set_volume(int(volume))
            volume = volume * decay
            receivedKey=radio.receive()
            if receivedKey:
                print(receivedKey)
                radio.config(group=(player +1 ) % 10)
                radio.send(receivedKey)
                radio.config(group=player)
                receivedKey = ''
        time.sleep_us(200)
        dloop -= 1
        noteNow = time.ticks_ms()
    display.clear()
    set_volume(0)
radio.config(group=player)
display.scroll('P={}'.format(player), delay=60)

while True:
    if not receivedKey:
        receivedKey = radio.receive()
    if button_a.was_pressed():
        player += 1 if player < 9 else -9
        radio.config(group=player)    
        display.scroll('P={}'.format(player), delay=60)
    if receivedKey:
        print(receivedKey)
        playKey(receivedKey)    
    #sleep(5000)    
        
        
    