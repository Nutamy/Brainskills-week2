# 1.4.3 По числу n вывести лесенку
# Простите, я не поняла какую нужно лесенку.

listj = ""
x = int(input("Enter a number: "))
for i in range(1,x+1):
    for j in range(1,i+1):
        listj += str(j)
    listj += "\n"
print(listj)

listi = ""
y = int(input("Enter a number: "))
for i in range(1,y+1):
    for j in range(1,i+1):
        listi += str(i)
    listi += "\n"
print(listi)