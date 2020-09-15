# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        cur_index = i
        smallest_value = arr[cur_index]
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for unsorted_index in range(cur_index, len(arr)):
            if arr[unsorted_index] < smallest_value:
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index

        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Your code here
    counter = True
    while (counter):
        counter = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                counter = True
    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here
    if not maximum and arr:
        maximum = max(arr)
    if arr == []:
        return arr
    if min(arr) < 0:
        return 'Error, negative numbers not allowed in Count Sort'
    # [5, 5, 4, 3, 2, 1]
    count_of_nums = maximum + 1  # to include 0
    # createing an array of numbers
    array_of_counts = [0] * count_of_nums
    # [0, 1, 1 ,1 ,1, 2]
    for item in arr:
        array_of_counts[item] += 1

    index = 0

    for num in range(count_of_nums): # [0, 1, 2, 3 ,4 ,5]
        for num_in in range(array_of_counts[num]): #array_of_counts[0] = 0 
            # range(0) = [] so you ended up not overiding anything in the arr[0] and not moving 
            # the index over
            arr[index] = num
            index += 1
    # [1, 2 , 3, 4, 5, 5]
    return arr
