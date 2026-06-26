
n = int(input().strip())
users = []
for _ in range(n):
    username, active = input().split()
    users.append({'username': username, 'active': active == '1'})
count = sum(1 for user in users if user['active'])
print(count)

