x, y = map(int, raw_input().split())
while not(x == 0 and y == 0):
    if y < x:
        tmp = y
        y = x
        x = tmp
    print x, y
    x, y = map(int, raw_input().split())
