
d = {}
for i in range(3):
    fan, baho = input().split()
    d[fan] = int(baho)
max_fan = max(d, key = d.get)
print(max_fan, d[max_fan])

    