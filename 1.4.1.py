# 1.4.1 Вычислить для числа N Сумму S = 1/1+1/2+1/3+...1/n

sumOfFraction = 0
strSumOfFraction = ""
n = int(input("Enter n = "))
for x in range(1,n+1):
    sumOfFraction += 1/x
    strSumOfFraction += ' + 1/' + str(x) 
print(strSumOfFraction[2:]," = ",sumOfFraction)
