#greatest between 4 numbers
a=((input("First no.")))
b=(input(a.replace("First","Second")))
c=(input(a.replace("First","Third")))
d=(input(a.replace("First","Fourth")))
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if(a>b and a>c and a>d):
    print("a is greatest")
elif(b>c and b>a and b>d):
    print("b is greatest")
elif(c>a and c>b and c>d):
    print("c is greatest")
elif(d>a and d>b and d>c):
    print("d is greatest")

