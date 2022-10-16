a=int(input("Enter the value of A:"))
b=int(input("Enter the value of B:"))
c=int(input("Enter the value of C:"))
d=int(input("Enter the value of D:"))
if((a<b) and (a<c) and (a<d)):
    print("smallest Value A:",a)
elif((b<c) and (b<a) and (b<d)):
    print("smallst Value B:",b)
elif((c<a) and (c<b) and (c<d)):
    print("smallst Value c:",b)
else:
    print("smallest Value d:",d)
