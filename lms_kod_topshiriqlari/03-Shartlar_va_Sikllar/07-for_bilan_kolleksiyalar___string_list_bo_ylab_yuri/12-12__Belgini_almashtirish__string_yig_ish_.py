
s = input()
total = ""
for i in s:
    if i == "a":
        total += "@"
    else:
        total += i
print(total)