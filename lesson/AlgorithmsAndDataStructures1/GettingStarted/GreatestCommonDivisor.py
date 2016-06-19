m, n = map(int, raw_input().split())
if m < n:
    tmp = n
    n = m
    m = tmp
while 1:
    if n == 0:
        print m
        break
    tmp = n
    n = m % n
    m = tmp
