def c(n, k):
    kk, nn = 1, 1
    for i in range(1, k + 1):
        nn *= (n - k + i)
        kk *= i
    res = nn // kk
    return res

print(c(40, 20))
