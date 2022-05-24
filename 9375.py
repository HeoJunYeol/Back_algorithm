from sys import *
from collections import Counter
t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    clothes = []
    for _ in range(n):
        name, kind = stdin.readline().strip().split()
        clothes.append(kind)
    clothes_Counter = Counter(clothes)

    cnt = 1

    for i in clothes_Counter:
        cnt *= clothes_Counter[i] + 1
    print(cnt-1)