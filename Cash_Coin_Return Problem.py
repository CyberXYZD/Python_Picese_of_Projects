value = True
while value:
    try:
        Owe = input("Your Owe: ")
        coin = 0
        charges = int(Owe)

        while charges > 0:
            if charges >= 25:
                charges = charges - 25


            elif charges >= 10:
                charges = charges - 10


            elif charges >= 5:
                charges = charges - 5


            else:
                charges = charges - 1

            coin = coin + 1

        print(f" Your Owe: {charges} and coin: {coin}")
        value = False
    except ValueError:
        print(f"Please enter a valid number")


