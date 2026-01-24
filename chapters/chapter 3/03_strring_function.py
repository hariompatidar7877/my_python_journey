name = "hariom patidar"


# 1 = len() iishse ham striong ki lenght chack karte hai
print(len(name))

# OUTPUT = 15

# 2 = endswith() & startswith()  ishme haam chack karte hai ki ye ishi se start or end ho raha hai ki nahi
print(name.startswith("hariom"))
print(name.endswith("patidar"))
print(name.startswith("hariop"))
print(name.endswith("patidah"))

# output
# True
# True
# False
# False

# 3 find("value") ishka use haam tab karte hai jab hum vo value ya words find karna hoya hai

print(name.find("om"))
print(name.find("pa"))

# output
# 4
# 7

# 4 count("value") jab hame koi words/value dekhni ho ki kitni jagah baar repeat huvi hai
print(name.count("a"))
print(name.count("r"))

# output
# 3  teen baar a aaya hai name me
# 2  two time r aaya hai name me


#5 =string.replace("old value", "new value") isha ka use ham tab karte hai jab kisi words/ value ki jagah me kisi dusri words/value ko replace karnba ho

print(name.replace("hariom","niklesh"))

# output
# niklesh patidar

# 6 = string.capitalize()  jab hame puri string ke only strating word ke starting element ko capital kar deta hai

print(name.capitalize())

# output
# Hariom patidar


# 7 = string.upper() jab hame puri string ko capital likhna ho

print(name.upper())

# output
# HARIOM PATIDAR

# 8 string.lower()   jab puri string ko small likhna ho


# 9 = string.title()  jab hame puri string ke sabhi words ke starting elements capital karne ho


print(name.title())

# output
# Hariom Patidar

#  10 = string,strip()  jab string me starting & ending me extra space ho to ushe remove kar deti hai

print(name.strip())

# output
# hariom patidar

#  11 = string.split()  string ko list me thod deta hai

print(name.split())

# output
# ['hariom', 'patidar']


#  13  =  string.join() jab list ko add karke string banan ho

# print(name.join())

# 14 string.isalpha()  jab puri string me only alphabate ho

name1 = "hariom"
print(name1.isalpha())

# output
# True

# 15 = string.isdigit()  jab puri string me only digit ho

print(name1.isdigit())

# output
# False




