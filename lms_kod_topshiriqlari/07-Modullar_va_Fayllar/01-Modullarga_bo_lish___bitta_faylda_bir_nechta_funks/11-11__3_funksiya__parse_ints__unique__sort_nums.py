def parse_ints(s):
    return list(map(int, s.split()))

def unique(xs):
    return sorted(set(xs))

def sort_nums(xs):
    return sorted(xs)

nums = parse_ints(input())
print(*unique(sort_nums(nums)))