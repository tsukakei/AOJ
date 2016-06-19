n = input()
a = input()
b = input()
maxProfit = b - a
minData = min(a, b)
for i in xrange(n - 2):
    a = input()
    maxProfit = max([maxProfit, a - minData])
    minData = min(minData, a)
print maxProfit
