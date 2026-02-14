#6. Write a program to calculate the factorial of a given number using for loop
# 5 = 1*2*3*4*5
n = int(input("Enter the number"))
product=1
for i in range (1, n+1):
    product = product*i
print(product)

"""
OUTPUT
Enter the number5
120
"""