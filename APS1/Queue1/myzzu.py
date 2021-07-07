# 마이쮸의 개수
N = 20
# 큐 초기화
queue = [(1,0)]

# (0,0) [0] : 사람 번호, [1] : 직전까지 받았던 마이쮸의 개수

new_people = 1
last_people = 0

while N > 0:
    # 받으러 온 사람, 저번까지 받은 개수
    num, cnt = queue.pop(0)
    # 마지막으로 받으러 온 사람
    last_people = num
    # 저번에 받은 개수 + 지금 받은 개수
    cnt+=1
    # num이라는 친구가 cnt 개수만큼 가져감
    N -= cnt
    new_people+=1

    queue.append((num, cnt))
    queue.append((new_people, 0))