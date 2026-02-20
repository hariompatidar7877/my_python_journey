def pettern(n):
    if(n==0):
        return
    print("*"*n)
    pettern (n-1)
    
n = int(input("Enter your number"))
print(pettern(n))

"""
OUTPUT
Enter your number5
*****
****
***
**
*
None
"""