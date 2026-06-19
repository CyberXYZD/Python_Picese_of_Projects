import random


continue_game = True

while continue_game:


    wrong_choose = True
    game_player =''
    while wrong_choose:

            player = input("Rock, Paper or Scissors? (r/p/s) ").lower()
            if player == "r":
                print("You Choose Rock")
                wrong_choose = False
            elif player == "p":
                print("You Choose Paper")
                wrong_choose = False
            elif player == "s":
                print("You Choose Scissors")
                wrong_choose = False
            else:
                print("Invalid Input please Enter r, p, or s")

            game_player = player
            if game_player == "r":
                game_player = "rock"
            elif game_player == "p":
                game_player = "paper"
            elif game_player == "s":
                game_player = "scissors"





    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    print(f"Computer Choose {computer.title()}")

    if game_player == computer:
        print("Tie")

    elif game_player == "rock" and computer == "paper":
        print("You Lose")

    elif game_player == "paper" and computer == "scissors":
        print("You Lose")

    elif game_player == "scissors" and computer == "rock":
        print("You Lose")

    else:
        print("You Win")

    game_try_more = True
    while game_try_more:
        asking = input("Do you want to play again? (y/n) ").lower()
        if asking == "y":
            continue_game = True
            game_try_more = False

        elif asking == "n":
            continue_game = False
            game_try_more = False
            print("Thank you for playing")


        else:
            print("Invalid Input please Enter y or n")
            game_try_more = True









