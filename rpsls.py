'''
The MIT License (MIT)
Copyright (c) 2016 Antal Janos Monori.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

###########
# Imports #
###########

# needed for checking python version
from sys import version_info

# needed for the game mechanics
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

####################
# Helper functions #
####################

def number_to_name(num):
    if num == 0:
        name = "rock"
        return name
    elif num == 1:
        name = "Spock"
        return name
    elif num == 2:
        name = "paper"
        return name
    elif num == 3:
        name = "lizard"
        return name
    elif num == 4:
        name = "scissors"
        return name

def name_to_number(name):
    if name.lower() == "rock".lower():
        num = 0
        return num
    elif name.lower() == "Spock".lower():
        num = 1
        return num
    elif name.lower() == "paper".lower():
        num = 2
        return num
    elif name.lower() == "lizard".lower():
        num = 3
        return num
    elif name.lower() == "scissors".lower():
        num = 4
        return num

########
# Main #
########

def rpsls(name):
    player_number = name_to_number(name)
    print("Player chooses "+number_to_name(player_number))
    comp_number = random.randrange(5)
    print("Computer chooses "+number_to_name(comp_number))
    diff = (player_number - comp_number) % 5
    if diff <= 2 and diff != 0:
        print("Player wins!\n")
    elif diff >=3 and diff != 0:
        print("Computer wins!\n")
    else:
        print("Player and computer tie!\n")

if __name__ == '__main__':
    running = True
    while running:
        py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2
        if py3:
          response = input("Rock, paper, scrissors, Lizard, Spock: ")
        else:
          response = raw_input("Rock, paper, scrissors, Lizard, Spock: ")

        if response == "exit":
            running = False
            break
        else:
            rpsls(response)
