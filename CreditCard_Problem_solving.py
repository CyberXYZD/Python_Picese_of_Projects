number = True
while number:
    try:

        card_Number = input("Please enter a number: ").strip()
        sum_total1 = 0
        sum_total2 = 0
        for card in range(len(card_Number)-2,-1,-2):
            multiply_card = int(card_Number[card]) * 2

            if multiply_card >= 10:
                multiply_card  = multiply_card // 10 + multiply_card % 10

            sum_total1 = sum_total1 + multiply_card

        # print(sum_total1)

        for card in range(len(card_Number)-1,-1,-2):
            remaind_number = int(card_Number[card])
            sum_total2 = sum_total2 + remaind_number
        # print(sum_total2)


        final_valid_num = sum_total1 + sum_total2



        start_number = int(card_Number)
        start_first_digit_number = 0

        while start_number >= 100:
            start_number = start_number // 10

        start_two_digit_number = start_number
        start_first_digit_number = start_two_digit_number // 10

        # print(start_two_digit_number,start_first_digit_number,final_valid_num)




        if final_valid_num % 10 == 0 and start_two_digit_number == 34 or start_two_digit_number == 37:
            print(f"American Express")
            number = False

        elif final_valid_num % 10 == 0 and start_two_digit_number in [22,51, 52, 53, 54, 55]:
            print(f"MasterCard")
            number = False

        elif final_valid_num % 10 == 0 and start_first_digit_number == 4:
            print(f"VisaCard")
            number = False

        else:
            print(f"Not a Valid Number")
            number = False

    except ValueError:
        print(f"Please enter vaild card number")




