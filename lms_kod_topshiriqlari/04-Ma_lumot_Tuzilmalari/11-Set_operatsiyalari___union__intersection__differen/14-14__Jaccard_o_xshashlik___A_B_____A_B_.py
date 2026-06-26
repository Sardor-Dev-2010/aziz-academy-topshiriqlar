A = set(map(int, input().split()))
B = set(map(int, input().split()))
count = len(A & B)
count2 = len(A | B)
index = count / count2
print("{:.3f}".format(index))