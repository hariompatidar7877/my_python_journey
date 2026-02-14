"""2. Write a program to greet all the person names stored in a list "T" and which starts with S

T["Harry", "Soham", "Sachin", "Rahul"]"""

l =["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")



"""
OUTPUT
Hello Soham
Hello Sachin
"""