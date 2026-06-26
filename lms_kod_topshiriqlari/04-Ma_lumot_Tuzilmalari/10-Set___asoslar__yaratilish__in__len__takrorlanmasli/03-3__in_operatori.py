malumot = list(map(int, input().replace(",", " ").split()))
c = set(malumot)
son = malumot[0]
if son in c:
    print("YES")
else:
    print("NO")