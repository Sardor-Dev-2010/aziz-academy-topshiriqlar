import random

seed = int(input())
random.seed(seed)
print(chr(random.randint(ord('a'), ord('z'))))