a = list(map(int, "-5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7".split()))
min = 5
max = 15
print([i for i in range(0, len(a)) if a[i] >= min and a[i] < max])