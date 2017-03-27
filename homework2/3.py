def decode_num(s, l, r):
    if l == r and s[l] == '0':
        return 0
    if l >= r:
        return 1
    k = (l + r) // 2
    mid = (ord(s[k]) - ord('0')) * 10 + ord(s[k+1]) - ord('0')
    # print(mid)
    return decode_num(s, l, k) * decode_num(s, k+1, r) + (1 if s[k] != '0' and mid >= 1
                                                               and mid <= 26 else 0) * decode_num(s, l, k-1) * decode_num(s, k+2, r)

s = '20124'
print(decode_num(s, 0, len(s) - 1))