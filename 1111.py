def super(n):
    o = 1
    for i in range(n+1):
        if i%2 != 0 and i%3 != 0:
            o *= i
    return o

print(super(10))




