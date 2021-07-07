
def binarySearch(a, key):
    start = 0
    end = len(a)-1
    count = 0
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
        count+=1
    return count



binarySearch()
