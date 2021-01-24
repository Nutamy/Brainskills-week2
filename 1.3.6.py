# 1.3.6 Дана последовательность натуральных чисел. Определите.
# какое наибольшее число подряд идущих эллементов 
# этой последовательности равны друг другу

a = int(input"Enter a number pls: ")
b = int(input"Enter a number pls: ")
countA = 0
countB = 0
listA = []
listB = []
while a == b:
    if countA > countB or countA == 0:
    listA.append(a)
    countA += 1
if a != b:
    listB.append(b)
    countB += 1

