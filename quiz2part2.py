# Author: CRS 11/17/21
import random
# Question 1
possible_days = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G"]
day_check = input("Please input a letter from a to g.")
if day_check in possible_days:
    print("You have class on day {0}.".format(day_check))
else:
    print("You do not have class on day {0}.".format(day_check))

# Question 3
user_cards = list(input("Please enter three numbers between 1 and 50 with spaces in between."))
winning_cards = random.randint(1, 50, 1)
if user_cards[0, 1, 2] == winning_cards[0, 1, 2]:
    print("The winning numbers were {0}, you guessed 3 cards correctly".format(winning_cards))
elif user_cards[0, 1, 2] != winning_cards[0, 1, 2]:
    print("The winning numbers were {0}, you guessed 0 cards correctly".format(winning_cards))