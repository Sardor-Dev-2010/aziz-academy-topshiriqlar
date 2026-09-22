nums = list(map(int, input().split()))
even = [str(x) for x in nums if x % 2 == 0]
print(" ".join(even) if even else "yo'q")