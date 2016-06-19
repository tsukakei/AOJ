a, b, c = map(int, raw_input().split())
cnt = 0
for i in xrange(a, b + 1):
    if c % i == 0:
        cnt += 1
print cnt
