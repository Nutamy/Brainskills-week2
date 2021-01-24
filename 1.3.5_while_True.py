# 1.3.5 С клавиатуры вводится число n. Узнать является ли n 
# факториалом какого-либо числа. Если да, то вывести это число.
while True:
    try:
        n = int(input("Enter number to get factorial: "))
        f = 1
        for i in range(1, n+1):
            f *= i
        break
    except:
        print("Enter a number pls.")
        continue
print("Factorial ",n," equils ",f)

print("Check if a number is a factorial of any number.")
x = 1
y = 1

while True:
    try:
        is_factorial = int(input("Enter number for check: "))
        for t in range(1,is_factorial):
            if is_factorial%x == 0:
                x += 1
                y *= x
                if y == is_factorial:
                    print("Yes! The given number is a factorial of ",x)
                    break
            elif is_factorial%x >= 1:
                print("The given number is not a factorial.")
                break
        break
    except:
        print("Enter a number pls.")
        break
