def f_to_c (f):
    return 5*(f-32)/9
f = int(input("Enter your temperature : "))
print(f_to_c(f))
a = f_to_c(f)
print(f"{round(a,2)}")


"""
OUTPUT
Enter your temperature : 456
235.55555555555554
235.56

"""