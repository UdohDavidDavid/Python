import time as t
import sys
import os
from rich import print
from rich.panel import Panel

def ask_for_games():
    print("[bold blue]>> Enter the game to review <single worded> : [/bold blue]", end="")
    game = input("")
    return game

def ask_review_time(time, RUNNING_TIME):
    if time.isdigit():
        time = int(time)
        RUNNING_TIME.append(time)
        return True
    return False

def print_values(GAMES, TOTAL_SEC, s_time):
    #print("-------------------------------------------------")
    print(f"  [bold magenta]Total time: [/bold magenta]{t.strftime("%H:%M:%S", t.gmtime(TOTAL_SEC))}")
    for key, value in GAMES.items():
        print(f"    [bold magenta]>{key} [/bold magenta]: {t.strftime("%H:%M:%S", t.gmtime(value))}")
    r_time = TOTAL_SEC - s_time
    print(f"  {t.strftime("%H:%M:%S", t.gmtime(r_time))} ({r_time} seconds) [bold magenta]available[/bold magenta]")
    #print("-------------------------------------------------")

def confirm_input(game, time):
    print(f"[yellow]>> Confirm entry? (Y/n) <{game} : {t.strftime("%H:%M:%S", t.gmtime(int(time)))}> ({int(time)} seconds): [/yellow]", end = "")
    choice = input("")
    while 1:
        if choice.lower() == 'y':
            return 1
        elif choice.lower() == 'n':
            return 0
        else:
            print("[yellow]Follow prompt (Y/n) [/yellow]", end = "")
            choice = input("")

def confirm_exit():
    print("[red]Start stream? (Y/n)[/red]", end = "")
    start_choice = input("")
    while 1:
        if start_choice.lower() == 'y':
            return 1
        elif start_choice.lower() == 'n':
            return 0
        else:
            print("[yellow]Follow prompt (Y/n) [/yellow]", end = "")
            start_choice = input("")

def start_stream(TOTAL_SEC, GAMES):
    print("[red]Stream Starting!!![/red]")
    while 1:
        print(f"Stream ongoing: ", end = "")
        print(f"{t.strftime("%H:%M:%S", t.gmtime(TOTAL_SEC))}", end = "\r")
        i = 0
        current = list(GAMES)[i]
        print(f"{current}", end = "\r")
        TOTAL_SEC-=1
        t.sleep(1)
        sys.stdout.flush()

if __name__ == "__main__":

    print(Panel("Manage you Stream tasks gracfully!!", title="🔥 CLI StreamSchedular 🔥", subtitle="v1.0"))

    print("[bold cyan] Process! [/bold cyan][green]Success![/green] [yellow]Warning![/yellow] [red]Error![/red]")

    #os.system("clear")
    terms = True
    while 1:
        print("[yellow]\n>> Stream durration <in minutes> : [/yellow]", end = "")
        TOTAL_MINUTES = input("")
        if TOTAL_MINUTES.isdigit():
            TOTAL_MINUTES = int(TOTAL_MINUTES)
            TOTAL_SEC = TOTAL_MINUTES * 60
            RUNNING_TIME = []
            GAMES = {}
            while terms:
                game = ask_for_games()
                if game.isalpha():
                    if game == "start":
                        exit_choice = confirm_exit()
                        if exit_choice:
                            start_stream(TOTAL_SEC, GAMES)
                        continue
                    else:
                        print("[bold cyan]>> Enter the time to spend reviewing <in seconds> (Try not to overflow the stream duration): [/bold cyan]", end = "")
                        time = input("")
                        time_check = ask_review_time(time, RUNNING_TIME)
                        if time_check:
                            if sum(RUNNING_TIME) < TOTAL_SEC:
                                s_time = sum(RUNNING_TIME)
                                choice = confirm_input(game, time);
                                if choice:
                                    GAMES[game] = int(time)
                                    #os.system("clear")
                                    print_values(GAMES, TOTAL_SEC, s_time)
                                    #print(s_time)
                            else:
                                print("[red]You just went overtime. Trying reducing the amount of time\n[/red]")
                                RUNNING_TIME.pop()
                                continue
            input("Start stream?")
        else:
            print("[red]Please just enter the damn time in minutes[/red]")
