
s = input()
total = 0
u = "aeiou"
for i in s:
    if i in u:
        total += 1
print(total)