import sys
#
input = lambda : sys.stdin.readline().strip()
#
# def binarySearch(s,e, n):
#
#     while s <= e:
#         mid = (s+e) // 2
#         if note1[mid] == n:
#             return 1
#         elif note1[mid] < n:
#             s = mid+1
#         else:
#             e = mid -1
#     return 0
#
#
# T = int(input())
# for tc in range(T):
#     n1 = int(input())
#     note1 = sorted(list(map(int, input().split())))
#     n2 = int(input())
#     note2 = list(map(int, input().split()))
#
#     s = 0
#     e = n1-1
#     for n in note2:
#         print(binarySearch(s,e,n))
T = int(input())
for tc in range(T):
    n1 = int(input())
    note1 = set(map(int, input().split()))
    n2 = int(input())
    note2 = list(map(int, input().split()))

    for i in range(n2):
        if note2[i] in note1:
            print(1)
        else:
            print(0)