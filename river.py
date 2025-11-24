import sys
import os
# ------------------------
# SUBFUNCTIONS
# ________________________

# Turn the variable on or off
def switch_places(choice, dict):
    if dict[choice]:
        dict[choice] = 0
    else:
        dict[choice] = 1

# Print the options you have to take over the river
def print_options(dict):
    for i in dict.keys():
        print(i, end=" ")
    print()

# Check if entered the right output
def verify(choice, running):
    if choice in dict.keys():
            switch_places(choice, dict)
    elif choice == "q":
        running = False
    else:
        print("Nah man")

def print_other_stuff(true_options, false_options):
    print("#----------------------------------------------------------")
    print("Stuff that are at the other side of the river.")
    for i in true_options:
        print(i)

    print("#----------------------------------------------------------")
    print("Stuff that are still on this side of this river")
    for i in false_options:
        print(i)

    print("#----------------------------------------------------------")

# Print the positions of the animals and the farmer of course
def print_choice(dict):
    # Either taking over or not
    true_options = []
    false_options = []
    # Check if it is true or not
    for i in dict:
        if dict[i]:
            true_options.append(i)
        else:
            false_options.append(i)
    print_other_stuff(true_options, false_options)

# ------------------------
# Main program
# ------------------------
# List of the choices
dict = {"farmer": 1, "fox": 0, "chicken": 0, "grain": 0}
running = True  # Switch

# main loop
try:

    while running:
        # Boilerplate text
        print_options(dict)

        # Enter the damn choice
        choice = input("Please choose one to take to the other side of the river: ")
        verify(choice, running)  # Verify the choice

        # Print the current positions
        print_choice(dict)
        print()

except KeyboardInterrupt:
    sys.exit()

# ------------------------
# End of the program
# ------------------------
