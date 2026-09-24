n = int(input())
book = {}
for _ in range(n):
    p = input().split()
    book[p[0]] = p[1]
q = int(input())
for _ in range(q):
    name = input().strip()
    if name in book:
        print(book[name])
    else:
        print('topilmadi')