data = 'data\\p022_names.txt'
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

d = dict(zip(letters, range(1, 26 + 1)))

with open(data, 'r') as f:
    lines = sorted(f.readline().split(','))
    res = 0
    for idx, line in enumerate(lines):
        line = line.replace('"', '')
        score = 0
        for w in line:
            score += d[w]
        res += score * (idx + 1)

print(res)
