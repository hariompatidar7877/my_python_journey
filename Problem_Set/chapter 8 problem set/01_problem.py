def gretest (a,b,c):
    if(a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a = int(input("enter number"))
b = int(input("enter number"))
c = int(input("enter number"))

print(gretest(a,b,c))
    



"""
OUTPUT
enter number451
enter number6523
enter number32
6523

"""