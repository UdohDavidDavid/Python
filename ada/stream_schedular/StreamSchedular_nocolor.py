import time as t
import string
import random
import sys
import os
from rich import print as printc
from rich.panel import Panel



#def print_panel_type_shii():
#    panel = r"""
#+==============================================================+
#||  Manage your stream tasks gracefully!!                     ||
#||    :: v1.0                                                 ||
#+==============================================================+
#"""
#    print(panel)
#


def print_panel_type_shii():
    panel_type_shii = r"""
+--------------------------------------------------------------+
|  Manage your streams tasks gracfully!!                       |
|   :: 1.0v                                                    |
+--------------------------------------------------------------+
"""
    print(panel_type_shii, end = "\n")





def ask_for_games():
    print("==> Enter the game to review <single worded> : ", end="")
    game = input("")
    return game

def ask_review_time(game, time, RUNNING_TIME):
    if time.isdigit():
        time = int(time)
        RUNNING_TIME[game] = time
        return True
    return False

def print_values(GAMES, TOTAL_SEC, s_time):
    os.system("clear")
    print_panel_type_shii()
    print("+--------------------------------------------------------------+")
    print(f":: Total time: {t.strftime("%H:%M:%S", t.gmtime(TOTAL_SEC))}")

    for key, value in GAMES.items():
        print(f"      >{key} : {t.strftime("%H:%M:%S", t.gmtime(value))}")

    r_time = TOTAL_SEC - s_time
    print(f":: {t.strftime("%H:%M:%S", t.gmtime(r_time))} ({r_time} seconds) available")
    print("+--------------------------------------------------------------+\n")

def confirm_input(game, time):
    print(f"Confirm entry? (Y/n) <{game} : {t.strftime("%H:%M:%S", t.gmtime(int(time)))}> ({int(time)} seconds): ", end = "")
    choice = input("")

    while 1:
        if choice.lower() == 'y':
            return 1
        elif choice.lower() == 'n':
            return 0
        else:
            print("Follow prompt (Y/n) ", end = "")
            choice = input("")

def confirm_exit():
    print("Start stream? (Y/n)", end = "")
    start_choice = input("")

    while 1:
        if start_choice.lower() == 'y':
            return 1
        elif start_choice.lower() == 'n':
            return 0
        else:
            print("Follow prompt (Y/n) ", end = "")
            start_choice = input("")

def get_run_time(RUNNING_TIME):
    run_time = []

    for key, value in RUNNING_TIME.items():
        run_time.append(value)
    return run_time

def print_total_time(TOTAL_SEC):
    print(f":: Stream ongoing: {t.strftime("%H:%M:%S", t.gmtime(TOTAL_SEC))}")
    sys.stdout.flush()

def print_current_game_time(current, current_timer, RUNNING_TIME):
    print("\n==> ", end = "")
    len_limit = 12

    if len(current) > len_limit:
        for i in range(len_limit):
            print(current[i], end = "")
        print(f"...: {t.strftime("%H:%M:%S", t.gmtime(current_timer))}", end = "")
    else:
        print(f"{current}: {t.strftime("%H:%M:%S", t.gmtime(current_timer))}", end = "")
    print("\t:: Currently reviewing this game!")

    sys.stdout.flush()

def release_discount_code(TOTAL_SEC):
    random_time = random.randint(0, TOTAL_SEC)
    return random_time

def print_discount_code_countdown(random_time):
    if random_time <= 0:
        print(f":: <Discount given!>")
    else:
        print(f":: Discount code in: <{t.strftime("%H:%M:%S", t.gmtime(random_time))}>")

def get_discount_code():
    #chars = string.ascii_letters + string.digits + string.punctuation
    chars = string.digits    # I dicided only digits would be okay
    result = ''.join(random.choice(chars) for _ in range(6))
    return result

def print_discount_code(discount):
    print(f"==> Discount code: {discount}")

