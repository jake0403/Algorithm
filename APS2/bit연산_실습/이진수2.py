result = ''
cnt = 0
num = 0.625
while True:
        next_num = num * 2
        result += str(int(next_num))
        num = next_num - int(next_num)
        cnt += 1
        if num == 0.0:
            break

        if cnt > 13:
            break
print(cnt)