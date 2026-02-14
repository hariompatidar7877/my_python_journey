"""
9. Write a program to print the following star pattern

forn-3
***
* *
***
"""
n = int(input("Enter the number"))
for i in range(1,n+1):
    if(i==1 or i==n):
      print("*"* n, end="")
    else:
     print("*", end="")
     print(" "*(n-2),end="")
     print("*", end="")
    print()



"""
OUTPUT
Enter the number3
***
* *
***
PS C:\Users\hario\OneDrive\Documents\GitHub\my_python_journey> & C:/Users/hario/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/hario/OneDrive/Documents/GitHub/my_python_journey/Problem_Set/chapter 7 problem set/09_problem.py"
Enter the number9
*********
*       *
*       *
*       *
*       *
*       *
*       *
*       *
*********
"""