from sys import *
n, k = map(int, stdin.readline().split())

coin = []
for _ in range(n):
    coin.append(int(stdin.readline()))
cnt = 0

for i in range(n-1, -1, -1):
    if k == 0:
        break
    elif k >= coin[i]:
        cnt += k//coin[i]
        k %= coin[i]

stdout.write(str(cnt))
