def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

def count_consonants(s):
    return sum(1 for ch in s.lower() if ch.isalpha() and ch not in "aeiou")

s = input().strip()
print(count_vowels(s))
print(count_consonants(s))