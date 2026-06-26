
matn = input()
words = matn.split()
soz = words[0]
for i in words:
    if len(i) > len(soz):
        soz = i 
print(soz)