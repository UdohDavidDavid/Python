import argparse
import time
from pygame import mixer

parser = argparse.ArgumentParser(description="Type in the amount of time")
parser.add_argument("time", help="Type in the amount of time")
args = parser.parse_args()

def convert():
    timer = args.time
    hours, mins, sec = list(map(int, timer.split(":")))
    hours = hours * 60
    mins = mins + hours
    mins = mins * 60
    sec = sec + mins
    return sec

sec = convert()

def countdown(sec):
    for i in range(sec):
        print(time.strftime("%H:%M:%S", time.gmtime(sec)), end="\r")
        sec -= 1
        time.sleep(1)

def playsound():
    mixer.init()
    mixer.music.load("/home/david/Music/Washing.mp3")
    mixer.music.play(-1)

def stop():
    input("Time's up buddy...")

def timer():
    print(f"Alarm set for {time.strftime("%H:%M:%S",time.gmtime(sec))}")
    countdown(sec)
    playsound()
    stop()

try:
    timer()
except KeyboardInterrupt:
    print("Bye buddy")
