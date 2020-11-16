#!python
from math import ceil, floor
from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k) Runs through input list twice
    Memory usage: O(n+k) Uses two additional arrays, output and a count (k is maximum possible value in array)"""
    
    if not numbers:
        return []
    
    # Find range of given numbers (minimum and maximum integer values)
    output = list() * len(numbers)
    # Create list of counts with a slot for each number in input range
    count = [0] * (max(numbers)+1)

    # Loop over given numbers and increment each number's count
    for num in numbers:
        count[num] += 1
    # print(count)
    # Loop over counts and append that many numbers into output list
    for i, each in enumerate(count):
        for _ in range(each):
            output.append(i)
    numbers[:] = output
    return numbers

# Stretch: Improve this to mutate input instead of creating new output list
def counting_sort_mutated(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k) Runs through input list once and all possible values (count)
    Memory usage: O(k) Uses additional count array (which makes this one not stable)"""
    if not numbers:
        return []
    # Find range of given numbers (minimum and maximum integer values)
    # Create list of counts with a slot for each number in input range
    count = [0] * (max(numbers)+1)

    # Loop over given numbers and increment each number's count
    for num in numbers:
        count[num] += 1

    # Loop over counts and append that many numbers into output list
    j = 0
    for i, each in enumerate(count):
        while each > 0:
            numbers[j] = i
            each -= 1
            j += 1
    return numbers

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: 
      Best/Avg: O(n+k) Creating buckets takes O(n) time, insertion sort is O(k)
      Worst: O(n^2) When buckets are not evenly distributed/all items in one bucket (takes on worst time complexity of sorting algo)
    Memory usage: O(n+k) n buckets, k possible values"""
    if not numbers:
        return []
    
    # Find range of given numbers (minimum and maximum values)
    divider = max(numbers) + 1 // len(numbers)

    # Create list of buckets to store numbers in subranges of input range
    buckets = [[] for _ in range(len(numbers))]

    # Loop over given numbers and place each item in appropriate bucket
    for i in range(len(numbers)):
        b_index = numbers[i] // divider
        buckets[b_index].append(numbers[i])

    output = []
    # Sort each bucket using any sorting algorithm (recursive or another)
    # Loop over buckets and append each bucket's numbers into output list
    for bucket in buckets:
        insertion_sort(bucket)
        output.extend(bucket)
    numbers[:] = output
    return numbers
#     # FIXME: Improve this to mutate input instead of creating new output list