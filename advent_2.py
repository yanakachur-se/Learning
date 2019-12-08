#solution https://adventofcode.com/2019/day/1
fname = 'input.txt'
hand = open(fname)
s = 0
s1 = 0
for f in hand:
    f = int(f.rstrip())
    while f >= 6:
        f = f // 3 - 2
        s = s + f
print(s)
