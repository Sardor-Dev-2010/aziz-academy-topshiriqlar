n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i * j) % 2 == 0:
            print('%d x %d = %d' % (i, j, i * j))