n = int(input())
d = [0]*n
count = 0
maxi = 0
for i in range(n):
    a = [int(i) for i in input().split()]
    d[i] = [a[0], a[1]]
d.sort()

for i in range(n):
    for j in range(i):
        if d[i][0] <= d[j][1]:
            count += 1
    if count > maxi:
        maxi = count
        ind = i
    count = 0

print(d[ind][0])
