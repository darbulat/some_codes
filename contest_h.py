n = int(input())
m = int(input())
k = int(input())
a = ['']*n

for i in range(n):
    a[i] = input()

unique_ip = dict()
count = 0

for i in range(n-m+1):
    for j in range(i, i+m):
        if a[j] not in unique_ip:
            unique_ip[a[j]] = 1
        elif unique_ip[a[j]] >= 0:
            unique_ip[a[j]] += 1
        if unique_ip[a[j]] >= k:
            unique_ip[a[j]] = -1
    for ip in unique_ip:
        if unique_ip[ip] > 0:
            unique_ip[ip] = 0

for ip in unique_ip:
    if unique_ip[ip] == -1:
        print(ip)
