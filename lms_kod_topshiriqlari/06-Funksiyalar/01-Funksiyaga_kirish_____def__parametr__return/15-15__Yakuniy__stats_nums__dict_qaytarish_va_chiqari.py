def stats(nums):
    return {
        'count': len(nums),
        'sum': sum(nums),
        'min': min(nums),
        'max': max(nums)
    }
numbers = list(map(int, input().split()))
print(stats(numbers))