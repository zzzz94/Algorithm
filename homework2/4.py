def inverse_pairs_core(s, l, r):
    if l >= r:
        return 0
    temp = s[:]
    m = (l + r) // 2
    count = 0
    inverse_pairs_core(s, l, m)
    inverse_pairs_core(s, m+1, r)
    i = m
    j = r
    k = len(temp[l:r+1]) - 1
    while i >= l and j >= m + 1:
        if s[i] > s[j]:
            temp[k] = s[i]
            k -= 1
            i -= 1
            count += j - m
        else:
            temp[k] = s[j]
            k -= 1
            j -= 1
    while i >= l:
        temp[k] = s[i]
        k -= 1
        i -= 1
    while j >= m + 1:
        temp[k] = s[j]
        k -= 1
        j -= 1
    s[:] = temp
    return count


def inverse_pairs(s, l, r):
    if l == r:
        return 0
    k = (l + r) // 2
    return inverse_pairs_core(s, l, k) + inverse_pairs_core(s, k+1, r) + inverse_pairs_core(s, l, r)

s = list('352164')
print(inverse_pairs(s, 0, len(s) - 1))