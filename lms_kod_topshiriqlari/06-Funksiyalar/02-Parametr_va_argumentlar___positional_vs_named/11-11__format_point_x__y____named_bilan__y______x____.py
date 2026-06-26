def format_point(x,y):
    return f"({x},{y})"
x,y = map(int, input().split())
print(format_point(x,y))
print(format_point(y=y, x=x))
