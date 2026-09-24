import sys
lines = sys.stdin.read().splitlines()
sep = lines[0] if lines else '-'
words = ' '.join(lines[1:]).split()
print(sep.join(words))