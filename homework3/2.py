def methods_num(n):
    a = [0 for _ in range(n + 1)]
    a[1] = 1
    a[2] = 2
    for i in range(3, n + 1):
        a[i] = a[i - 1] + a[i - 2]
    return a[n]

print(methods_num(3))