
n = int(input())
b = 0
while n > 0:
    digit = n % 10
    b = b * 10 + digit
    n //= 10
print(b)