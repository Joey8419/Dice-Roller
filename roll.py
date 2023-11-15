import random

# unit code characters to build art:

# ● ┌ ─ ┐ │ └ ┘

# Created a dictionary of dice art by using {}
# Each key is a number
# each value is a tuple made of String
dice_art = {
    
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

# Create a list of dice (numbers) by using []
# These are random numbers generated between 1 and 6
dice = []
# Total to calculate the total
total = 0
# Ask user for input for a number of dice
# type cast input as an integer
number_of_dice = int(input("How many dice?: "))

# Generate a random number between (1, 6)
# random.randint(1, 6)
# Then append number to list of dice
# Do this number amount of times depending on how many dice the user enters in
# Now add code to for loop
for die in range(number_of_dice):
    dice.append(random.randint(1, 6))


# Create nested for loop 

# Calculate total and iterate and sum all of the elements within the list
# Use another for loop
for die in dice:
    total += die # die = current value
print (f"total: {total}")

# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#

