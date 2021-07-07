N = 3
card = [4, 5, 6]

# 반복문을 이용해서 작성

# run?
# triplet?

# run = False
# tri = False
#
# for i in range(N):
#     for j in range(N):
#         if j != i :
#             for k in range(N):
#                 if k != i and k != j:
#                     print(card[i], card[j], card[k])
#
#                     # run을 검사
#                     if card[i]+1 == card[j] and card[i]+2 == card[k]:
#                         run = True
#
#                     # triplet 검사
#                     if card[i] == card[j] == card[k]:
#                         tri = True
#
#                     if run and tri:
#                         print("babyjin")

# 그리디 알고리즘

num = 444345
c = [0]*12      #6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
    c[num%10] +=1
    num//=10

i = 0
tri = run = 0

while i < 10 :
    if c[i] >= 3 :  #triplet 검사 후 데이터 삭제
        c[i]-=3
        tri+=1
        continue

    if c[i] >= 1 and c[i+1]>=1 and c[i+2] >= 1:     #run 검사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run+=1
        continue
    i+=1

if run + tri == 2 : print("Baby Gin")
else: print("Lose")