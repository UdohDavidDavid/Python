import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Removes pygame welcome message
import argparse
import time
from pygame import mixer

parser = argparse.ArgumentParser(description="Type in the amount of time in the format <00:00:00>")
parser.add_argument("time", help="Type in the amount of time in the format <00:00:00>")
args = parser.parse_args()

def convert():
    timer = args.time
    hours, mins, sec = list(map(int, timer.split(":"))) # Converts value of timer from string to int using map.
    hours = hours * 60
    mins = mins + hours
    mins = mins * 60
    sec = sec + mins

    return sec

sec = convert()

def countdown(sec):
    for i in range(sec):
        print(time.strftime("%H:%M:%S", time.gmtime(sec)), end="\r") # time.gmtime converts the number of seconds, e.g 90 - to the format <00:00:00> that is 00:01:03
        sec -= 1
        time.sleep(1) # Countdown every one second

def playsound():
    mixer.init()
    mixer.music.load("Music/Washing.mp3") # Music is in Music dir
    mixer.music.play(-1) # Plays infinitely

def stop():
    input("Time's up buddy...") # Keeps the program running so that the music can continue playing

def timer():
    print(f"Alarm set for {time.strftime("%H:%M:%S",time.gmtime(sec))}")
    countdown(sec)
    playsound()
    stop()

try:
    timer()
except KeyboardInterrupt:
    print("Bye buddy")
