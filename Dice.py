import random

print("Dice Game: Player vs Computer")

input("Press Enter to roll the dice")

user_roll = random.randint(1, 6)
computer_roll = random.randint(1, 6)

print("Your roll:", user_roll)
print("Computer roll:", computer_roll)

if user_roll > computer_roll:
    print("You win")
elif user_roll < computer_roll:
    print("Computer wins")
else:
    print("It is a tie")
