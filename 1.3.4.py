# 1.3.4 Последовательность состоит из натуральных чисел и заканчивается числом 0
# Определить значение второго по величене элемента

print("The program takes a sequence of natural numbers and ends with zero.")
print("Outputs the second largest element in a sequence.")
print("Enter at least two numbers.")

sequence = []
while True:
    try:
        given_number = int(input("Enter a number from your sequence: "))
        if given_number != 0:
            if given_number not in sequence:
                sequence.append(given_number)
            continue
        elif  given_number == 0 and len(sequence) > 1:
            break
        else:
            print("Enter at least two diferent numbers pls.")
    except:
        print("Something wrong. Try enter a number pls")
        continue
sequence.sort()
print("The second largest element is ",sequence[-2])
