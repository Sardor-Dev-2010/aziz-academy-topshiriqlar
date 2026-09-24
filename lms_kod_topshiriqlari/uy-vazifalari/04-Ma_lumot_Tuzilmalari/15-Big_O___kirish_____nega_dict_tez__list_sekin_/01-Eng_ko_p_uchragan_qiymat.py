vals = input().split()
freq = {}
order = []
for x in vals:
    if x not in freq:
        order.append(x)
        freq[x] = 0
    freq[x] += 1
best = order[0]
bestc = freq[best]
for x in order[1:]:
    if freq[x] > bestc:
        bestc = freq[x]
        best = x
print(best)