a = input().split()
b = input().split()
d = {}
for w in a:
    d[w] = 1
res = []
for w in b:
    if w in d:
        if w not in res:
            res.append(w)
for w in sorted(res):
    print(w)