# 2. Write a program to fill in a letter template given below with name and date.

letter = '''

Dear </Name>,

You are selected!

</Date|>'''

print(letter.replace("</Name", "Hariom").replace("</Date|>", "24/1/2026"))

# output
# Dear Hariom>,

# You are selected!

# 24/1/2026
