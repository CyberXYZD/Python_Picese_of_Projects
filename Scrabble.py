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

elif count1 > count2:
    print(f"Player1 win!")

else:
    print(f"Player2 win!")
