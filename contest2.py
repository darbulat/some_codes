def mostFrequent(a, n):
    a.sort()
    max_count = 1
    res = a[0]
    curr_count = 1

    for i in range(1, n):
        if a[i] == a[i - 1]:
            curr_count += 1
        else:
            if curr_count >= max_count:
                max_count = curr_count
                res = a[i - 1]
            curr_count = 1

    if curr_count >= max_count:
        max_count = curr_count
        res = a[n - 1]
    return res


n = int(input())
a = [int(i) for i in input().split()]

print(mostFrequent(a, n))
