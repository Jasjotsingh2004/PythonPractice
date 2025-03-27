a=int(input("enter number"))
b=int(input())
c=int(input())
d=int(input())

if(a>b and a>c and a>d):
    print ("a is greater")
elif(a<b and b>c and b>d ):
    print("b is greater")
elif(c>a and c>b and c>d):
    print("c is greater")
else:
    print(f"and is {d}")
