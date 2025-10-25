# Author: David
# Implementation of an insertion sort in python

def insertion_sort(arr):
    for i in range(1, len(arr)): # Iterates from the second to the last loop
        j = i  # Currently compared value
        # If the previous value is bigger than the current value and the index is not 0...
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1] # Swaps the values
            j -= 1   # Checks the leftmost items
    # Return the sorted arrray
    return arr

# Array to be sorted
arr = [80, 12, 48, 42, 19, 14, 67, 42]
sorted_arr = insertion_sort(arr) #Sorted array
print(sorted_arr)
