import sys
input = lambda : sys.stdin.readline().strip()

def color_check():
    k = card[0]
    flag = 1
    for i in range(1,N):
        if k[0] != card[i][0]:
            flag = 0
            return flag
    return flag

def num_check():
    num_arr = [0]*N
    left = 0
    right = 1
    cnt = 0
    while right < N:
        if card[left][1] == card[right][1]:
            cnt+=1
            right+=1
            if right == 5:
                for i in range(left, right):
                    num_arr[i] = cnt
        else:
            if cnt:
                for i in range(left,right):
                    num_arr[i] = cnt
                cnt = 0
            left = right
            right = left + 1
    for i in range(N):
        if num_arr[i]:
            return num_arr
    else:
        # 숫자 연속일 때
        for i in range(N-1):
            if card[i][1] != card[i+1][1] + 1:
                return num_arr
        return [6,6,6,6,6]

N = 5
card = []
answer = 0
for i in range(N):
    color, num = input().split()
    card.append([color, int(num)])

card.sort(key= lambda x: -x[1])
cc = color_check()
num_arr = num_check()
# 색이 모두 같을 때
if cc:
    # 1번 조건
    if num_arr == [4,4,4,4,4]:
        answer = 900 + card[0][1]
    # 4번 조건
    else:
        if num_arr.count(3) == 4 :
            answer = card[num_arr.index(3)][1] + 800
        elif num_arr.count(2) == 3 and num_arr.count(1) == 2:
            answer = card[num_arr.index(2)][1] * 10 + card[num_arr.index(1)][1] + 700
        else:
            answer = 600 + card[0][1]
else:
    if num_arr.count(3) == 4:
        answer = card[num_arr.index(3)][1] + 800
    elif num_arr.count(2) == 3 and num_arr.count(1) == 2:
        answer = card[num_arr.index(2)][1] * 10 + card[num_arr.index(1)][1] + 700
    elif num_arr == [6,6,6,6,6]:
        answer = card[0][1] + 500
    elif num_arr.count(2) == 3:
        answer = card[num_arr.index(2)][1] + 400
    elif num_arr.count(1) == 4:
        i = num_arr.index(1)
        num_arr[i] = num_arr[i+1] = 2
        j = num_arr.index(1)
        if card[i][1] > card[j][1]:
            card[i][1]* 10 + card[j][1] + 300
        else:
            card[j][1] * 10 + card[i][1] + 300
    elif num_arr.count(1) == 2:
        answer = card[num_arr.index(1)][1] + 200
    else:
        answer = card[0][1] + 100

print(answer)