sn , en = input().split()
cnt = 1
while sn != en:
    if int(en) > 1 and en[-1] == '1':
        en = en[:-1]
        cnt+=1
    elif int(en) % 2 == 0:
        en = str(int(en)//2)
        cnt+=1
    else:
        cnt = -1
        break
print(cnt)