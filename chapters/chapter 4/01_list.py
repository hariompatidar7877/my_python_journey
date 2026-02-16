friends = ["Apple","orange", 5, 555.4, False, "Akash", "Ved"]
print(friends[0])
a = "Hariom"
print(a[0])
print(a[5])
#a[5] = H
"""
 File "c:\Users\hario\OneDrive\Documents\GitHub\my_python_journey\chapters\chapter 4\01_list.py", line 6, in <module>
    a[5] = H
           ^
NameError: name 'H' is not defined
"""
friends[5] = "Hariom"
print(friends)
print(a)
print(friends[1:4])


"""
Apple
H
m
['Apple', 'orange', 5, 555.4, False, 'Hariom', 'Ved']
Hariom
['orange', 5, 555.4]
"""