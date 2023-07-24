


def binarySearch(arr, val):
    low = 0 
    high = len(arr)
    mid = int((low+high)/2)
    while(low<=high):
        if(arr[mid] == val):
            return mid
        elif(arr[mid]< val):
            low = mid + 1
            mid = int((low+high)/2)
        else:
            high = mid - 1
            mid = int((low+high)/2)

    return -1


print(binarySearch([3,4,5,6,7,8,9,10,11,17],5))
        

