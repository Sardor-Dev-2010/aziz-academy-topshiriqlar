login = input().strip()
parol = input().strip()
print(len(login) >= 3 and len(parol) >= 8 and login != parol)