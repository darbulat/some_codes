n = int(input())
a = [int(i) for i in input().split()]
max_a = max(a)

cache = [0]*3
cache[0] = 0
cache[1] = 1
cache[2] = 2

if 0 in a:
    print(cache[0], end=' ')
if 1 in a:
    print(cache[1], end=' ')
if 2 in a:
    print(cache[2], end=' ')

for i in range(3, max_a+1, 3):
    cache[0] = cache[0] + cache[2]
    cache[1] = cache[1] + cache[0]
    cache[2] = cache[1] + cache[2]
    if i in a:
        print(cache[0], end=' ')
    if i+1 in a:
        print(cache[1], end=' ')
    if i+2 in a:
        print(cache[2], end=' ')
