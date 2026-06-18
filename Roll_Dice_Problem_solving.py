import random
game_play = True
while game_play:

    ask = input("Roll the dice? (y/n)").lower()
    if ask == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"You rolled, dice one is {dice1}, and, dice two is {dice2}")

    elif ask == "n":
        print("Thank you for playing")
        game_play = False

    else:
        print("Invalid choice")
