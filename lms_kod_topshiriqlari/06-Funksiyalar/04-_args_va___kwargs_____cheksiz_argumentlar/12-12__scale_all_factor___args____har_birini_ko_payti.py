import sys
lines = sys.stdin.read().splitlines()
factor = int(lines[0])
nums = list(map(int, lines[1].split()))
print(' '.join(str(factor * x) for x in nums))