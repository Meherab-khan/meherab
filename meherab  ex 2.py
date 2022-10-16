a=int(input("Enter the value of A:"))
b=int(input("Enter the value of B:"))
c=int(input("Enter the value of C:"))
if((a>b) and (a>c)):
    print("largest Value A:",a)
elif((b>c) and (b>a)):
    print("largest Value B:",b)
else:
    print("largest Value c:",c)
