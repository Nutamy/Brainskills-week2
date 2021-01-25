# 1.3.d С клавиатуры вводится целое число N
# Вывести первые N чисел Фибоначчи
# считаем с единицы
iteration = 0
n = int(input("Enter how many the Fibonacci numbers do you need: "))
listOfFibonacci =[]

# Use the traditionl formula of Fibonacci
for i in range(n+1):

    f = ((((1+(5**0.5))/2)**i-((1-(5**0.5))/2)**i)/(5**0.5))
    listOfFibonacci.append(int(f))
    
print(listOfFibonacci[1:])
for s in range(1,len(listOfFibonacci)):
    iteration +=1
    print("{}:{}".format(iteration,int(listOfFibonacci[s])))

# Use ... I don't understant what did I use actualy, may be my intuition
a = 0
b = 1
c = 0
for i in range(n):
    c = a + b
    a = b
    b = c
    print(c)