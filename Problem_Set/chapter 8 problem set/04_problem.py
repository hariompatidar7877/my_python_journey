def sum(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return sum(n-1) + n
    

n = int(input("Enter the sum number"))
print(sum(n))

"""
Enter the sum number5
15

"""