import numpy  # Numpy lib

# Test array
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Mean
x = numpy.mean(speed)
print(x)

# Sorting the array using bubble sort
def bubble(array):
    length = len(array) # length of the array
    for i in range(length - 1): # This will reduce the number of times we need to run the nested loop each term (Dont mind the minus 1 there) - Its there because after testing we have realized that we only need lenght -1 amount of reduces before j becomes 0

        for j in range(length - 1 - i): # Minus one there so we dont have to check the last term
            # Checks if current value is bigger than the next value
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]  # If so, it switches them out
    return array

sorted_speed = bubble(speed)


# Sorting using insertion search
def insertion(array):
    n = len(array)
    for i in range(1, n):
        insert_index = i
        current_value = array.pop(i)
        for j in range(i-1, -1, -1):
            if array[j] > current_value:
                insert_index = j
        array.insert(insert_index, current_value)


speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
print(speed)
insertion(speed)
