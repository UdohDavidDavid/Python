import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Removes pygame welcome message

import argparse
import time
from pygame import mixer

import platform

system = platform.system
APP_NAME = "Python Alarm"
os.environ["PULSE_PROP_application.name"] = APP_NAME

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
        input("Time's up buddy...") # Keeps the program running so that the music can continue playing


def lower_other_apps():
    if system == "Windows":
        from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name() != "python.exe":
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                volume.SetMasterVolume(0.2, None)  # lower others
    elif system == "Linux":
        import pulsectl
        pulse = pulsectl.Pulse('volume-control')
        for sink in pulse.sink_input_list():
            if APP_NAME not in sink.proplist.get("application.name", ""):
                pulse.volume_set_all_chans(sink, 0.1)


def restore_volumes():
    if system == "Windows":
        from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                volume.SetMasterVolume(1.0, None)
    elif system == "Linux":
        import pulsectl
        pulse = pulsectl.Pulse('volume-control')
        for sink in pulse.sink_input_list():
            pulse.volume_set_all_chans(sink, 1.0)


   
def timer():
    print(f"Alarm set for {time.strftime("%H:%M:%S",time.gmtime(sec))}")
    countdown(sec)
    lower_other_apps()
    playsound() # Plays song till stoped
    restore_volumes()

try:
    timer()
except KeyboardInterrupt:
    restore_volumes()
    print("Bye buddy.") # Shuts it off

