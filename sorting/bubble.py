# Author: David
# Bubble sort python implementation

def bubble(arr):
    n = len(arr) # length of arr
    for i in range(n -1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]: # Switches numbers if j > j+1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # Return a sorted array
    return arr

# Unsorted array
arr = [67, 43, 25, 98, 31, 52, 73, 87]
sorted_list = bubble(arr) # Sorted array
print(sorted_list)
