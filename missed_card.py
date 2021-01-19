#
#
#

print("")
amountOfCards = int(input("How many card do you have? "))
sumOfCards = 0
for x in range(1,amountOfNumbers+1):
    sumOfCards += x
sumOfremainCards = 0
print("Enter remaining cards consequentially pls.")
while True:
    try:
        remainCard = int(input("Enter the remaining card: "))
        if remainCard > 0