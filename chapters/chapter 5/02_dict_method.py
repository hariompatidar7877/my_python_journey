marks = {
    "Hariom" : 98,
    "Ved" : 99,
    "Nitesh" : 89,
    0 : "patidar"
}
print(marks.items())
print(marks.values())
print(marks.keys())
marks.update({"Hariom" : 59, "Jay" : 85})
print(marks)
print(marks.get("Hariom"))  # ishka use karne par agar dict me key vale nahi hai to output none aayega program crash nahi hoga
print(marks["Hariom"])      # ishka use karne par agar dict me key vale nahi hai to output none nahi aayega program crash ho jayega
print(marks.pop("Hariom"))
print(marks)
print(marks.popitem())

"""
OUTPUT
dict_items([('Hariom', 98), ('Ved', 99), ('Nitesh', 89), (0, 'patidar')])
dict_values([98, 99, 89, 'patidar'])
dict_keys(['Hariom', 'Ved', 'Nitesh', 0])
{'Hariom': 59, 'Ved': 99, 'Nitesh': 89, 0: 'patidar', 'Jay': 85}
59
59
59
{'Ved': 99, 'Nitesh': 89, 0: 'patidar', 'Jay': 85}
('Jay', 85)

"""