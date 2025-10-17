import os
import argparse
import time
from pygame import mixer

mixer.init()

parser = argparse.ArgumentParser(description="Type in the amount of time")
parser.add_argument("time", help="Type in the amount of time")
args = parser.parse_args()

timer = args.time

hours, mins, sec = list(map(int, timer.split(":")))

hours = hours * 60
mins = mins + hours
mins = mins * 60
sec = sec + mins

def countdown(sec):
    for n in range(sec):
        print(time.strftime("%H:%M:%S",time.gmtime(sec)), end="\r")
        sec -= 1
        time.sleep(1)

def playsong():
    print("Done here")
    mixer.music.load("/home/david/Music/Washing.mp3")
    mixer.music.play(0)

try:
    while True:
        print(f"Alarm set for {time.strftime("%H:%M:%S",time.gmtime(sec))}")
        countdown(sec)
        playsong()
        break
except KeyboardInterrupt:
    print("Uhh Oh")
