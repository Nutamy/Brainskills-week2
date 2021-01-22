from math import sin,tan,fabs,cos
print("a,b")
a=int(input("a="))
b=int(input("b="))
x=sin((a**b))+(b**(b-a)+a)
y=(cos(x)/sin(x))+(fabs(sin(a*x-(b**x)))**1/6)
print("y={:7.3f}".format(y))