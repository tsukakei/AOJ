while 1:
    H, W = map(int, raw_input().split())
    if H == 0 and W == 0:
        break
    chessboard = "#." * W
    for i in xrange(H):
        board = chessboard[:W] if i % 2 == 0 else chessboard[1:W + 1]
        print board
    print
