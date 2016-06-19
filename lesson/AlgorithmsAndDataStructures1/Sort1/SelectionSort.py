def selectionSort(a):
    cnt = 0
    for i in xrange(len(a)):
        min_piv = i
        for j in xrange(i + 1, len(a)):
            if a[j] < a[min_piv]:
                min_piv = j
        if min_piv != i:
            tmp = a[min_piv]
            a[min_piv] = a[i]
            a[i] = tmp
            cnt += 1
    for i in a:
        print i,
    print
    print cnt

if __name__ == '__main__':
    n = input()
    a = map(int, raw_input().split())
    selectionSort(a)
