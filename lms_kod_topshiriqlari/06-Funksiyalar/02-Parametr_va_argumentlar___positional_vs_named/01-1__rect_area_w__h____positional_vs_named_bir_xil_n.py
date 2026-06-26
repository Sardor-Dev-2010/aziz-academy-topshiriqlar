def rect_area(w, h):
    return w * h
w, h = map(int, input().split())
result1 = rect_area(w, h)
result2 = rect_area(h=h, w=w)
print(result1)
print(result2)