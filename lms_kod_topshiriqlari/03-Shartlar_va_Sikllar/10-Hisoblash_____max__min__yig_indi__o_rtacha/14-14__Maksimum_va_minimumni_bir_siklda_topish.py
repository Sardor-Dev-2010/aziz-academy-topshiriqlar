
n = int(input())
son = list(map(int, input().split()))
max_son = son[0]
min_son = son[0]
for i in son:
    if i > max_son:
        max_son = i 
    elif i < min_son:
        min_son = i 
print(max_son, min_son)