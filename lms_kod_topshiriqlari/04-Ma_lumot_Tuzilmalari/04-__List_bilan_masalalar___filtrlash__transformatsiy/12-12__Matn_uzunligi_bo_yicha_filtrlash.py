
n = int(input())
son = input().split()
lst = []
for x in son:
    if len(x) >= n:
        lst.append(x) 
print(lst)