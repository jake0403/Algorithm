# from collections import deque
T = int(input())
for tc in range(T):
    N = int(input())
    phone = [input() for x in range(N)]
    phone.sort(key=len)
    # phone = deque(phone)
    answer = "YES"
    short = phone[0]
    for i in range(1,len(phone)):
        if short == phone[i][:len(short)]:
            answer = "NO"
            break

    print(answer)