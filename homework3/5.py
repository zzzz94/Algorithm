def windy():
    d = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(10):
        d[1][i] = 1
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(0, 10):
                if abs(j - k) > 1:
                    d[i][j] += d[i - 1][k]
    return d

def find(a, d):
    a = list(map(lambda x: ord(x) - ord('0'), str(a)))
    ans = 0
    for i in range(1,len(a)):
        for j in range(10):
            ans += d[i][j]
    for i in range(1, a[0]):
        ans += d[len(a)][i]
    if len(a) == 1:
        ans += 1
    for i in range(1, len(a)):
        for j in range(a[i]):
            if abs(j - a[i-1]) > 1:
                ans += d[len(a) - i][j]
    return ans

d = windy()
a = 25
b = 50
print(find(b+1, d))
print(find(a, d))
print(find(b + 1, d) - find(a, d))

