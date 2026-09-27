def palindrom(s):
    if s == s[::-1]:
        return "Ha"
    return "Yo'q"

print(palindrom(input().strip()))