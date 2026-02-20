def rem (l,word):
    n = []
    for item in l :
        if not (item == word):
            n.append(item.strip(word))
    return n
l = ["Hariom", "Rohan", "Ved", "an"]
print(rem(l,"an"))

"""
OUTPUT
['Hariom', 'Roh', 'Ved']

"""

