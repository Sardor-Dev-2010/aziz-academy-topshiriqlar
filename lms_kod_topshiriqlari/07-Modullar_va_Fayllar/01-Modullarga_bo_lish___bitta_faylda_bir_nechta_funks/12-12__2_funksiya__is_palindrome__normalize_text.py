def normalize_text(s):
    out = ""
    for ch in s.lower():
        if ch.isalnum():
            out = out + ch
    return out

def is_palindrome(s):
    t = normalize_text(s)
    return t == t[::-1]

print(is_palindrome(input()))