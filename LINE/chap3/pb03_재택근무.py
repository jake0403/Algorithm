from collections import defaultdict
num_teams = 3
remote_tasks = ["development","marketing","hometask"]
office_tasks = ["recruitment","education","officetask"]
employees = ["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]
result = [1,4,5,7]

empl = defaultdict(list)
answer = []
remote = []
office = []
worker = [[] for _ in range(num_teams+1)]
for i in range(len(employees)):
    empl[int(employees[i][0])].append(i+1)
    worker[int(employees[i][0])].append(i+1)
    work = employees[i].split(" ")[1:]
    flag = 0
    for w in work:
        if w in office_tasks:
            flag =1
            break
    if flag:
        office.append(i+1)
    else:
        remote.append(i+1)
all_remote = []

for i in range(1, num_teams+1):
    flag = 1
    for o in office:
        if o in worker[i]:
            flag = 0
            break
    if flag:
        all_remote.append(i)
for ar in all_remote:
    remote.remove(worker[ar][0])
print(office)
print(remote)
print(empl)
print(worker)
print(all_remote)
print(remote)