bit = input()
for i in range(10):
    s = 0
    for j in range(7):
        s += int(bit[i*7+j])*(1<<(6-j))
    print(s, end=' ')