
n = int(input())
son = list(map(int, input().split()))
lst = []
for i in son:
    soni = len(str(abs(i)))
    lst.append(soni)
print(lst)