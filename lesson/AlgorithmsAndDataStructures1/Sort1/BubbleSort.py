def bubbleSort(a):
    cnt = 0
    for i in xrange(len(a)):
        for j in reversed(range(i + 1, len(a))):
            if a[j] < a[j - 1]:
                tmp = a[j]
                a[j] = a[j - 1]
                a[j - 1] = tmp
                cnt += 1
    for i in a:
        print i,
    print
    print cnt

if __name__ == '__main__':
    n = input()
    a = map(int, raw_input().split())
    bubbleSort(a)
