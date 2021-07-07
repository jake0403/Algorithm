T = int(input())
for tc in range(1, T+1):
     short = input()
     long = input()
     max_num = 0
     for s in short:
         count = 0
         for l in long:
             if s == l:
                 count+=1
         if max_num < count:
             max_num = count
     print('#{} {}'.format(tc, max_num))