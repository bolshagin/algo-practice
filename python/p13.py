data = 'data\\p13.txt'
xs = 0

with open(data) as f:
    for line in f:
        xs += int(line)

print(str(xs)[:10])
