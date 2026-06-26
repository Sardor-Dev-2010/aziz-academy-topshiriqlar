t = input().split()
a =  {i.lower() for i in t if i.isalpha()}
if a:
    for token in sorted(a):
        print(token, end=' ')
else:
    print("BO'SH")
        