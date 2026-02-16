a = (1,2,55,26)
print(type(a))
b = (1)
print(type(b))
c = (1,)
print(type(c))
d = (1,2,55,26, False, "Hariom")
print(type(d))
a[0] = 55
"""
OUTPUT
<class 'tuple'>
<class 'int'>
<class 'tuple'>
<class 'tuple'>
Traceback (most recent call last):
  File "c:\Users\hario\OneDrive\Documents\GitHub\my_python_journey\chapters\chapter 4\03_tuple.py", line 9, in <module>
    a[0] = 55
    ~^^^
TypeError: 'tuple' object does not support item assignment
"""