a = set(map(int, input().split()))
b = set(map(int, input().split()))
natija = a ^ b 
if not natija:
    print("BO'SH")
else:
    print(*sorted(natija))
