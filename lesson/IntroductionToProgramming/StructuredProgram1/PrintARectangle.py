while 1:
    H, W = map(int, raw_input().split())
    if H == 0 and W == 0:
        break
    for i in xrange(H):
        print "".join(["#" for i in xrange(W)])
    print