def print_all_games(GAMES):
    #print("==> ", end = "")
    len_limit = 12

    for key, value in GAMES.items():
        if len(key) > len_limit:
            print("::", end = " ")
            for i in range(len_limit):
                print(key[i], end = "")
            print(f"...: {t.strftime("%H:%M:%S", t.gmtime(value))}  ", end = " ")
        else:
            print("::", end = " ")
            print(f"{key}: {t.strftime("%H:%M:%S", t.gmtime(value))}  ", end = " ")

    print("\n\n", end = "")


def print_stream_type_shii():
    stream_type_shii = r"""
+--------------------------------------------------------------+
|  Manage your streams tasks gracfully!!                       |
|     :: Stream Ongoing...                                     |
+--------------------------------------------------------------+
"""
    print(stream_type_shii, end = "")


#def print_stream_type_shii():
#    switch = r"""
#/==============================================================\
#||  Manage your stream tasks gracefully!!                     ||
#||    :: v1.0                                                 ||
#\==============================================================/
#"""
#    print(switch)



def start_stream(TOTAL_SEC, GAMES):
    #os.system("clear")
    #print("\033[H\033[J")


    random_time = release_discount_code(TOTAL_SEC);
    i = 0
    j = i
    current = list(GAMES)[i]
    current_timer = RUNNING_TIME[current]

    discount = get_discount_code()

    while TOTAL_SEC >= 0:
        os.system("clear")
        print_stream_type_shii()
        print()
        print_all_games(GAMES)

        print_total_time(TOTAL_SEC)
        print_discount_code_countdown(random_time)
        print_current_game_time(current, current_timer, RUNNING_TIME)

        TOTAL_SEC-=1

        if current_timer > 0:
            current_timer-=1
        else:
            try:
                j+=1
                current = list(GAMES)[j]
                current_timer = RUNNING_TIME[current]
            except IndexError:
                #print("\033[1B", end = "")
                print("\n:: No more games to review!")
                #print("\033[2A", end = "")

        if random_time > 0:
            random_time-=1
        elif random_time <= 0:
            print_discount_code(discount)

        #print("\033[4A", end = "")
        t.sleep(1)

    input("\nPress enter to leave...")
    quit()



#def print_panel_type_shii():
#    panel_type_shii = r"""
#+--------------------------------------------------------------+
#|  Manage your streams tasks gracfully!!                       |
#|   :: 1.0v                                                    |
#+--------------------------------------------------------------+
#"""
#    print(panel_type_shii, end = "\n")


if __name__ == "__main__":
    os.system("clear")
    #print("\033[H\033[J")

    #printc(Panel("Manage you Stream tasks gracfully!!", title="🔥 CLI StreamSchedular 🔥", subtitle="v1.0"))
    #
    print_panel_type_shii()

    #print("\n:: Process! Success! Warning! Error!")

    terms = True
    try:
        while 1:
            print("==> Stream durration <in minutes> : ", end = "")
            TOTAL_MINUTES = input("")
            if TOTAL_MINUTES.isdigit():
                TOTAL_MINUTES = int(TOTAL_MINUTES)
                TOTAL_SEC = TOTAL_MINUTES * 60
                RUNNING_TIME = {}
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
                            print("==> Enter the time to spend reviewing <in seconds> : ", end = "")
                            time = input("")
                            time_check = ask_review_time(game, time, RUNNING_TIME)
                            if time_check:
                                run_time = get_run_time(RUNNING_TIME)
                                if sum(run_time) < TOTAL_SEC:
                                    s_time = sum(run_time)
                                    choice = confirm_input(game, time);
                                    if choice:
                                        GAMES[game] = int(time)
                                        #os.system("clear")
                                        print_values(GAMES, TOTAL_SEC, s_time)
                                        #print(s_time)
                                else:
                                    print("You just went overtime. Trying reducing the amount of time\n")
                                    RUNNING_TIME.pop(game)
                                    continue
                input("Start stream?")
            else:
                print("Please just enter the damn time in minutes")
    except KeyboardInterrupt:
        print("\nStream Stopped")
