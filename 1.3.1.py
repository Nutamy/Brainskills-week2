# 1.3.1 Определите среднее значение всех элементов
# последовательности, завершающейся числом 0

print("The program calculate an average.\nEnter zero to stop the program.")
sumOfNumbers = 0
amountOfNumbers = 0
while True:
    try:
        given_number = int(input("Enter a number pls: "))
        if given_number > 0:
            sumOfNumbers += given_number
            amountOfNumbers += 1
            continue
        elif given_number == 0 and len(str(given_number)) == 1:
            if amountOfNumbers == 1:
                print("You have entered only one number. It is not enough.")
                continue
            else:
                break
        elif given_number < 0:
            print("Enter positive number pls.")
            continue
    except:
        print("Somethin wrong. Try again pls.")
        continue
try:
    print("You have entered ",amountOfNumbers," numbers. Cool!")
    print("Their average is ",(sumOfNumbers/amountOfNumbers))
except:
    print("It looks like you haven't entered any numbers.")

    

