tokens = input().split()
if not tokens:
    n = 0
else:
    n = int(tokens[0])

idx = 1
ruyxat = []

for _ in range(n):
    if idx >= len(tokens):
        tokens.extend(input().split())
    ism = tokens[idx]
    ball = int(tokens[idx+1])
    ruyxat.append({'name': ism, 'score': ball})
    idx += 2

if ruyxat:
    best = ruyxat[0]
    for i in range(1, len(ruyxat)):
        current = ruyxat[i]
        if current['score'] > best['score']:
            best = current
        elif current['score'] == best['score']:
            if current['name'] < best['name']:
                best = current
    
    print(f"{best['name']} {best['score']}")