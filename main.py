# Inspired from: https://stackoverflow.com/questions/40138031/how-to-read-realtime-microphone-audio-volume-in-python-and-ffmpeg-or-similar

import sounddevice as sd
import numpy as np
import os
import time

duration = 10  # seconds
level = 50
delay_between_clicks = 1
last_click = time.time()

def do_sound(indata, frames, timex, status):
    global last_click
    volume_norm = np.linalg.norm(indata)*10
    #print("|" * int(volume_norm))
    if ((volume_norm>level) & ( time.time() > last_click+delay_between_clicks)):
        print("X")
        os.system("xdotool key Next")
        last_click = time.time()

stream =  sd.InputStream(callback=do_sound)
with stream:
    sd.sleep(duration * 1000)
