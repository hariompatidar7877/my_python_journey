#4. Write a program to find whether a given number is prime or not.
n = int(input("Enter the number"))
for i in range(2,n):
    if(n%i)==0:
        print("This number is not prime number")
        break
else:
    print("this is prime number")


"""
OUTPUT
Enter the number4
This number is not prime number
PS C:\Users\hario\OneDrive\Documents\GitHub\my_python_journey> & C:/Users/hario/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/hario/OneDrive/Documents/GitHub/my_python_journey/Problem_Set/chapter 7 problem set/04_problem.py"
Enter the number5
this is prime number
PS C:\Users\hario\OneDrive\Documents\GitHub\my_python_journey> 
"""