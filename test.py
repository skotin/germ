__author__ = 'Serg'
import math,pygame,time
#for i in range(0,20):
#    print  i%3%2

a=1
b=2

def myprint(a,b):
    print "a=",a,", b=",b

myprint(a,b)
start = time.clock()
for i in range(1,1000000):
    t=a
    a=b
    b=t
end = time.clock()
myprint(a,b)
print 'Time 1: %s' % (end - start)

myprint(a,b)
start = time.clock()
for i in range(1,1000000):
    a,b=b,a
end = time.clock()
myprint(a,b)
print 'Time 2: %s' % (end - start)
