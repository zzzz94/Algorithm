def LCS(x, y, z):
    c = [[[0 for _ in range(len(z) + 1)] for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            for k in range(1, len(z) + 1):
                if x[i-1] == y[j-1] and y[j-1] == z[k-1]:
                    c[i][j][k] = c[i-1][j-1][k-1] + 1
                elif c[i-1][j][k] >= c[i][j-1][k] and c[i-1][j][k] >= c[i][j][k-1]:
                    c[i][j][k] = c[i-1][j][k]
                elif c[i][j-1][k] >= c[i-1][j][k] and c[i][j-1][k] >= c[i][j][k-1]:
                    c[i][j][k] = c[i][j-1][k]
                else:
                    c[i][j][k] = c[i][j][k-1]
    return c[len(x)][len(y)][len(z)]

a = 'BDCABA'
b = 'ABCBDAB'
c = 'BCAB'
print(LCS(a, b, c))