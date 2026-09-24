import sys
data = sys.stdin.read().splitlines()
nums = list(map(int, data[0].split()))
n = int(data[1])
d = {}
for i in range(n):
    k, v = data[2 + i].split()
    d[k] = int(v)
print({'args_count': len(nums), 'args_sum': sum(nums), 'kwargs_count': len(d), 'kwargs_sum': sum(d.values())})