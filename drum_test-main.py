# Imports go at the top
from microbit import *
from audio import SoundEffect

# Play the default Sound Effect
#audio.play(audio.SoundEffect())

# Create a new Sound Effect and immediately play it
audio.play(audio.SoundEffect(
    freq_start=400,
    freq_end=2000,
    duration=500,
    vol_start=100,
    vol_end=255,
    waveform=audio.SoundEffect.WAVEFORM_TRIANGLE,
    fx=audio.SoundEffect.FX_VIBRATO,
    shape=audio.SoundEffect.SHAPE_LOG
))

# Play a Sound Effect instance, modify an attribute, and play it again
my_effect = audio.SoundEffect(
    freq_start=2000,
    freq_end=1000,
    vol_start=255,
    vol_end=100,
    waveform=audio.SoundEffect.WAVEFORM_NOISE
)
for f in range(0, 43):
        my_effect.freq_start = 2000 - f ^ 2
        my_effect.freq_end = 2000 + f ^ 2
        my_effect.duration = 25
        audio.play(my_effect)    
        sleep(200)
        audio.play(my_effect)    
        sleep(200)
        my_effect.duration= 50
        audio.play(my_effect)    
        sleep(400)


# You can also create a new effect based on an existing one, and modify
# any of its characteristics via arguments
my_modified_effect = my_effect.copy()
my_modified_effect.waveform = audio.SoundEffect.WAVEFORM_NOISE
audio.play(my_modified_effect)

