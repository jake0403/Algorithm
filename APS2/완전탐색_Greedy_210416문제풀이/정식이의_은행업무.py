T = int(input())
for tc in range(1, T+1):
    binary, ternary = input(), input()
    base2 = []
    base3 = []
    for b in range(len(binary)):
        if binary[b] == '0':
            l = list(binary)
            l[b] = '1'
            base2.append(''.join(l))
        else:
            l = list(binary)
            l[b] = '0'
            base2.append(''.join(l))
    for t in range(len(ternary)):
        tr = ternary[t]
        for i in range(3):
            if ternary[t] != str(i):
                l = list(ternary)
                l[t] = str(i)
                base3.append(''.join(l))
    base2 = [int(x, 2) for x in base2]
    base3 = [int(x, 3) for x in base3]
    ans = 0
    if len(base2) < len(base3):
        for t in base2:
            if t in base3:
                ans = t
                break
    else:
        for t in base3:
            if t in base2:
                ans = t
                break
    print(f'#{tc} {ans}')