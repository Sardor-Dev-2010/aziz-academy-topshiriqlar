def percent(done, total):
    return int(done * 100 / total)

def bar(p):
    filled = p * 10 // 100
    return "%" * filled + "." * (10 - filled)

def make_progress(done, total):
    p = percent(done, total)
    return "%d%% %s" % (p, bar(p))

done, total = map(int, input().split())
print(make_progress(done, total))