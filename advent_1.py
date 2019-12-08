fname = 'input.txt'
hand = open(fname)
s = 0
for num in hand:
    num = num.rstrip()
    f = int(num) // 3 - 2
    s = s + f
print(s)
