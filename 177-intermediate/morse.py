# Probably very NOT pythonic
# print was giving me a headache
# turns out printing without newline and python versions
# can be pretty rough...
from __future__ import print_function
def cuboid(l, h, d):
    # Print top
    for i in range(0, d):
        for j in range(0, d-i):
            print(" ", end="")
        for j in range(0, l):
            print(":", end="")
        print("/", end="")
        for j in range(0, i):
            print("+", end="")
        print()
    # Print front
    for i in range(h - d):
        for j in range(0, l):
            print("#", end="")
        for j in range(0, d):
            print("+", end="")
        print()
    # Print bottom
    for i in range(0, d):
        for j in range(0, l):
            print("#", end="")
        for j in range(0, (d-1-i)):
            print("+", end="")
        print()

l = (input("Length: "))
h = (input("Height: "))
d = (input("Depth: "))
cuboid(l, h, d)