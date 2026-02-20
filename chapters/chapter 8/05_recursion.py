"""
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1
factorial(n) = n * factorial(n-1)
"""
def factorial(n):
    if(n == 1 or n ==0):
        return 1
    return n*factorial(n-1)
n = int(input("Enter a number"))
print(f"The factorial this number is :  {factorial(n)}")

"""
OUTPUT
Enter a number5
The factorial this number is :  120
PS C:\Users\hario\OneDrive\Documents\GitHub\my_python_journey> & C:/Users/hario/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/hario/OneDrive/Documents/GitHub/my_python_journey/chapters/chapter 8/05_recursion.py"
Enter a number3
The factorial this number is :  6
"""