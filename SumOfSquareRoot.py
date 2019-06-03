import math
m,n=map(int,raw_input().split())
a,b=map(int,raw_input().split())
def sqrtsum(m,n):
    sum=0
    for i in xrange(m,n+1,2):
        sum+=math.sqrt(i)
    return sum
if sqrtsum(m,n)>sqrtsum(a,b):
    print "YES"
else:
    print "No"
