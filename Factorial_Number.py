
letter_catch = True
while letter_catch:
    try:
        facto_num = int(input("Enter the Factorial Number "))
        if facto_num == 1 or facto_num <= 0:
            print("This is not a Factorial Number.")
            letter_catch = False



        else:
            for i in range(facto_num,0,-1):
                facto_num = facto_num * i
            print(f"Factorial Number --> {facto_num} ")
            letter_catch = False
    except ValueError:
        print("Please enter a valid Factorial Number.")




