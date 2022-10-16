from cmath import sqrt
import math
a=float(input("Enter the vlaue of a:"))
b=float(input("Enter the vlaue of b:"))
c=float(input("Enter the vlaue of c:"))
if((a+b)>c and (b+c)>a and (c+a)>b):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("area od t:",area)
else:
    print("not possible")
