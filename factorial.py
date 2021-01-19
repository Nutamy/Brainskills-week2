n = int(input("Enter number to get factorial: "))
f = 1
for i in range(1, n+1):
    f *= i
x = 1
y = 1
print("Factorial ",n," equils ",f)


is_factorial = int(input("Check if a number is a factorial of any number.\nEnter number for check: "))
while True:
    if is_factorial%x == 0:
        x += 1
        y *= x
        if y == is_factorial:
            print("Yes! The given number is a factorial of ",x)
            break
    elif is_factorial%x >= 1:
        x += 1
        print("The given number is not a factorial.")
        break
