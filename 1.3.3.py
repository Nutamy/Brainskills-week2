# 1.3.3 Последовательность чисел вводится до нуля. найдите среди них максимум и минимум
#
print("Enter a sequence of numbers to find min and max.")
print("To end a sequence enter zero.")
given_number = 1
list_of_numbers = []
while given_number != 0:
    try:
        given_number = int(input("Enter a number: "))
        list_of_numbers.append(given_number)
    except:
        print("Wrong!")
        continue
min_of_numbers = min(list_of_numbers)
max_of_numbers = max(list_of_numbers)
print("min={} max={}".format(min_of_numbers,max_of_numbers))