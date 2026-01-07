########################################################
#                                                      #
#  Program name: Piano Conductor                       #
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
treble1 = ['D5.q',                               # She
         'E5.c' , 'G5.c' , 'G5.m' ,            # love you, yeah
         'F5#c.', 'E5.qc', 'Rs.q' , 'D5.q' ,   # yeah, yeah.  She
         'E5.c' , 'G5.c' , 'G5.m' ,            # loves you, yeah
         'F5#c.', 'E5.qc', 'Rs.q' , 'D5.q',    # yeah, yeah.  She
         'E5.c' , 'G5.c', 'G5.m',              # loves you, yeah
         'F5#m' ,         'E5.m',              # yeah, yeah
         'E5.Sm.'                              # yeah.
        ]
treble2 = ['Rs.q',                             # She
         'Rs.c' , 'E5.c' , 'Rs.c', 'E5#c' ,    # love you, yeah
         'B4.c.', 'B4.qc', 'Rs.c',             # yeah, yeah.  She
         'Rs.c' , 'E5.c' , 'Rs.c', 'E5.c' ,    # loves you, yeah
         'C5#c.', 'C5.qc', 'Rs.c',             # yeah, yeah.  She
         'Rs.c' , 'E5.c' , 'Rs.c', 'E5.c' ,    # loves you, yeah
         'Rs.c' , 'C5.c' , 'C5.m',             # yeah, yeah
         'Rs.c' , 'D5.c' , 'Rs.c', 'D5.c' ,    # yeah.
        ]
treble3 = ['Rs.q',                             # She
         'Rs.c' , 'B4.c' , 'Rs.c', 'B4.c' ,    # love you, yeah
         'G4.c.', 'G4.qc', 'Rs.c',             # yeah, yeah.  She
         'Rs.c' , 'C5#c' , 'Rs.c', 'C5.c' ,    # loves you, yeah
         'A4.c.', 'G4.qc', 'Rs.c',             # yeah, yeah.  She
         'Rs.c' , 'C5fc' , 'Rs.c', 'C5.c' ,    # loves you, yeah
         'Rs.c' , 'G4.c' , 'G4.m',             # yeah, yeah
         'Rs.c' , 'B4.c' , 'Rs.c', 'B4.c' ,    # yeah.
        ]
treble4 = ['Rs.q',                             # She
         'Rs.c' , 'G4.c' , 'Rs.c', 'G4.c' ,    # love you, yeah
         'Rs.c.', 'Rs.qc', 'Rs.c',             # yeah, yeah.  She
         'Rs.c' , 'G4.c' , 'Rs.c', 'G4.c' ,    # loves you, yeah
         'Rs.c.', 'Rs.qc', 'Rs.c',             # yeah, yeah.  She
         'Rs.c' , 'G4.c' , 'Rs.c', 'G4.c' ,    # loves you, yeah
         'Rs.c' , 'Rs.c' , 'Rs.m',             # yeah, yeah
         'Rs.c' , 'G4.c' , 'Rs.c', 'G4.c' ,    # yeah.
        ]
base1 = ['Rs.q',                               # She
         'D2.c.', 'D2.q' , 'B2.m' ,            # love you, yeah
         'G2.c' , 'B2.q' , 'E3.qc', 'B2.c' ,   # yeah, yeah.  She
         'A2.c.', 'A2.q' , 'E3.m' ,            # loves you, yeah
         'A2.c' , 'E3.q' , 'A3.qc', 'A2.c' ,   # yeah, yeah.  She
         'C3.c.', 'C3.c' , 'G2.c.', 'G2.q' ,   # loves you, yeah
         'C3.c.', 'C3.q' , 'G2.c' , 'C2.c' ,   # yeah, yeah
         'G2.c.', 'G2.q' , 'D2.c.', 'D2.q'     # yeah.
        ]
tune = [treble1, treble2, treble3, treble4, base1]
totalKeys = len(tune)

nextNoteIndex = [0] * (totalKeys)
nextNoteTime = [0] * (totalKeys)
print(len(nextNoteIndex))
notes = {'C': -8, 'D': -6, 'E': -5, 'F': -4, 'G': -2, 'A': 0, 'B': 2}
notetype = {'S': 4, 'm': 2, 'c': 1, 'q': 0.5, 's': 0.25, 'd': 0.125  }
note = 50
display.scroll("Piano Conductor", delay=60)
player=0
beat = 320
decay = 0.995
volume = 0
receivedKey = ""


def calcNoteLength(noteTypeStr):
    length = int(beat * notetype[noteTypeStr[3]])
    #print(noteTypeStr[3], length)
    if len(noteTypeStr) > 4:
        for i in noteTypeStr[4:]:
            if i == '.':
                length = int(length * 1.5)
            else:
                length = int(length + beat * notetype[i])
            #print(i, length)
    return length
    
def setNote(message):
    note = notes[message[0]] + int(message[1]) * 12 # note letter and octave 
    display.show(message[0])
    if message[2] == '#': # sharp
        note += 1
        display.set_pixel(4, 0, 5)
    elif message[2] == 'f': # flat
        note -= 1
        display.set_pixel(4, 4, 5)
    return int(27.5 * 2 ** (note/12))


def playKey(message):
    tStart = time.ticks_us()
    noteStart = time.ticks_ms()
    global receivedKey
    receivedKey = ""
    freq = setNote(message)
    notelength = calcNoteLength(message)
    #print(notelength)
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
                break
        time.sleep_us(200)
        dloop -= 1
        noteNow = time.ticks_ms()
    display.clear()
    set_volume(0)
    
#print(tune)
#print(len(tune[0]))
#print(len(tune[1]))
#print(tune[0][0])
#print(tune[4][0])
# loop repeats forever
timer = time.ticks_ms()
for k in range(totalKeys):
    nextNoteTime[k] = timer
while True:
    #print (timer)
    
    for k in range(totalKeys):
        if timer >= nextNoteTime[k] and nextNoteIndex[k] < len(tune[k]):
            message = tune[k][nextNoteIndex[k]]
            if message[0:2] != "Rs":
                radio.config(group=k)
                radio.send(message)
                #print(k ,message)
            nextNoteIndex[k] += 1
            nextNoteTime[k] += calcNoteLength(message)
            #print(k,nextNoteIndex[k], nextNoteTime[k])
    if button_a.was_pressed():
        for k in range(totalKeys):
            nextNoteIndex[k] = 0
            nextNoteTime[k] = timer
            
    #for i in treble1:
    #    print(i)
    #    if i[0:2] == 'Rs':
    #        sleep(beat * notetype[i[3]])
    #    else:
    #        # playKey(i)
    #        radio.send(i)
    #        sleep(beat * notetype[i[3]])
    #receivedKey = radio.receive()
    #if receivedKey:
    #    playKey(receivedKey)    
    sleep(1)
    timer = time.ticks_ms()
        
        
    