
n = int(input())
a = list(map(int, input().split()))
print(max(set(a), key=lambda x: a.count(x)))