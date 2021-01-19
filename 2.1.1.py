sumOfFraction = 0
strSumOfFraction = ""
n = int(input("Enter n = "))
for x in range(1,n+1):
    sumOfFraction += 1/x
    strSumOfFraction += ' + 1/' + str(x) 
print(strSumOfFraction[2:]," = ",sumOfFraction)
