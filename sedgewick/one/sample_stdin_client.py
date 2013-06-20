import sys


data = [float(i) for i in sys.stdin.readlines()]
print "Average is", sum(data) / len(data)
