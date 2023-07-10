# Linear Search 
# Time Complexity
# Worst Case Time Complexity - O(n)
# Average Case Time Complexity - O(n)
# Best Case Time Complexity - O(1)

arr = [1,5,6,7,8,9,10,11]
target = 10

def linear_search(arr,target):
    if(len(arr)==0):
        return -1
    for i in range(0,len(arr)):
        if(arr[i] == target):
            return i
    return -1

print(linear_search(arr, target))