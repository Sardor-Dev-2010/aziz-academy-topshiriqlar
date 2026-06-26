
s = input()
harf = list(s)
print("{" + ", ".join(f"'{ch}'" for ch in harf) + "}")