# 1.3.a Дано целое число, не меньше 2. Выведите его наименьший натуральный делитель, отличный от 1

print("The program calculates the smallest divisor of number.")
given_number = 0
while given_number < 2:
    given_number = int(input("Enter a number: "))
while True:
    for i in range(1,given_number+1):
        if given_number%i == 0 and i != 1 and given_number != i:
            print("The smallest divisor of ",given_number," is ",i)
            break
        elif given_number%i == 0 and i == given_number:
            print("You\'ve entered A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers.")
            print(given_number)
            break   
    break
