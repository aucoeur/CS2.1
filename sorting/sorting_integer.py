#!python

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k) Runs through input list twice
    Memory usage: O(n+k) Uses two additional arrays, output and a count (k is maximum possible value in array)"""
    # Find range of given numbers (minimum and maximum integer values)
    output = list() * len(numbers)
    # Create list of counts with a slot for each number in input range
    count = [0 for each in range(max(numbers)+1)]

    # Loop over given numbers and increment each number's count
    for num in numbers:
        count[num] += 1
    # print(count)
    # Loop over counts and append that many numbers into output list
    for i, each in enumerate(count):
        for _ in range(each):
            output.append(i)
    return output

# Stretch: Improve this to mutate input instead of creating new output list
def counting_sort_mutated(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k) Runs through input list once and all possible values (count)
    Memory usage: O(k) Uses additional count array (which makes this one not stable)"""
    # Find range of given numbers (minimum and maximum integer values)
    # Create list of counts with a slot for each number in input range
    count = [0 for each in range(max(numbers)+1)]

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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list