from math import sqrt
def isPrimeNumber(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in xrange(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    else :
        return True

if __name__ == '__main__':
    n = input()
    cnt = 0
    for i in xrange(n):
        a = input()
        if isPrimeNumber(a):
            cnt += 1
    print cnt
