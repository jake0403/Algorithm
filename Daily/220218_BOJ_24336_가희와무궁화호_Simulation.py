import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().strip()

def calc(s, e, l1, l2):
    sh, sm = s.split(":")
    eh, em = e.split(":")
    if sm > em :
        em = str(int(em)+60)
        eh = str(int(eh)-1)
    # 시간이 00시(하루가 넘어갔을 때)가
    if int(sh) > int(eh):
        eh = str(int(eh)+24)

    hh, mm = int(eh)-int(sh) , int(em) - int(sm)
    if dist[l1] > dist[l2]:
        d = dist[l1] - dist[l2]
    else:
        d = dist[l2] - dist[l1]
    return round(d/(hh+(mm/60)),8)



N, Q = map(int, input().split())
table = defaultdict(list)
for _ in range(N):
    des, arrive, leave = input().split()
    table[des] = [arrive, leave]
question = []
for _ in range(Q):
    question.append(list(input().split()))
dist = {
    "Seoul": 0.0,
    "Yeongdeungpo": 9.1,
    "Anyang": 23.9,
    "Suwon": 41.5,
    "Osan": 56.5,
    "Seojeongri": 66.5,
    "Pyeongtaek": 75.0,
    "Seonghwan": 84.4,
    "Cheonan": 96.6,
    "Sojeongni": 107.4,
    "Jeonui": 114.9,
    "Jochiwon": 129.3,
    "Bugang": 139.8,
    "Sintanjin": 151.9,
    "Daejeon": 166.3,
    "Okcheon": 182.5,
    "Iwon": 190.8,
    "Jitan": 196.4,
    "Simcheon": 200.8,
    "Gakgye": 204.6,
    "Yeongdong": 211.6,
    "Hwanggan": 226.2,
    "Chupungnyeong": 234.7,
    "Gimcheon": 253.8,
    "Gumi": 276.7,
    "Sagok": 281.3,
    "Yangmok": 289.5,
    "Waegwan": 296.0,
    "Sindong": 305.9,
    "Daegu": 323.1,
    "Dongdaegu": 326.3,
    "Gyeongsan": 338.6,
    "Namseonghyeon": 353.1,
    "Cheongdo": 361.8,
    "Sangdong": 372.2,
    "Miryang": 381.6,
    "Samnangjin": 394.1,
    "Wondong": 403.2,
    "Mulgeum": 412.4,
    "Hwamyeong": 421.8,
    "Gupo": 425.2,
    "Sasang": 430.3,
    "Busan": 441.7,
}
for i in range(Q):
    print(calc(table[question[i][0]][1], table[question[i][1]][0], question[i][0], question[i][1]))

