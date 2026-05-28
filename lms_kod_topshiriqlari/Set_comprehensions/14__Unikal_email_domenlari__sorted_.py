e = input().split()
if not e:
    print("BO'SH")
else:
    d = set()
    for i in e:
        if '@' in i:
            d.add(i.split('@')[1].lower())
    if d:
        print(' '.join(sorted(d)))
    else:
        print("BO'SH")