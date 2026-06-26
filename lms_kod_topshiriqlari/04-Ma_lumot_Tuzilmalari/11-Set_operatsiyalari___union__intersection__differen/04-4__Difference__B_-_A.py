a = set(map(int, input().split()))
b = set(map(int, input().split()))
natija = b - a
if not natija:
    print("BO'SH")
else:
    print(*sorted(natija))
