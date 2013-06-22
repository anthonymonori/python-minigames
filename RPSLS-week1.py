# Rock-paper-scissors-lizard-Spock template
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

# helper functions

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
    if name == "rock":
        num = 0
        return num
    elif name == "Spock":
        num = 1
        return num
    elif name == "paper":
        num = 2
        return num
    elif name == "lizard":
        num = 3
        return num
    elif name == "scissors":
        num = 4
        return num

# main function

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
      
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
