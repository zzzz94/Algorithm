def methods(m, n):
    g = [[0 for _ in range(m + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        g[i][1] = 1
        g[1][i] = 1
    for i in range(2, m + 1):
        for j in range(2, i + 1):
            if j != i:
                g[i][j] = g[i][j-1] + g[i - j][j]
            else:
                g[i][i] = g[i][i-1] + 1
    return g[m][n]
m = 5
n = 4
print(methods(m, n))