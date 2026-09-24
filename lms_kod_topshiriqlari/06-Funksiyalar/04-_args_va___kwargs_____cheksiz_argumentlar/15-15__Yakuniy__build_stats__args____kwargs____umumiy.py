import sys
data = sys.stdin.read().splitlines()
nums = list(map(int, data[0].split()))
n = int(data[1])
keys = []
total = 0
for i in range(n):
    k, v = data[2 + i].split()
    keys.append(k)
    total += int(v)
print({'count': len(nums), 'min': min(nums), 'max': max(nums), 'sum': sum(nums), 'extra_keys': keys, 'extra_sum': total})