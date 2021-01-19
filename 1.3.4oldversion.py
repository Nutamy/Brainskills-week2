# 1.3.4 Последовательность состоит из натуральных чисел и заканчивается числом 0
# Определить значение второго по величене элемента

print("The program takes a sequence of natural numbers and ends with zero.")
print("Outputs the second largest element in a sequence.")
print("Enter at least two numbers.")

def sortAndCleanTheSequence(theList):
    sortList = []
    for i in theList:
        if i not in sortList:
            sortList.append(i)
    return sortList

secondLargestElement = 0
sequence = []
newSequence = []
while True:
    try:
        given_number = int(input("Enter a number from your sequence: "))
        if given_number != 0:
            sequence.append(given_number)
            newSequence = sortAndCleanTheSequence(sequence)
            continue
        elif  given_number == 0 and len(newSequence) > 1:
            break
        else:
            print("Enter at least two diferent numbers pls.")
    except:
        print("Something wrong. Try enter a number pls")
        continue
sequence.sort()
print("The second largest element is ",newSequence[-2])
newSequence = sortAndCleanTheSequence(sequence)
print(newSequence)
