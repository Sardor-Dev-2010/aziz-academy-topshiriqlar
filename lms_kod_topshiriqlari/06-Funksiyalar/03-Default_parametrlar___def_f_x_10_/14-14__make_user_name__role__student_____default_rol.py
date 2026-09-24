import sys
d = sys.stdin.read().split()
name = d[0]
role = d[1] if len(d) > 1 else 'student'
print('name=%s, role=%s' % (name, role))