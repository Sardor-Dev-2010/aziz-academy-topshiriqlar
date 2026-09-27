def teskari(s):
    if s == "":
        return ""
    return teskari(s[1:]) + s[0]

s = input()
print(teskari(s))