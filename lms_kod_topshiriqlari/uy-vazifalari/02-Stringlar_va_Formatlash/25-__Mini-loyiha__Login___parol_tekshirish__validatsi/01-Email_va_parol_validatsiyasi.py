email = input().strip()
parol = input().strip()
print('@' in email and '.' in email and 8 <= len(parol) <= 16 and email == email.lower())