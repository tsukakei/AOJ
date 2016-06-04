while 1:
    H, W = map(int, raw_input().split())
    if H == 0 and W == 0:
        break
    for i in xrange(H):
        print "".join(["." if (i != 0 and i != H - 1) and (j != 0 and j != W - 1) else "#" for j in xrange(W)])
    print
