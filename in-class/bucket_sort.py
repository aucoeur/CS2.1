from string import ascii_lowercase

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: 
        - Worst/Avg: O(n^2) when items are in reverse sorted order or randomly scrambled 
        - Best: O(n) when current value is > then precending value, insertion is O(1) constant time (outer loop runs n times but inner loop doesn't run at all) or if array is already sorted
    Memory usage: O(1), extra variable used"""

    # Set sorted subarray starting at index 0, unsorted subarray starting at index 1
    for i in range(1, len(items)):
        # Take first unsorted item
        current = items[i]
        previous = i - 1

        # Exits when previous = -1 or if current > preceding value
        while previous >= 0 and current < items[previous]:
            # slide sorted value one index to the right
            items[previous+1] = items[previous]
            # move sorted index pointer back one to evaluate if current < precendin prev 
            previous = previous - 1
            
        # Insert current in sorted order in front of previous item pointer
        items[previous + 1] = current
    return items


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: 
      Best/Avg: O(n+k) Creating buckets takes O(n) time, insertion sort is O(k)
      Worst: O(n^2) When buckets are not evenly distributed/all items in one bucket (takes on worst time complexity of sorting algo)
    Memory usage: O(n+k) n buckets, k possible values"""
    if not numbers:
        return []
    try:
        num_buckets = len(numbers)
        maximum = max(numbers) + 1

    except TypeError:
        num_buckets = 26
        max_str = max(numbers).lower()
        maximum = ascii_lowercase.index(max_str[0])

    # Find range of given numbers (minimum and maximum values)
    divider = maximum + 1 // num_buckets

    # Create list of buckets to store numbers in subranges of input range
    buckets = [[] for _ in range(num_buckets)]

    # Loop over given numbers and place each item in appropriate bucket
    for i, each in enumerate(numbers):
        b_index = i // divider
        buckets[b_index].append(each)

    output = []
    # Sort each bucket using any sorting algorithm (recursive or another)
    # Loop over buckets and append each bucket's numbers into output list
    for bucket in buckets:
        insertion_sort(bucket)
        output.extend(bucket)
    
    return output
    # FIXME: Improve this to mutate input instead of creating new output list

numbers = [4,12,6,32,8,6,15,41,25,56,22,74,65,30,13]
# numbers = [5, 7, 3]
# numbers = [5, 3]
# numbers = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
sorted_items = sorted(numbers)  
print(numbers)
print(sorted_items)
print(bucket_sort(numbers, len(numbers)))