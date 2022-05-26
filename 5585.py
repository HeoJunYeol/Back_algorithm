from sys import *
money = 1000 - int(stdin.readline())
coin = [500, 100, 50, 10, 5, 1]
count = 0
for i in range(len(coin)):
    if money == 0:
        break
    elif money >= coin[i]:
        count += money//coin[i]
        money %= coin[i]

stdout.write(str(count))