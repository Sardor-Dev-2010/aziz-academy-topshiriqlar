n = int(input())
vals = input().split()
s = set()
for v in vals:
    s.add(int(v))
q = int(input())
for _ in range(q):
    x = int(input())
    if x in s:
        print("YES")
    else:
        print("NO")