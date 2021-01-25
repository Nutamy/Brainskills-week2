# 1.3.c В первый день спортсмен пробежал Х км, а затем каждый день он увеличивал пробег
# на 10% от предыдущего значения. По данному числу У определите номер дня, на который пробег спортсмена за все дни 
# составит не менее У км. 
# Программа получает на вход действительные числа Х и У и должна
# вывести одно натуральное число.

firstDayDistance = int(input("Enter how many kilometers have you run today? "))
daysInProcess = firstDayDistance
yourGoal = int(input("Enter your goal distance and I'll tell you how long it takes: "))
daysHavePassed = 1
sumDistance = firstDayDistance
while True:
    daysInProcess = daysInProcess + daysInProcess*0.1
    sumDistance += daysInProcess
    daysHavePassed += 1

    if sumDistance > yourGoal:
        print('To achive the goal {}km. You should keep rising distance by 10{} every day for {} days.'.format(yourGoal,"%",daysHavePassed))
        break

print(yourGoal)
