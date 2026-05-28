
n = int(input().strip())
users = []
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    users.append({'username': username, 'tags': tags})
tags2 = set()
for user in users:
    for tag in user['tags']:
        tags2.add(tag)
print(len(tags2))

