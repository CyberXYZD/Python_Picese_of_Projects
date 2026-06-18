import random


random_number = random.randint(1, 100)


game_play = True
while game_play:
    try:
        guess_number = int(input("Guess the number between 1 and 100: "))
        if guess_number == random_number:
            print(f"Congratulations! You guessed the number{guess_number}!")
            game_play = False

        elif guess_number > random_number:
            print(f"{guess_number} is too high!")

        elif guess_number < random_number:
            print(f"{guess_number} is too low!")

        else:
            print(f"Unknow Error! Check Stagtge")
    except ValueError:
        print("Please Enter valid Number")



