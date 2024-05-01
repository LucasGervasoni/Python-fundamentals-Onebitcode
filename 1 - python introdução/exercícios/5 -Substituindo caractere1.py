name = "fifa 23"

character =  name[0].lower()
new = name.replace(character,"#")
new = character + new[1:]
print(new)

str1 = "abc"
str2 = "xyz"

new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

print(f"{new_str1} {new_str2}")