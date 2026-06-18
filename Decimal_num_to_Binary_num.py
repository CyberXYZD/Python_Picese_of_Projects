from operator import truediv

number = True
while number:
    try:
        decimal_num = int(input("Enter Decimal Number: "))
        original_num = decimal_num
        final_binary_num = ''

        while decimal_num > 0:
            first_binary_num = decimal_num % 2
            decimal_num = decimal_num // 2
            final_binary_num = str(first_binary_num) + final_binary_num
            print(f"remainder : {decimal_num}  binary : {final_binary_num} ")
        print(f'Decimal Number --> {original_num} Binary Number-->{final_binary_num}' )
        number = False

    except ValueError:
        print(f"Please enter a valid Decimal Number")
