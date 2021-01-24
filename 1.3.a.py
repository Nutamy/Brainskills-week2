# 1.3.a Дано целое число, не меньше 2. Выведите его наименьший натуральный делитель, отличный от 1
given_number = 0
while given_number < 2:
    given_number = int(input("Enter a number: "))
while True:
    for i in range(1,given_number):
        if given_number%i == 0 and i != 1:
            print("The smallest divisor of ",given_number," is ",i)
            break
        
    break
