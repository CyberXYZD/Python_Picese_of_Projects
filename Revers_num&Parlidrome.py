number = True
while number:
    try:
        random_number = int(input("Enter your random number: "))
        final_reverse_number = 0
        original_number = random_number

        while random_number > 0:
            first_reverse_digit = random_number % 10
            random_number = random_number // 10
            final_reverse_number = final_reverse_number * 10 + first_reverse_digit
        print(f"Original --> {original_number} Reverse --> {final_reverse_number}")
        number = False

        if final_reverse_number == original_number:
            print(f"This is Parlidrome")
        else:
            print(f"This is Not Parlidrome")

    except ValueError:
        print(f"Just Enter Number")