# 1.3.b. По данному натуральному числу N найдите наибольшую целую степень двойки,
# не превосходящую N. Выведите показатель степени и саму степень.
# Операцией возведения в степень пользоваться нельзя

given_number = int(input("Enter a number: "))
square_numbers = [1]
twoInDegree = 0
degree = 0
lenthOflist = len(square_numbers)
b = 1
for i in range(given_number):
    b = b + b
    square_numbers.append(b)
    if given_number == square_numbers[-1]:
        degree = square_numbers.index(given_number)
        print("Введённое число это 2 в степени ",degree,". 2 в степени ", degree," = ",given_number)
    

for z in range(len(square_numbers)):
    if square_numbers[z] < given_number and square_numbers[z+1] > given_number:
        D = square_numbers[z]
        degree = square_numbers.index(D)
        print("Ближайшее к числу",given_number," это 2 в степени ",degree,". 2 в степени ", degree," = ",D)

""" print(square_numbers) """