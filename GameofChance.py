# Second Case Study : A Game of Chance - Crap
# • You roll two six-sided dice, each with faces containing one, two, three, four, five and six spots, respectively.
#   When the dice come to rest, the sum of the spots on the two upward faces is calculated.
# • If the sum is 7 or 11 on the first roll, you win. If the sum is 2, 3 or 12 on the first roll (called “craps”), you lose
#   (i.e., the “house” wins).
# • If the sum is 4, 5, 6, 8, 9 or 10 on the first roll, that sum becomes your “point.” To win, you must continue
#   rolling the dice until you “make your point” (i.e., roll that same point value). You lose by rolling a 7 before
#   making your point.

import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def play_game():
    die1, die2 = roll_dice()
    sum_dice = die1 + die2
    print(f"You rolled {die1} + {die2} = {sum_dice}")

    if sum_dice in (7, 11):
        print("You win!")
        return
    elif sum_dice in (2, 3, 12):
        print("Craps! You lose!")
        return
    else:
        point = sum_dice
        print(f"Your point is {point}")

        while True:
            die1, die2 = roll_dice()
            sum_dice = die1 + die2
            print(f"You rolled {die1} + {die2} = {sum_dice}")

            if sum_dice == point:
                print("You made your point! You win!")
                return
            elif sum_dice == 7:
                print("You rolled a 7 before making your point. You lose!")
                return

if __name__ == "__main__":
    play_game()
