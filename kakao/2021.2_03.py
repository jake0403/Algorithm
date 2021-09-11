fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
import math
def solution(fees, records):
    answer = []
    records = [x.split() for x in records]
    records.sort(key= lambda x: x[1])
    print(records)
    car_cnt = 1
    for i in range(len(records)-1):
        if records[i][1] != records[i+1][1]:
            car_cnt+=1
    park_time = [[] for _ in range(car_cnt)]
    tmp = records[0][1]
    idx = 0
    for i in range(len(records)):
        if records[i][1] != tmp:
            idx += 1
            tmp = records[i][1]
        park_time[idx].append(records[i][0])
    print(park_time)
    park_charge = []
    for i in range(car_cnt):
        total = 0
        if len(park_time[i]) % 2 !=0:
            park_time[i].append('23:59')
        for j in range(0,len(park_time[i]),2):
            in_hour, in_minutes = park_time[i][j].split(":")
            out_hour, out_minutes = park_time[i][j+1].split(":")
            in_hour = int(in_hour)
            in_minutes = int(in_minutes)
            out_hour = int(out_hour)
            out_minutes = int(out_minutes)
            if out_minutes < in_minutes:
                out_hour-=1
                out_minutes+=60
            total += (out_hour - in_hour)*60 + (out_minutes - in_minutes)
        print(total)
        if total <= fees[0]:
            answer.append(fees[1])
        else:
            charge = fees[1] + (math.ceil((total - fees[0]) / fees[2])*fees[3])
            answer.append(charge)
    return answer


print(solution(fees, records))