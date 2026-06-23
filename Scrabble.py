game_play = True
while game_play:
    player1 = input("Player 1: ")
    player2 = input("Player 2: ")

    count1 = 0
    count2 = 0

    for p1 in player1:
        count1 = count1 + 1
    #print(count1)

    for p2 in player2:
        count2 = count2 + 1
    #print(count2)

    if count1 == count2:
        print(f"Tie!")
        game_play = False


    elif count1 > count2:
        print(f"Player1 win!")
        game_play = False


    else:
        print(f"Player2 win!")
        game_play = False


    again = True

    while again:
        play_more = input("Do you want to play again? (y/n)").lower()
        if play_more == "y":
            game_play = True
            again = False

        elif play_more == "n":
            print("Thank you for playing!")
            again = False


        else:
            print("Invalid")
            again = True


