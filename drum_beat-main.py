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
sleep(1000)
bass_drum = audio.SoundEffect(
    freq_start=200,
    freq_end=50,
    duration=100,
    vol_start=250,
    vol_end=0,
    waveform=audio.SoundEffect.WAVEFORM_SINE,
    shape=audio.SoundEffect.SHAPE_LOG
)
for i in range(8):
    audio.play(bass_drum)
    sleep(500)
sleep((1000))
# Play a Sound Effect instance, modify an attribute, and play it again
highHat_closed = audio.SoundEffect(
    freq_start=2000,
    freq_end=500,
    vol_start=255,
    vol_end=0,
    duration=50,
    waveform=audio.SoundEffect.WAVEFORM_NOISE
)
for i in range(8):
    audio.play(highHat_closed)
    sleep(500)

sleep(2000)

snare_drum = audio.SoundEffect(
    freq_start=80,
    freq_end=1600,
    vol_start=255,
    vol_end=0,
    duration=100,
    waveform=audio.SoundEffect.WAVEFORM_NOISE,
    shape=audio.SoundEffect.SHAPE_LOG
)
for i in range(8):
    audio.play(snare_drum)
    sleep(500)

sleep(2000)

for bar in range(10):
    audio.play(bass_drum)
    sleep(500)
    audio.play(highHat_closed)
    sleep(500)
    audio.play(snare_drum)
    sleep(500)
    audio.play(highHat_closed)
    sleep(500)
    audio.play(bass_drum)
    sleep(125)
    audio.play(bass_drum)
    sleep(375)
    audio.play(highHat_closed)
    sleep(500)
    audio.play(snare_drum)
    sleep(500)
    audio.play(highHat_closed)
    sleep(500)
sleep((10000))



