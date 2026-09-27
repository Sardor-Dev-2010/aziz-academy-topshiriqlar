def digits_sum(n):
    return sum(int(d) for d in str(n))

def digits_count(n):
    return len(str(n))

def digits_rev(n):
    return int(str(n)[::-1])

n = int(input())
print(digits_sum(n))
print(digits_count(n))
print(digits_rev(n))