def max_sublist(a, l, r):
    if l == r:
        return a[l]
    k = (l + r) // 2
    max_sum = 0
    lsum = 0
    i = k
    while i >= l:
        lsum += a[i]
        i -= 1
        if lsum > max_sum:
            max_sum = lsum
    lsum = max_sum
    rsum = 0
    max_sum = 0
    i = k+1
    while i<= r:
        rsum += a[i]
        i += 1
        if rsum > max_sum:
            max_sum = rsum
    rsum = max_sum
    return max(max_sublist(a, l, k), max_sublist(a, k+1, r), rsum + lsum)

a = [-2, -5, 6, -2, -3, 1, 5, -6]
print(max_sublist(a, 0, len(a) - 1))