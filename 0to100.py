import random

max = input("Please enter your max: ")

if max < 0:
    max = input("Please enter a max again: ")
print("\n")

min = input("Please enter your min: ")

if min > max:
    min = input("Please enter a max again: ")
print("\n")

CompCount = random.randint(min, max)

entryNum = random.randint(min, max)

if CompCount != entryNum:
    print("Sorry the computer won against you")
else:
    print("Somehow you think like a computer")

