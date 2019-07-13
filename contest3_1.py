n = int(input())
a = [int(i) for i in input().split()]
max_a = max(a)

cache = [0]*1000
cache[0] = 0
cache[1] = 1
cache[2] = 2

for i in range(3, max_a+1):
    cache.append(cache[i - 1] + cache[i - 3])

for i in a:
    print(cache[i], end=' ')