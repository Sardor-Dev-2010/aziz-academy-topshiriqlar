numbers = list(map(int, input().split()))
even_numbers = [str(x) for x in numbers if x % 2 == 0]
if even_numbers:
    print(' '.join(even_numbers))
else:
    print("BO'SH")