T = int(input())
for tc in range(1,T+1):
    n, a = input().split()
    b = [format(int(i, 16),'04b') for i in a]
    print((b))
    print(f"#{tc} {''.join(b)}")

