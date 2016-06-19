def insertionSort(a):
    for i in range(len(a)):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = v
        for k in a:
            print k,
        print

if __name__ == '__main__':
    n = input()
    a = map(int, raw_input().split())
    insertionSort(a)
