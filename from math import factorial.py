from math import factorial


n=int(input("Enter the value:"))
factorial=1
if n<0:
    print("Negtive number are not aloow:")
else:
    for i in range(1,n):
        factorial=factorial*i
    print("the number of",n,"is",factorial)