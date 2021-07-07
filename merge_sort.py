'''
6 5 3 1 8 7 2 4
'''


arr = [6,5,3,1,8,7,2,4]

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merge_arr = []

    low = high = 0

    while low < len(low_arr) and high < len(high_arr):
        if low_arr[low] < high_arr[high]:
            merge_arr.append(low_arr[low])
            low+=1
        else:
            merge_arr.append(high_arr[high])
            high+=1

    merge_arr += low_arr[low:]
    merge_arr += high_arr[high:]
    return merge_arr

print(merge_sort(arr))