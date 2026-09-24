words = input().split()
freq = {}
order = []
for w in words:
    if w not in freq:
        order.append(w)
        freq[w] = 0
    freq[w] += 1
for w in order:
    print(w, freq[w])