import math

def print_triangles(size):
    size = math.ceil(size/2)
    space = size - 1
    w = 1
    for i in range(size):
        print(" "*space, end="")
        print("*"*w, end="")
        print()
        w+=2
        space-=1

#    *
#   ***
#  *****

def print_better_traingles(size):
    size = math.ceil(size/2)  # height

    for i in range(size):
        # print spaces
        for j in range(size - i - 1):
            print(" ", end="")
        # print stars
        for j in range(2*i + 1):
            print("*", end="")
        print()


print_triangles(69)
#print_better_traingles(69)
