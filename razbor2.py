# 1.4.4 

while True:
    n = int(input("Enter how many cards do you had? \nI had: "))
    all_num_card = 0
    sum_cards = 0
    for i in range(1, n):
        all_num_card += i
        x = int(input("card lefts: "))
        sum_cards += x
    all_num_card += n
    a = all_num_card - sum_cards
    if  a > 0:
        print("You've lost the card with number of {}".format(a))
        break
    else:
        print("Something wrong!")
        continue