w = input().split()
if not w:
    print(0)
else:
    p = set()
    for i in w:
        x = i.lower()
        p.add((x, len(x)))
    print(len(p))
    for word, length in sorted(p):
        print(f"{word}:{length}")