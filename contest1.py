with open("input.txt", "r") as f:
    n = int(f.readline())
    a = [int(i) for i in f.readline().split()]

a.sort()

with open("output.txt", "w") as f:
    f.write(" ".join(str(i) for i in a))