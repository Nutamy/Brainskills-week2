# 1.3.2 Определите количество четных элементов
# в последовательности, завершающейся числом 0

print("The program calculate an average of even elements \nin the entered sequence.")
print("Enter zero to stop the program.")

sumOfEvenNumbers = 0
amountOfEvenNumbers = 0
while True:
    try:
        givenNumber = int(input("Enter a number pls: "))
        if givenNumber > 0 and givenNumber%2 == 0:
            sumOfEvenNumbers += givenNumber
            amountOfEvenNumbers += 1
            continue
        elif givenNumber > 0 and givenNumber%2 == 1:
            continue
        elif givenNumber == 0 and len(str(givenNumber)) == 1:
            if amountOfEvenNumbers == 1:
                print("You have entered only one even number. It is not enough.")
                continue
            else:
                break
        elif givenNumber < 0:
            print("Enter positive number pls.")
            continue
    except:
        print("Something wrong. Try again pls.")
        continue
try:
    average = sumOfEvenNumbers/amountOfEvenNumbers
    print("You have entered ",amountOfEvenNumbers," even numbers. Cool!")
    print("Their average is ",average)
except:
    print("It looks like you haven't entered any even numbers.")