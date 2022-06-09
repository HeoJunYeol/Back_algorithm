from sys import *

n = int(stdin.readline())
ex_level = sorted([int(stdin.readline()) for _ in range(n)])
s = 0
for i in range(1,n+1):
    s += abs(i - ex_level[i-1])

stdout.write(str(s))