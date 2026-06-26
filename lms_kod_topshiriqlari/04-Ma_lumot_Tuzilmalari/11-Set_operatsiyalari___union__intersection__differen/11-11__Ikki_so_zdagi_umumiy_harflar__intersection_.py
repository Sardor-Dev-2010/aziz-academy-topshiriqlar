a = input().strip()
b = input().strip()
natija = set(a) & set(b)
if not natija:
    print("BO'SH")
else:
    print("".join(sorted(natija)))