marks = {
    "Hariom" : 98,
    "Ved" : 99,
    "Nitesh" : 89,
    0 : "patidar"
}
print(marks)
print(marks, type(marks))
print("Hariom")
print(marks.values())
print(marks.keys())
print(marks.pop("Ved"))
print(marks)
print(marks.popitem())
print(marks)
print(marks.copy())


"""
OUTPUT
{'Hariom': 98, 'Ved': 99, 'Nitesh': 89, 0: 'patidar'}
{'Hariom': 98, 'Ved': 99, 'Nitesh': 89, 0: 'patidar'} <class 'dict'>
Hariom
dict_values([98, 99, 89, 'patidar'])
dict_keys(['Hariom', 'Ved', 'Nitesh', 0])
99
{'Hariom': 98, 'Nitesh': 89, 0: 'patidar'}
(0, 'patidar')
{'Hariom': 98, 'Nitesh': 89}
{'Hariom': 98, 'Nitesh': 89}
"""