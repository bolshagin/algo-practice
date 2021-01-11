def collatz(n):
    return int(n / 2) if n % 2 == 0 else (3 * n + 1)

max_len, max_num = 1, 1

for x in range(500000, 1000000):
    l, first = 1, x
    while x > 1:
        x = collatz(x)
        l += 1
    if l > max_len:
        max_len, max_num = l, first

print(f'{max_num}, {max_len}')
