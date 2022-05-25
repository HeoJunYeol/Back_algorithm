from sys import *
n, m = map(int, stdin.readline().split())
n_list = list(map(int, stdin.readline().split()))
s = [0] * n
s[0] = n_list[0]

for i in range(1, n):
    s[i] = s[i-1] + n_list[i]

for _ in range(m):
    a, b = (map(int, stdin.readline().split()))
    if a > 1 :
        answer = s[b-1] - s[a-2]
    else:
        answer = s[b-1]
    stdout.write(str(answer)+'\n')


