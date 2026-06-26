
n = int(input().strip())
users = []
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    users.append({'username': username, 'tags': tags})
natija_tags = -1 
natija_username = ""
for user in users:
    tag_count = len(user['tags'])
    if tag_count > natija_tags:
        natija_tags = tag_count
        natija_username = user['username']
print(natija_username)

